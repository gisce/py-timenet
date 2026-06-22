# coding=utf-8
from __future__ import unicode_literals, absolute_import

import json
import unittest

import requests

from timenet.client import TimenetClient


class FakeResponse(object):
    def __init__(self, status_code=200, payload=None, text=''):
        self.status_code = status_code
        self.payload = payload
        self.text = text

    def json(self):
        if isinstance(self.payload, Exception):
            raise self.payload
        return self.payload


class FakeSession(object):
    def __init__(self, response=None, exception=None):
        self.response = response or FakeResponse(payload={'ok': True})
        self.exception = exception
        self.calls = []

    def request(self, method, url, headers=None, params=None, data=None,
                timeout=None):
        self.calls.append({
            'method': method,
            'url': url,
            'headers': headers,
            'params': params,
            'data': data,
            'timeout': timeout,
        })
        if self.exception:
            raise self.exception
        return self.response


class TimenetClientRequestTest(unittest.TestCase):

    def make_client(self, session):
        return TimenetClient(
            token='token-123',
            base_url='https://example.test/api/',
            timeout=5,
            session=session,
        )

    def test_get_sends_headers_params_and_timeout(self):
        session = FakeSession(FakeResponse(payload={'workers': []}))
        client = self.make_client(session)

        result = client.request('GET', '/workers', params={'active': 1})

        self.assertEqual({'workers': []}, result)
        self.assertEqual(1, len(session.calls))
        call = session.calls[0]
        self.assertEqual('GET', call['method'])
        self.assertEqual('https://example.test/api/workers', call['url'])
        self.assertEqual({'Content-Type': 'application/json',
                          'token': 'token-123'}, call['headers'])
        self.assertEqual({'active': 1}, call['params'])
        self.assertIsNone(call['data'])
        self.assertEqual(5, call['timeout'])

    def test_post_serializes_body_as_json(self):
        session = FakeSession(FakeResponse(payload={'id': 10}))
        client = self.make_client(session)

        result = client.request('POST', 'workers', data={'name': 'Ada'})

        self.assertEqual({'id': 10}, result)
        self.assertEqual(json.dumps({'name': 'Ada'}), session.calls[0]['data'])

    def test_delete_accepts_params_and_body(self):
        session = FakeSession(FakeResponse(payload={'ok': True}))
        client = self.make_client(session)

        result = client.request(
            'DELETE',
            'workers/10',
            params={'force': 1},
            data={'reason': 'duplicate'},
        )

        self.assertEqual({'ok': True}, result)
        self.assertEqual({'force': 1}, session.calls[0]['params'])
        self.assertEqual(json.dumps({'reason': 'duplicate'}),
                         session.calls[0]['data'])

    def test_http_error_returns_status_code_and_api_error(self):
        session = FakeSession(FakeResponse(
            status_code=404,
            payload={'error': 'not found'},
        ))
        client = self.make_client(session)

        result = client.request('GET', 'workers/10')

        self.assertEqual(False, result['ok'])
        self.assertEqual(404, result['status_code'])
        self.assertEqual('not found', result['error'])

    def test_invalid_json_returns_error_context(self):
        session = FakeSession(FakeResponse(
            status_code=200,
            payload=ValueError('no json'),
            text='not-json',
        ))
        client = self.make_client(session)

        result = client.request('GET', 'workers')

        self.assertEqual(False, result['ok'])
        self.assertEqual(200, result['status_code'])
        self.assertIn('Invalid JSON response', result['error'])
        self.assertEqual('not-json', result['response_text'])

    def test_request_exception_returns_error(self):
        session = FakeSession(exception=requests.exceptions.Timeout('boom'))
        client = self.make_client(session)

        result = client.request('GET', 'workers')

        self.assertEqual(False, result['ok'])
        self.assertEqual('boom', result['error'])

    def test_invalid_method_returns_error_without_http_call(self):
        session = FakeSession()
        client = self.make_client(session)

        result = client.request('PATCH', 'workers')

        self.assertEqual(False, result['ok'])
        self.assertEqual('Invalid HTTP method', result['error'])
        self.assertEqual([], session.calls)


if __name__ == '__main__':
    unittest.main()
