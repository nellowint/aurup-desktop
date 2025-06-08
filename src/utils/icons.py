import os

class Icons:
    def __init__(self, path):
        self.icons = os.listdir(path)
    
    def _search_icon(self, name):
        for icon in self.icons:
            if f'{name}.svg'.lower() in icon.lower():
                return icon

    def get_icon(self, name):
        icon = self._search_icon(name)
        if icon is None:
            return f'applications-python.svg'
        return icon