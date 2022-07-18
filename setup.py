#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', "PyQt5>=5.15.7"]

test_requirements = ['pytest>=3']

setup(
    author="Md Ashraful Islam",
    author_email='imdashraful17@gmail.com',
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
    description="Magically turn your CLI into a GUI program and make it more user friendly.",
    entry_points={
        'console_scripts': [
            'guiprint=guiprint.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='guiprint',
    name='guiprint',
    packages=find_packages(include=['guiprint', 'guiprint.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ashrafulislambd/guiprint',
    version='1.0.4',
    zip_safe=False,
)
