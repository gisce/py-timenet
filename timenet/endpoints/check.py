# coding=utf-8
from __future__ import unicode_literals, absolute_import

class CheckAPI(object):
    def __init__(self, client):
        self.client = client

    def list(self, start, end, worker=None, checkpoint=None):
        """
        Obté una llista de registres de checks.

        :param start: Data d'inici (format 'YYYY-MM-DD').
        :param end: Data de finalització (format 'YYYY-MM-DD').
        :param worker: ID del treballador (opcional).
        :param checkpoint: ID del checkpoint (opcional).
        :return: Resposta JSON de l'API.
        """
        params = {'start': start, 'end': end}
        if worker:
            params['worker'] = worker
        if checkpoint:
            params['checkpoint'] = checkpoint
        return self.client.request('GET', 'check', params=params)

    def by_pin(self, data):
        """
        Registra un check utilitzant un PIN.

        :param data: Dades del check (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'check/bypin', data=data)

    def by_worker(self, data):
        """
        Registra un check per a un treballador específic.

        :param data: Dades del check (diccionari).
        :return: Resposta JSON de l'API.
        """
        return self.client.request('POST', 'check/byworker', data=data)

    def status_by_day(self, start, end, worker=None, mode=None):
        """
        Obté l'estat dels checks per dia.

        :param start: Data d'inici (format 'YYYY-MM-DD').
        :param end: Data de finalització (format 'YYYY-MM-DD').
        :param worker: ID del treballador (opcional).
        :param mode: Mode de consulta (opcional).
        :return: Resposta JSON de l'API.
        """
        params = {'start': start, 'end': end}
        if worker:
            params['worker'] = worker
        if mode:
            params['mode'] = mode
        return self.client.request('GET', 'check/status/byday', params=params)


