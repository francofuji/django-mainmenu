import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-mainmenu",
    version = "0.1.0",
    description = "django pluggable application for make dynamic the main menu of web apps",
    long_description = read('README.rst'),
    url = 'https://github.com/francofuji/django-mainmenu',
    author = 'Francisco Pérez Ferrer',
    author_email = 'francofuji@gmail.com',
    packages = find_packages(exclude=['tests', 'example', 'docs']),
    install_requires = ['django'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
