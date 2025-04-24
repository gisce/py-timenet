# coding=utf-8
from __future__ import unicode_literals, absolute_import

class GroupsAPI(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        Obté una llista de grups.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'groups')

    def get(self, id_):
        """
        Obté informació d'un grup específic.

        :param id_: ID del grup.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'groups/{}'.format(id_))

    def create(self, data):
        """
        Crea un nou grup.

        :param data: Dades del grup (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'groups', data=data)

    def update(self, id_, data):
        """
        Actualitza un grup existent.

        :param id_: ID del grup.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'groups/{}'.format(id_), data=data)

    def delete(self, id_):
        """
        Elimina un grup.

        :param id_: ID del grup.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'groups/{}'.format(id_))

    def get_calendar(self, id_, start, end):
        """
        Obté el calendari d'un grup.

        :param id_: ID del grup.
        :param start: Data d'inici (format 'YYYY-MM-DD').
        :param end: Data de finalització (format 'YYYY-MM-DD').
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'groups/{}/calendar'.format(id_), params={'start': start, 'end': end})

    def set_calendar(self, id_, data):
        """
        Defineix el calendari d'un grup.

        :param id_: ID del grup.
        :param data: Dades del calendari (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'groups/{}/calendar'.format(id_), data=data)

