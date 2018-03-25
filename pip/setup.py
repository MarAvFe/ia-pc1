
from setuptools import setup, find_packages

setup(name='tec',
      version='0.1',
      description='Proyecto Corto 1 - IA',
      url='https://github.com/MarAvFe/ia-pc1/',
      author='Grupo 04 IA',
      author_email='sfalconc@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      package_data={'': ['*.csv']},
      zip_safe=False,
      )

