from setuptools import setup, find_packages

setup(
	name='django-mvx-geo',
	version='0.0.1',
	description='Random geo utils for Django.',
	url='https://github.com/mvx24/django-mvx-geo',
	author='mvx24',
	author_email='cram2400@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Framework :: Django',
		'License :: OSI Approved :: MIT License',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Operating System :: Unix',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 2 :: Only',
		'Topic :: Database',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	keywords='django utils views decorators geo ip geoip',
	packages=find_packages(),
	install_requires=['django']
)
