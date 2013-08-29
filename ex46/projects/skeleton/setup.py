try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Project',
        'author': 'Sun Mengchao',
        'url': 'github.com/smc002/',
        'download_url': 'github.com/smc002/',
        'author_email': 'sunmengchao@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname
}

setup(**config)
