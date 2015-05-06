#!/usr/bin/env python

from distutils.core import setup

setup(
	name='pyxl-magic',
	version='0.1',
	description="Excel file type identification. Improved detection compared to libmagic or python-magic.",
	long_description="""Python module to check if a file is an Excel file.  
Less false positive or false negative compared to libmagic or python-magic.
Pure python. No need for external library like libmagic, works on Windows as is.
	""",
	author='Christophe Pierret',
	author_email='cpierret@gmail.com',
	url="http://github.com/cpierret/pyxl-magic",
	py_modules=['pyxl-magic'],
	keywords="mime magic file excel xls xlsx",
	license='Apache License 2.0',
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: Apache Software License',
		'Development Status :: 4 - Beta',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
	],
)
