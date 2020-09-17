#!/usr/bin/env python
import plynx
from setuptools import setup, find_packages

install_requires = [
]

setup(
    name='plynx_deploy',
    version=plynx.__version__,
    description='Specific plug-ins for Plynx',
    url='https://plynx.com',
    author='Ivan Khomyakov',
    author_email='ivan@plynx.com',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Environment :: Console',
        'Environment :: Web Environment',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: POSIX',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',

        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords='data science, machine learning, pipeline, workflow, experiments',
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={},
    package_data={},
    project_urls={
        'Demo': 'https://plynx.com',
        'Source': 'https://github.com/plynx-team/plynx',
    },
    zip_safe=False,
)
