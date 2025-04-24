# coding=utf-8
from __future__ import unicode_literals, absolute_import

class WorkersAPI(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        Obté una llista de treballadors.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'workers')

    def get(self, id_):
        """
        Obté informació d'un treballador específic.

        :param id_: ID del treballador.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'workers/{}'.format(id_))

    def create(self, data):
        """
        Crea un nou treballador.

        :param data: Dades del treballador (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'workers', data=data)

    def update(self, id_, data):
        """
        Actualitza un treballador existent.

        :param id_: ID del treballador.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'workers/{}'.format(id_), data=data)

    def delete(self, id_):
        """
        Elimina un treballador.

        :param id_: ID del treballador.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'workers/{}'.format(id_))

    def update_pin(self, id_, pin):
        """
        Actualitza el PIN d'un treballador.

        :param id_: ID del treballador.
        :param pin: Nou PIN.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'workers/{}/pin/{}'.format(id_, pin))

    def get_calendar(self, id_, start, end):
        """
        Obté el calendari d'un treballador.

        :param id_: ID del treballador.
        :param start: Data d'inici (format 'YYYY-MM-DD').
        :param end: Data de finalització (format 'YYYY-MM-DD').
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'workers/{}/calendar'.format(id_), params={'start': start, 'end': end})

    def set_calendar(self, id_, data):
        """
        Defineix el calendari d'un treballador.

        :param id_: ID del treballador.
        :param data: Dades del calendari (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'workers/{}/calendar'.format(id_), data=data)


