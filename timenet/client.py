# coding=utf-8
from __future__ import unicode_literals, absolute_import
import requests
import json
from .endpoints.check import CheckAPI  # Importem CheckAPI
from .endpoints.config import ConfigAPI  # Importem ConfigAPI
from .endpoints.groups import GroupsAPI  # Importem GroupsAPI
from .endpoints.projects import ProjectsAPI  # Importem ProjectsAPI
from .endpoints.workers import WorkersAPI  # Importem WorkersAPI

class TimenetClient(object):
    def __init__(self, token, base_url="https://timenet.gpisoftware.com/api/public",
                 timeout=30, session=None):
        self.token = token
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests
        self.headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }
        self.check = CheckAPI(self)  # Instanciem CheckAPI com a atribut del client
        self.config = ConfigAPI(self)  # Instanciem ConfigAPI
        self.groups = GroupsAPI(self)  # Instanciem GroupsAPI
        self.projects = ProjectsAPI(self)  # Instanciem ProjectsAPI
        self.workers = WorkersAPI(self)  # Instanciem WorkersAPI

    def _decode_response(self, response):
        try:
            return response.json()
        except ValueError as e:
            return {
                'ok': False,
                'error': 'Invalid JSON response: {}'.format(e),
                'status_code': getattr(response, 'status_code', None),
                'response_text': getattr(response, 'text', None),
            }

    def request(self, method, endpoint, data=None, params=None):
        """
        Envia una sol·licitud HTTP a l'API de Timenet.

        :param method: Mètode HTTP ('GET', 'POST', 'PUT', 'DELETE').
        :param endpoint: Endpoint de l'API (relatiu a la base_url).
        :param data: Dades a enviar en el cos de la sol·licitud (opcional).
        :param params: Paràmetres de consulta per a la sol·licitud (opcional).
        :return: Resposta JSON de l'API o un diccionari amb l'error.
        """
        method = method.upper()
        url = "{}/{}".format(self.base_url, endpoint.strip("/"))
        try:
            if method not in ('GET', 'POST', 'PUT', 'DELETE'):
                raise ValueError("Invalid HTTP method")

            body = None
            if data is not None:
                body = json.dumps(data)

            r = self.session.request(
                method,
                url,
                headers=self.headers,
                params=params,
                data=body,
                timeout=self.timeout,
            )
            if not 200 <= r.status_code < 300:
                result = self._decode_response(r)
                if isinstance(result, dict):
                    result.setdefault('ok', False)
                    result.setdefault('status_code', r.status_code)
                    return result
                return {
                    'ok': False,
                    'error': 'HTTP {}'.format(r.status_code),
                    'status_code': r.status_code,
                    'response': result,
                }
            return self._decode_response(r)
        except requests.exceptions.RequestException as e:
            return {'ok': False, 'error': str(e)}
        except ValueError as e:
            return {'ok': False, 'error': str(e)}
