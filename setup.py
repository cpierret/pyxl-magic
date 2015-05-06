#!/usr/bin/env python

from distutils.core import setup


PROJECT = 'pyxl-magic'
VERSION = '0.1'
AUTHOR = 'Christophe Pierret'
AUTHOR_EMAIL = 'cpierret@gmail.com'
DESC = "Excel file type identification. Improved detection compared to libmagic or python-magic."

setup(
	name=PROJECT,
	version=VERSION,
	description=DESC,
	long_description="""Python module to check if a file is an Excel file.  
Less false positive or false negative compared to libmagic or python-magic.
Pure python. No need for external library like libmagic, works on Windows as is.
	"""
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	url="http://github.com/cpierret/pyxl-magic",
	py_modules=['magic'],
	keywords="mime magic file excel xls xlsx",
	license="MIT",
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Development Status :: 4 - Beta',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
	],
)
