try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'discription': 'My Project',
	'author': 'Anke Ge',
	'url':'URL',
	'download_url':'download_url',
	'author_email':'email',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name': 'projectname'
	}

setup(**config)

