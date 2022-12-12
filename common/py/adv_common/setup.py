import sys
from setuptools import setup, find_packages

setup(
	name='adv_common',
	version='0.1.0',
	author='Hector Bravo',
	author_email='hbravo@cuic.net',
	url='https://github.com/HectorBravo/adventofcode',
	packages=find_packages(),
	license='LICENSE.txt',
	description='Common code for https://adventofcode.com',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	install_requires=[],
	python_requires='>=3.11'
)