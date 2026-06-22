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

    def get_lines(self):
        """
        Obté una llista de línies de projecte.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects/lines')

    def get_line(self, id_):
        """
        Obté informació d'una línia de projecte específica.

        :param id_: ID de la línia de projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects/lines/{}'.format(id_))

    def create_line(self, data):
        """
        Crea una nova línia de projecte.

        :param data: Dades de la línia (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'projects/lines', data=data)

    def update_line(self, id_, data):
        """
        Actualitza una línia de projecte existent.

        :param id_: ID de la línia de projecte.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'projects/lines/{}'.format(id_), data=data)

    def delete_line(self, id_):
        """
        Elimina una línia de projecte.

        :param id_: ID de la línia de projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'projects/lines/{}'.format(id_))

    def get_linetypes(self):
        """
        Obté una llista de tipus de línies de projecte.

        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects/linetypes')

    def get_linetype(self, id_):
        """
        Obté informació d'un tipus de línia de projecte específic.

        :param id_: ID del tipus de línia de projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('GET', 'projects/linetypes/{}'.format(id_))

    def create_linetype(self, data):
        """
        Crea un nou tipus de línia de projecte.

        :param data: Dades del tipus de línia (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'projects/linetypes', data=data)

    def update_linetype(self, id_, data):
        """
        Actualitza un tipus de línia de projecte existent.

        :param id_: ID del tipus de línia de projecte.
        :param data: Dades actualitzades (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('PUT', 'projects/linetypes/{}'.format(id_), data=data)

    def delete_linetype(self, id_):
        """
        Elimina un tipus de línia de projecte.

        :param id_: ID del tipus de línia de projecte.
        :return: Resposta JSON de l'API.
        """
        return self.client.request('DELETE', 'projects/linetypes/{}'.format(id_))
