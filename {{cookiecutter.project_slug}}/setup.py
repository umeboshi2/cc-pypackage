#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    {%- if cookiecutter.command_line_interface|lower == 'click' %}
    'Click>=6.0',
    {%- endif %}
    # TODO: put package requirements here
    'plaster_pastedeploy',
    'pyramid >= 1.9a',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',
    'pytest-cov',
]

setup_requirements = [
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest-runner',
{%- endif %}
    # TODO({{ cookiecutter.github_username }}): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'WebTest >= 1.3.1',  # py3 compat
{%- if cookiecutter.use_pytest == 'y' %}
    'pytest',
    'pytest-cov',
{%- endif %}
    # TODO: put package test requirements here
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'UNLICENSED': 'License :: Public Domain'
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    entry_points={
        'paste.app_factory': [
            'main = {{ cookiecutter.project_slug }}:main',
        ],
        'console_scripts': [
            'initialize_{{ cookiecutter.project_slug }}_db = {{ cookiecutter.project_slug }}.scripts.initializedb:main',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='{{ cookiecutter.project_slug }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
