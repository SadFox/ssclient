import types
from typing import Any, Dict, Optional

from ssclient.client import SSClient
from ssclient.http_client import HttpClient


class SSClientFactory:
    HOSTS_MAP = types.MappingProxyType({
        '02': 'https://api.serverspace.by',
        '04': 'https://api.serverspace.io',
        '06': 'https://api.serverspace.ru',
        '07': 'https://api.lincore.kz',
        '08': 'https://api.serverspace.us',
        '09': 'https://api.serverspace.com.tr',
        '0a': 'https://api.serverspace.in',
        '0f': 'https://api.itglobal.com',
        '14': 'https://api.serverspace.kz',
        '20': 'https://api.cloudtek.kz',
        '21': 'https://api.serverspace.ca',
        '22': 'https://api.serverspace.com.br',
        '23': 'https://api.falconcloud.ae',
        '25': 'https://api.vc.miran.ru',
        '26': 'https://api.ekacod.ru',
        '28': 'https://api.glos.online',
        '29': 'https://api.vcloud-test.uzum.io',
    })

    @staticmethod
    def get_host_by_apikey(apikey: str) -> Optional[str]:
        partner_code = apikey[:2].lower()
        return SSClientFactory.HOSTS_MAP.get(partner_code)

    @staticmethod
    def create(apikey: str) -> SSClient:
        host = SSClientFactory.get_host_by_apikey(apikey)
        return SSClient(HttpClient(host, apikey))
