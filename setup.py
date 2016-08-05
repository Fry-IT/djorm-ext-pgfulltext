from setuptools import find_packages
from setuptools import setup


setup(
    name="djorm-ext-pgfulltext",
    version='0.9.3-1-fry',
    packages=find_packages(),
    pbr=True,
    setup_requires=['pbr'],
)
