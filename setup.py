from setuptools import setup
setup(
    name = 'dtest',
    version = '0.1.0',
    packages = ['dtest'],
    entry_points = {
        'console_scripts': [
            'dtest = dtest.__main__:main'
        ]
    })