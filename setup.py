"""
Flask-Mako
----------

Adds Mako support to Flask applications.

Links
`````

* `development version
<http://github.com/tzellman/flask-mako/zipball/master#egg=Flask-Mako-dev>`_

.. _Mako: http://www.makotemplates.org/

"""
from setuptools import setup


setup(
    name='Flask-Mako',
    version='0.1',
    url='http://github.com/tzellman/flask-mako',
    license='BSD',
    author='Tom Zellman',
    author_email='tzellman@forthought.net',
    description='Adds Mako support to Flask applications',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Mako'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

