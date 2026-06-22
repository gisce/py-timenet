# coding=utf-8
from __future__ import unicode_literals, absolute_import

import unittest

from timenet.endpoints.check import CheckAPI
from timenet.endpoints.config import ConfigAPI
from timenet.endpoints.customers import CustomersAPI
from timenet.endpoints.groups import GroupsAPI
from timenet.endpoints.projects import ProjectsAPI
from timenet.endpoints.workers import WorkersAPI
from timenet.client import TimenetClient


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

    def assertCrudCalls(self, calls, base_endpoint, payload):
        self.assertEqual([
            {
                'method': 'GET',
                'endpoint': base_endpoint,
                'data': None,
                'params': None,
            },
            {
                'method': 'GET',
                'endpoint': '{}/5'.format(base_endpoint),
                'data': None,
                'params': None,
            },
            {
                'method': 'POST',
                'endpoint': base_endpoint,
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': '{}/5'.format(base_endpoint),
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': '{}/5'.format(base_endpoint),
                'data': None,
                'params': None,
            },
        ], calls)

    def test_client_version_uses_version_endpoint(self):
        client = self.make_client()
        api = TimenetClient(token='token')
        api.request = client.request

        api.get_version()

        self.assertLastCall(client, 'GET', 'version')

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

    def test_check_current_uses_optional_filters_as_params(self):
        client = self.make_client()

        CheckAPI(client).current(worker=42, checkpoint=7)

        self.assertLastCall(
            client,
            'GET',
            'check/current',
            params={'worker': 42, 'checkpoint': 7},
        )

    def test_check_current_without_filters_does_not_send_params(self):
        client = self.make_client()

        CheckAPI(client).current()

        self.assertLastCall(client, 'GET', 'check/current')

    def test_check_incidences_keep_expected_urls_params_and_bodies(self):
        client = self.make_client()
        payload = {'worker': 42, 'date': '2026-06-22', 'reason': 'forgot'}

        CheckAPI(client).get_incidences('2026-06-01', '2026-06-30', worker=42)
        CheckAPI(client).get_incidence(5)
        CheckAPI(client).create_incidence(payload)
        CheckAPI(client).update_incidence(5, payload)
        CheckAPI(client).delete_incidence(5)

        self.assertEqual([
            {
                'method': 'GET',
                'endpoint': 'check/incidences',
                'data': None,
                'params': {
                    'start': '2026-06-01',
                    'end': '2026-06-30',
                    'worker': 42,
                },
            },
            {
                'method': 'GET',
                'endpoint': 'check/incidences/5',
                'data': None,
                'params': None,
            },
            {
                'method': 'POST',
                'endpoint': 'check/incidences',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'check/incidences/5',
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'check/incidences/5',
                'data': None,
                'params': None,
            },
        ], client.calls)

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

    def test_checktype_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Entry'}

        ConfigAPI(client).get_checktypes()
        ConfigAPI(client).get_checktype(5)
        ConfigAPI(client).create_checktype(payload)
        ConfigAPI(client).update_checktype(5, payload)
        ConfigAPI(client).delete_checktype(5)

        self.assertCrudCalls(client.calls, 'config/checktypes', payload)

    def test_checkpoint_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Main office'}

        ConfigAPI(client).get_checkpoints()
        ConfigAPI(client).get_checkpoint(5)
        ConfigAPI(client).create_checkpoint(payload)
        ConfigAPI(client).update_checkpoint(5, payload)
        ConfigAPI(client).delete_checkpoint(5)

        self.assertCrudCalls(client.calls, 'config/checkpoints', payload)

    def test_config_calendar_keeps_expected_params_and_body(self):
        client = self.make_client()
        payload = {'days': [{'date': '2026-06-22', 'daytype': 1}]}

        ConfigAPI(client).get_calendar('2026-06-01', '2026-06-30')
        ConfigAPI(client).set_calendar(payload)

        self.assertEqual([
            {
                'method': 'GET',
                'endpoint': 'config/calendar',
                'data': None,
                'params': {'start': '2026-06-01', 'end': '2026-06-30'},
            },
            {
                'method': 'PUT',
                'endpoint': 'config/calendar',
                'data': payload,
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

    def test_project_line_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'project': 9, 'name': 'Support'}

        ProjectsAPI(client).get_lines()
        ProjectsAPI(client).get_line(5)
        ProjectsAPI(client).create_line(payload)
        ProjectsAPI(client).update_line(5, payload)
        ProjectsAPI(client).delete_line(5)

        self.assertCrudCalls(client.calls, 'projects/lines', payload)

    def test_project_linetype_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Billable'}

        ProjectsAPI(client).get_linetypes()
        ProjectsAPI(client).get_linetype(5)
        ProjectsAPI(client).create_linetype(payload)
        ProjectsAPI(client).update_linetype(5, payload)
        ProjectsAPI(client).delete_linetype(5)

        self.assertCrudCalls(client.calls, 'projects/linetypes', payload)

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

    def test_worker_extrahour_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'worker': 34, 'date': '2026-06-22', 'hours': 2}

        WorkersAPI(client).get_extrahours(
            '2026-06-01',
            '2026-06-30',
            worker=34,
        )
        WorkersAPI(client).get_extrahour(5)
        WorkersAPI(client).create_extrahour(payload)
        WorkersAPI(client).update_extrahour(5, payload)
        WorkersAPI(client).delete_extrahour(5)

        self.assertEqual([
            {
                'method': 'GET',
                'endpoint': 'workers/extrahours',
                'data': None,
                'params': {
                    'start': '2026-06-01',
                    'end': '2026-06-30',
                    'worker': 34,
                },
            },
            {
                'method': 'GET',
                'endpoint': 'workers/extrahours/5',
                'data': None,
                'params': None,
            },
            {
                'method': 'POST',
                'endpoint': 'workers/extrahours',
                'data': payload,
                'params': None,
            },
            {
                'method': 'PUT',
                'endpoint': 'workers/extrahours/5',
                'data': payload,
                'params': None,
            },
            {
                'method': 'DELETE',
                'endpoint': 'workers/extrahours/5',
                'data': None,
                'params': None,
            },
        ], client.calls)

    def test_customer_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'name': 'Customer'}

        CustomersAPI(client).list()
        CustomersAPI(client).get(5)
        CustomersAPI(client).create(payload)
        CustomersAPI(client).update(5, payload)
        CustomersAPI(client).delete(5)

        self.assertCrudCalls(client.calls, 'customers', payload)

    def test_customer_contact_crud_endpoints_keep_expected_urls_and_bodies(self):
        client = self.make_client()
        payload = {'customer': 5, 'name': 'Contact'}

        CustomersAPI(client).get_contacts()
        CustomersAPI(client).get_contact(5)
        CustomersAPI(client).create_contact(payload)
        CustomersAPI(client).update_contact(5, payload)
        CustomersAPI(client).delete_contact(5)

        self.assertCrudCalls(client.calls, 'customers/contacts', payload)


if __name__ == '__main__':
    unittest.main()
