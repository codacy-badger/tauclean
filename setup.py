from setuptools import setup
import sys


def get_version():
    """Get the version number of tauclean"""
    import tauclean
    return tauclean.__version__


reqs = ['numpy>=1.16.2', 'matplotlib>=3.0.3', 'scipy>=1.2.1']

if sys.version_info < (3, 5):
    sys.exit('tauclean requires Python 3.5+')

setup(
    name='tauclean',
    version=get_version(),
    url='https://github.com/bwmeyers/tauclean',
    author='Bradley Meyers',
    author_email='bradley.meyers1993@gmail.com',
    description='A package to deconvolve scattered pulsar profiles',
    install_requires=reqs,
    packages=['tauclean'],
    scripts=['scripts/tauclean', 'scripts/simulate'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'nose']
)