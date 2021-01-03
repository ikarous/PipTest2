#setup.py

from setuptools import setup


setup(
      name='piptest2',
      version='0.1',
      description='piptest2',
      license='MIT',
      url='https://github.com/ikarous/piptest2/',
      author='William Norris',
      author_email='ike.norris@gmail.com',
      license='MIT',
      packages=['piptest1'],
      zip_safe=False,
      python_requires='>=3.6'
)