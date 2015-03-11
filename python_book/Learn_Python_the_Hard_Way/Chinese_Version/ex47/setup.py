try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My test project.',
    'author: Shuailong Wang',
    'url': 'Url can get my information',
    'download_url': 'Where it can be downloaded.'.
    'email': 'oopswangsl@gmail.com',
    'version': '0.1',
    'install_required': ['Nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}


setup(**config)
