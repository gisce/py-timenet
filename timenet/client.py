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
    def __init__(self, token, base_url="https://timenet.gpisoftware.com/api/public"):
        self.token = token
        self.base_url = base_url
        self.headers = {
            'Content-Type': 'application/json',
            'token': self.token
        }
        self.check = CheckAPI(self)  # Instanciem CheckAPI com a atribut del client
        self.config = ConfigAPI(self)  # Instanciem ConfigAPI
        self.groups = GroupsAPI(self)  # Instanciem GroupsAPI
        self.projects = ProjectsAPI(self)  # Instanciem ProjectsAPI
        self.workers = WorkersAPI(self)  # Instanciem WorkersAPI

    def request(self, method, endpoint, data=None, params=None):
        """
        Envia una sol·licitud HTTP a l'API de Timenet.

        :param method: Mètode HTTP ('GET', 'POST', 'PUT', 'DELETE').
        :param endpoint: Endpoint de l'API (relatiu a la base_url).
        :param data: Dades a enviar en el cos de la sol·licitud (opcional).
        :param params: Paràmetres de consulta per a la sol·licitud (opcional).
        :return: Resposta JSON de l'API o un diccionari amb l'error.
        """
        url = "{}/{}".format(self.base_url, endpoint.strip("/"))
        try:
            if method == 'GET':
                r = requests.get(url, headers=self.headers, params=params)
            elif method == 'POST':
                r = requests.post(url, headers=self.headers, data=json.dumps(data))
            elif method == 'PUT':
                r = requests.put(url, headers=self.headers, data=json.dumps(data))
            elif method == 'DELETE':
                r = requests.delete(url, headers=self.headers)
            else:
                raise ValueError("Invalid HTTP method")
            return r.json()
        except Exception as e:
            return {'ok': False, 'error': str(e)}

