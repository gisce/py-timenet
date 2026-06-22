# coding=utf-8
from __future__ import unicode_literals, absolute_import


class CustomersAPI(object):
    def __init__(self, client):
        self.client = client

    def list(self):
        """
        Obté una llista de clients.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'customers')

    def get(self, id_):
        """
        Obté informació d'un client específic.

        :param id_: ID del client.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'customers/{}'.format(id_))

    def create(self, data):
        """
        Crea un nou client.

        :param data: Dades del client (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'customers', data=data)

    def update(self, id_, data):
        """
        Actualitza un client existent.

        :param id_: ID del client.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'customers/{}'.format(id_), data=data)

    def delete(self, id_):
        """
        Elimina un client.

        :param id_: ID del client.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'customers/{}'.format(id_))

    def get_contacts(self):
        """
        Obté una llista de contactes de clients.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'customers/contacts')

    def get_contact(self, id_):
        """
        Obté informació d'un contacte de client específic.

        :param id_: ID del contacte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'customers/contacts/{}'.format(id_))

    def create_contact(self, data):
        """
        Crea un nou contacte de client.

        :param data: Dades del contacte (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'customers/contacts', data=data)

    def update_contact(self, id_, data):
        """
        Actualitza un contacte de client existent.

        :param id_: ID del contacte.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'customers/contacts/{}'.format(id_), data=data)

    def delete_contact(self, id_):
        """
        Elimina un contacte de client.

        :param id_: ID del contacte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'customers/contacts/{}'.format(id_))
