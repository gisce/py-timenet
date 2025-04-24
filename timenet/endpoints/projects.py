# coding=utf-8
from __future__ import unicode_literals, absolute_import

class ProjectsAPI(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        Obté una llista de projectes.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects')

    def get(self, id_):
        """
        Obté informació d'un projecte específic.

        :param id_: ID del projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects/{}'.format(id_))

    def create(self, data):
        """
        Crea un nou projecte.

        :param data: Dades del projecte (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'projects', data=data)

    def update(self, id_, data):
        """
        Actualitza un projecte existent.

        :param id_: ID del projecte.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'projects/{}'.format(id_), data=data)

    def close(self, id_):
        """
        Tanca un projecte.

        :param id_: ID del projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'projects/{}/close'.format(id_))

    def open(self, id_):
        """
        Reobre un projecte.

        :param id_: ID del projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'projects/{}/open'.format(id_))

    def delete(self, id_):
        """
        Elimina un projecte.

        :param id_: ID del projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'projects/{}'.format(id_))


