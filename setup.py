#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', "hypothesis"]

setup(
    author="Ivar Grytten",
    author_email='name@domain.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="..",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='copilot_testproject',
    name='copilot_testproject',
    packages=find_packages(include=['copilot_testproject', 'copilot_testproject.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivargr/copilot_testproject',
    version='0.0.1',
    zip_safe=False,
)
