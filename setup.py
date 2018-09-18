from os import path
from codecs import open
from setuptools import setup, find_packages
from pypandoc import convert_text

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    # Get the long description from README.md
    readme_md = f.read()
    # Convert to reStructuredText using pypandoc
    readme_rst = convert_text(readme_md, 'rst', format='markdown').replace('\r', '')


setup(
    name = 'plover-phenrsteno',
    version = '0.2.3',
    author = 'Gregory Chamberlain',
    author_email = '15685804+contrum@users.noreply.github.com',
    description = 'Phonemic non-rhotic English stenotype system for Plover',
    long_description = readme_rst,
    long_description_content_type = 'text/x-rst',
    license = 'GNU General Public License v2 or later (GPLv2+)',
    keywords = 'plover plover_plugin',
    url = 'https://github.com/contrum/plover-phenrsteno',
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
        'plover_phenrsteno',
    ],
    entry_points = '\n\n[plover.system]\nPhenrsteno = plover_phenrsteno\n\n',
    zip_safe = True
)
