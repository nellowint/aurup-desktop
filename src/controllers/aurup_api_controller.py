import os
from models.package import Package
from services.aurup_api import AurupAPI
from utils.directory import ProgramDirectory
from utils.icons import Icons

class AurupAPIController:
    def __init__(self, icons: Icons):
        self._icons = icons
        self._api = AurupAPI()
        self._directory = ProgramDirectory()
        self.packages: list[Package] = list()

    def search_packages(self, name: str, searching: bool, local_version=None):
        response = self._api.search(name=name, searching=searching)
        if response:
            for index in range(len(response)):
                package = Package(
                    name=response[index]['Name'],
                    description=response[index]['Description'],
                    url_path=response[index]['URLPath'],
                    version=response[index]['Version'],
                    local_version=local_version
                )
                package.icon = self._icons.get_icon(package.name)
                self.packages.append(package)
        else:
            return None

    def load_packages(self):
        os.system(f'pacman -Qm > {self._directory.local_packages}')
        with open(f'{self._directory.local_packages}') as file:
            for line in file:
                packages_split = line.split()
                name = packages_split[0]
                version = packages_split[1]
                package = Package(
                    name=name,
                    local_version=version,
                )
                self.search_packages(
                    name=package.name,
                    searching=False,
                    local_version=package.local_version
                )
        file.close()