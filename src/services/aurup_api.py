import requests


class AurupAPI:
    def __init__(self):
        self._packages: list[Package] = list()
        self._base_url = 'https://aur.archlinux.org/rpc/v5'

    def search(self, name: str, searching: bool):
        name = name.replace(' ', '-')
        response = (
            requests.get(f'{self._base_url}/search/{name}?by=name')
            if searching
            else requests.get(f'{self._base_url}/info/{name}')
        )

        if response:
            return response.json().get('results')
        else:
            return None
