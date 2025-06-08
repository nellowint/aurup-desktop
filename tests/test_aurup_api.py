from services.aurup_api import AurupAPI

api = AurupAPI()
packages = [
    'google-chrome',
    'sublime-text-4',
    'android-studio'
]

def test_search_package():
    for index in range(len(packages)):
        assert api.search_package(packages[index])

def test_search_packages():
    assert api.search_packages(packages)
