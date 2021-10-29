"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
#long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='adi_env_parser',
    version='0.0.1a',
    description='Adinsure Environment parser',
    #long_description=long_description,
    #long_description_content_type='text/markdown',
    packages=find_packages(exclude=["tests"]),
    python_requires='>=3.8, <4',
    install_requires=[],
    extras_require={
        'dev': [
            'pre-commit',
            'autopep8'
            'pytest'
        ],
        'test': [
            'pytest'
            ],
    },
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)