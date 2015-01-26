import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README.markdown')


setup(
    name='django-galleries',
    version='1.0.4',
    description='Simple Django galleries.',
    long_description=README,
    author='Matthew Tretter',
    author_email='m@tthewwithanm.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-imagekit>=0.3.6',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
