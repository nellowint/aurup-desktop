class Package:
    def __init__(
        self,
        name,
        description='',
        url_path='',
        version='',
        icon=None,
        local_version=None,
    ):
        self.name = name
        self.description = description
        self.url_path = url_path
        self.version = version
        self.icon = icon
        self.local_version = local_version

    def __str__(self):
        return f'{self.name}\n{self.description}\n{self.url_path}\n{self.version}\n{self.local_version}\n'
