"""
Flask-Restafarian
-------------

Flask compliant restful library
"""
from setuptools import setup


setup(
    name='Flask-Restafarian',
    version='0.0.1',
    url='http://github.com/erwagasore/flask_restafarian/',
    license='BSD-2-Clause',
    author='Eugene Rwagasore',
    author_email='rwagasore@gmail.com',
    description='Flask compliant restful library',
    long_description=__doc__,
    py_modules=['flask_restafarian'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
