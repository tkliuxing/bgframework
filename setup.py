from setuptools import setup, find_packages
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from bgframework import __version__
# from Cython.Build import cythonize

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    'Topic :: Internet :: WWW/HTTP :: Site Management',
    'Programming Language :: Python :: 3.4',
]

config = {
    'name': 'bgframework',
    'description': 'Django background management full-stack framework',
    'long_description': "Django background management full-stack framework",
    'url': 'https://github.com/tkliuxing/bgframework',
    'author': 'Ronald White',
    'author_email': 'ouyanghongyu@gmail.com',
    'license': 'MIT License',
    'version': __version__,
    'install_requires': [
        'django-braces',
        'django-sekizai',
        'django-bootstrap-form-tkliuxing',
        'six==1.10.0',
    ],
    'setup_requires': [
        'setuptools_scm'
    ],
    'package_dir': {'': 'src'},
    'packages': find_packages("src"),
    'include_package_data': True,
    'platforms': ['OS Independent'],
    'scripts': [],
    'zip_safe': False,
    'classifiers': CLASSIFIERS,
    # 'ext_modules': cythonize([Extension("helloworld", ["helloworld.pyx"]),]),
}

setup(**config)
