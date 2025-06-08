import os

class ProgramDirectory():
    def __init__(self):
        self.__home_dir = os.path.expanduser('~')
        self.__base_dir = os.path.join(self.__home_dir, '.aurup')
        self.__temp_dir = f'{self.__base_dir}/tmp'
        self.local_packages=f'{self.__base_dir}/local_packages.txt'
        self.repo_packages=f'{self.__base_dir}/repo_packages.txt'
        self.__initialize()

    def __initialize(self):

        try:
            os.makedirs(self.__base_dir)
            os.makedirs(self.__temp_dir)
            print(f'Directory {self.__base_dir} created successfully.')
            print(f'Directory {self.__temp_dir} created successfully.')
        except FileExistsError:
            print(f'Directory {self.__base_dir} already exist.')
            print(f'Directory {self.__temp_dir} already exist.')
        except PermissionError:
            print(f'Permission denied to create: {self.__base_dir}')
            print(f'Permission denied to create: {self.__temp_dir}')
        except Exception as e:
            print(f'Erro: {e}')