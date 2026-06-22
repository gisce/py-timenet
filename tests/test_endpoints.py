# coding=utf-8
from __future__ import unicode_literals, absolute_import

import unittest

from timenet.endpoints.check import CheckAPI
from timenet.endpoints.config import ConfigAPI
from timenet.endpoints.groups import GroupsAPI
from timenet.endpoints.projects import ProjectsAPI
from timenet.endpoints.workers import WorkersAPI


class FakeClient(object):
    def __init__(self):
        self.calls = []

    def request(self, method, endpoint, data=None, params=None):
        call = {
            'method': method,
            'endpoint': endpoint,
            'data': data,
            'params': params,
        }
        self.calls.append(call)
        return {'ok': True}


class EndpointPayloadContractTest(unittest.TestCase):

    def make_client(self):
        return FakeClient()

    def assertLastCall(self, client, method, endpoint, data=None, params=None):
        self.assertEqual(1, len(client.calls))
        self.assertEqual({
            'method': method,
            'endpoint': endpoint,
            'data': data,
            'params': params,
        }, client.calls[0])

    def test_check_by_pin_posts_raw_payload_to_expected_endpoint(self):
        client = self.make_client()
        payload = {
            'pin': '1234',
            'checkpoint': 7,
            'date': '2026-06-22',
            'time': '08:30',
        }

        CheckAPI(client).by_pin(payload)

        self.assertLastCall(client, 'POST', 'check/bypin', data=payload)

    def test_check_by_worker_posts_raw_payload_to_expected_endpoint(self):
        client = self.make_client()
        payload = {
            'worker': 42,
            'checkpoint': 7,
            'date': '2026-06-22',
            'time': '17:00',
        }

        CheckAPI(client).by_worker(payload)

        self.assertLastCall(client, 'POST', 'check/byworker', data=payload)

    def test_group_calendar_puts_raw_payload_to_group_calendar_endpoint(self):
        client = self.make_client()
        payload = {
            'days': [
                {'date': '2026-06-22', 'daytype': 1},
                {'date': '2026-06-23', 'daytype': 2},
            ],
        }

        GroupsAPI(client).set_calendar(12, payload)

        self.assertLastCall(
            client,
            'PUT',
            'groups/12/calendar',
            data=payload,
        )

    def test_group_write_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Operations'}

        GroupsAPI(client).create(payload)
        GroupsAPI(client).update(12, payload)
        GroupsAPI(client).delete(12)

        self.assertEqual([
            {
                'method': 'POST',
                'endpoint': 'groups',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'groups/12',
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'groups/12',
                'data': None,
                'params': None,
            },
        ], client.calls)

    def test_worker_calendar_puts_raw_payload_to_worker_calendar_endpoint(self):
        client = self.make_client()
        payload = {
            'days': [
                {'date': '2026-06-22', 'daytype': 1},
            ],
        }

        WorkersAPI(client).set_calendar(34, payload)

        self.assertLastCall(
            client,
            'PUT',
            'workers/34/calendar',
            data=payload,
        )

    def test_daytype_write_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Holiday', 'color': '#ff0000'}

        ConfigAPI(client).create_daytype(payload)
        ConfigAPI(client).update_daytype(5, payload)
        ConfigAPI(client).delete_daytype(5)

        self.assertEqual([
            {
                'method': 'POST',
                'endpoint': 'config/daytypes',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'config/daytypes/5',
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'config/daytypes/5',
                'data': None,
                'params': None,
            },
        ], client.calls)

    def test_project_state_and_delete_endpoints_use_expected_urls(self):
        client = self.make_client()

        ProjectsAPI(client).close(9)
        ProjectsAPI(client).open(9)
        ProjectsAPI(client).delete(9)

        self.assertEqual([
            {
                'method': 'PUT',
                'endpoint': 'projects/9/close',
                'data': None,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'projects/9/open',
                'data': None,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'projects/9',
                'data': None,
                'params': None,
            },
        ], client.calls)

    def test_project_write_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Migration', 'code': 'MIG'}

        ProjectsAPI(client).create(payload)
        ProjectsAPI(client).update(9, payload)

        self.assertEqual([
            {
                'method': 'POST',
                'endpoint': 'projects',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'projects/9',
                'data': payload,
                'params': None,
            },
        ], client.calls)

    def test_worker_write_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Ada Lovelace', 'group': 12}

        WorkersAPI(client).create(payload)
        WorkersAPI(client).update(34, payload)
        WorkersAPI(client).delete(34)

        self.assertEqual([
            {
                'method': 'POST',
                'endpoint': 'workers',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'workers/34',
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'workers/34',
                'data': None,
                'params': None,
            },
        ], client.calls)

    def test_worker_pin_update_keeps_pin_in_expected_url(self):
        client = self.make_client()

        WorkersAPI(client).update_pin(34, '9999')

        self.assertLastCall(client, 'PUT', 'workers/34/pin/9999')


if __name__ == '__main__':
    unittest.main()
