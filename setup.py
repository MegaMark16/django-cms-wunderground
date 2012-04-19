from setuptools import setup, find_packages
import os

version = __import__('cmsplugin_wunderground').__version__

install_requires = [
    'setuptools',
    'django',
    'django-cms',
]

setup(
    name = "django-cms-wunderground",
    version = version,
    url = 'http://github.com/megamark16/django-cms-wunderground',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "An extension for Django CMS that displays the current local weather pulled from  wunderground.com",
    author = "Mark Ransom",
    author_email = 'megamark16@gmail.com',
    packages=find_packages(),
    install_requires = install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'cmsplugin_wunderground': 'cmsplugin_wunderground',
    },
)
