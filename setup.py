""" setup.py """
import os
import sys
from setuptools import setup, find_packages
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

def get_description():
    """ Makes README file into a string"""
    with open("README.rst") as file:
        long_description = file.read()
    return long_description

def get_reqs():
    """ Parses `requirements.txt` for dependencies"""
    parsed_reqs = parse_requirements("requirements/base.txt", session=False)
    reqs = [str(ir.req) for ir in parsed_reqs]
    return reqs

def get_version():
    """ Gets version from diehard.__init__.py

    Runs `diehard.__init__` and loads defined variables into scope
    """
    with open(os.path.join('diehard', '__init__.py')) as version_file:
        # pylint: disable=exec-used, undefined-variable
        exec(version_file.read(), globals())
        return __version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

setup(
    name='diehard',
    author='Elton Law',
    author_email='eltonlaw296@gmail.com',
    version=get_version(),
    url="http://diehard.readthedocs.io/en/latest/",
    download_url='https://github.com/eltonlaw/diehard',
    description='Tests for randomness.',
    long_description=get_description(),
    packages=find_packages(exclude=['docs']),
    install_requires=get_reqs(),
    keywords=["RNG", "tests"],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering'],
    extras_require={
        'dev': ['pylint', 'sphinx'],
        'test': ['pytest'],
    },
    license='Apache License 2.0'
)
