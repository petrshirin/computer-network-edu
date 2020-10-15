import re
from typing import List, Dict
import socket
import sys


class InvalidFormat(Exception):
    pass


class NotFoundIpHost(Exception):
    pass


class RegisterDataDict:
    date: str
    urls: List[str]
    ips: List[str]


class Register:

    def __init__(self, file_path: str):
        self.path: str = file_path
        self.data: Dict[str, Dict] = {}
        self.read_data()

    def read_data(self):
        try:
            f = open(self.path, 'r', encoding='utf-8')
            index = 0
            for line in f.readlines():
                elements = line.split(';')
                dict_key = None
                if elements[2]:
                    dict_key = elements[2]
                else:
                    dict_key = str(index)
                    index += 1

                self.data[dict_key] = {
                    "date": elements[0],
                    "urls": [],
                    "ips": []
                }

                for url in elements[1].split(','):
                    self.data[dict_key]['urls'].append(url)
                for ip in elements[3].split(','):
                    self.data[dict_key]['ips'].append(ip)
            f.close()

        except IndexError:
            raise InvalidFormat(f'Invalid file content: {self.path}')

    @staticmethod
    def _get_host_from_url(url: str):
        try:
            result = url.split('/')
            return result[2]
        except IndexError:
            raise InvalidFormat(f"Invalid url: {url}")

    def find_by_url(self, url: str) -> bool:
        host = self._get_host_from_url(url)
        data_row = self.data.get(host)
        if data_row:
            for data_url in data_row['urls']:
                if data_url == url:
                    return True
        return False

    def find_by_host(self, url: str) -> bool:
        host = self._get_host_from_url(url)
        data_row = self.data.get(host)
        if data_row:
            return True
        return False

    def find_by_ips(self, url: str) -> bool:
        host = self._get_host_from_url(url)
        try:
            ip = socket.gethostbyname(host)
            for val in self.data.values():
                for data_ip in val['ips']:
                    if data_ip == ip:
                        return True
            return False
        except socket.gaierror:
            raise NotFoundIpHost(f'ip address for host: {host} not found')

    def full_search(self, url: str) -> bool:
        if self.find_by_host(url):
            return True
        elif self.find_by_url(url):
            return True
        elif self.find_by_ips(url):
            return True
        else:
            return False


if __name__ == '__main__':
    register = Register('register.txt')
    if register.full_search(sys.argv[1]):
        print('URL in register')
    else:
        print('URL not in register')
