# coding=utf-8
from __future__ import unicode_literals, absolute_import

class ConfigAPI(object):
    def __init__(self, client):
        self.client = client

    def get_company(self):
        """
        Obté la configuració de l'empresa.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/company')

    def get_daytypes(self):
        """
        Obté una llista de tipus de dies.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/daytypes')

    def get_daytype(self, id_):
        """
        Obté informació d'un tipus de dia específic.

        :param id_: ID del tipus de dia.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/daytypes/{}'.format(id_))

    def create_daytype(self, data):
        """
        Crea un nou tipus de dia.

        :param data: Dades del tipus de dia (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'config/daytypes', data=data)

    def update_daytype(self, id_, data):
        """
        Actualitza un tipus de dia existent.

        :param id_: ID del tipus de dia.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'config/daytypes/{}'.format(id_), data=data)

    def delete_daytype(self, id_):
        """
        Elimina un tipus de dia.

        :param id_: ID del tipus de dia.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'config/daytypes/{}'.format(id_))

    def get_checkpoints(self):
        """
        Obté una llista de checkpoints.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/checkpoints')


