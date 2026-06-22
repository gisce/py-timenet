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

    def get_checkpoint(self, id_):
        """
        Obté informació d'un checkpoint específic.

        :param id_: ID del checkpoint.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/checkpoints/{}'.format(id_))

    def create_checkpoint(self, data):
        """
        Crea un nou checkpoint.

        :param data: Dades del checkpoint (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'config/checkpoints', data=data)

    def update_checkpoint(self, id_, data):
        """
        Actualitza un checkpoint existent.

        :param id_: ID del checkpoint.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'config/checkpoints/{}'.format(id_), data=data)

    def delete_checkpoint(self, id_):
        """
        Elimina un checkpoint.

        :param id_: ID del checkpoint.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'config/checkpoints/{}'.format(id_))

    def get_checktypes(self):
        """
        Obté una llista de tipus de check.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/checktypes')

    def get_checktype(self, id_):
        """
        Obté informació d'un tipus de check específic.

        :param id_: ID del tipus de check.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'config/checktypes/{}'.format(id_))

    def create_checktype(self, data):
        """
        Crea un nou tipus de check.

        :param data: Dades del tipus de check (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'config/checktypes', data=data)

    def update_checktype(self, id_, data):
        """
        Actualitza un tipus de check existent.

        :param id_: ID del tipus de check.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'config/checktypes/{}'.format(id_), data=data)

    def delete_checktype(self, id_):
        """
        Elimina un tipus de check.

        :param id_: ID del tipus de check.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'config/checktypes/{}'.format(id_))

    def get_calendar(self, start, end):
        """
        Obté el calendari general de l'empresa.

        :param start: Data d'inici (format 'YYYY-MM-DD').
        :param end: Data de finalització (format 'YYYY-MM-DD').
        :return: Resposta JSON de l'API.
        """
        return self.client.request(
            'GET',
            'config/calendar',
            params={'start': start, 'end': end},
        )

    def set_calendar(self, data):
        """
        Defineix el calendari general de l'empresa.

        :param data: Dades del calendari (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'config/calendar', data=data)
