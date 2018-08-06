from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from README.md --> rst
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'plover-phenrsteno',
    version = '0.1.7',
    author = 'Gregory Chamberlain',
    author_email = '15685804+contrum@users.noreply.github.com',
    description = 'Phonemic non-rhotic English stenotype system for Plover',
    long_description = long_description,
    license = 'GNU General Public License v2 or later (GPLv2+)',
    long_description_content_type = 'text/markdown',
    keywords = 'plover plover_plugin',
    url = 'https://github.com/contrum/phenrsteno',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
    ],
    install_requires =[
        'plover>=4.0.0.dev0',
    ],
    py_modules = [
        'plover_phenr',
    ],
    entry_points = '''

[plover.system]
Phenrsteno = plover_phenr

''',
    zip_safe = True,
)
