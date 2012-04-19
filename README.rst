django-cms-wunderground
=================
An extension for Django CMS that pulls current weather information
based on the website visitor's IP address and displays it on the 
screen.  You will need a www.wunderground.com API key to use this.

Dependancies
============

- django (tested with 1.3)
- django-cms (tested with 2.2)

Getting Started
=============

To get started simply install using ``pip``:
::
    pip install django-cms-wungerground

Add ``cmsplugin_wunderground`` to your installed apps.

Add WUNDERGROUND_KEY to your settings file.  
::
    WUNDERGROUND_KEY = 'abcdefgh12345678'
	
Usage
=============

Simply drop a Current Local Weather plugin on a page.  You will probably
want to override the ``cmsplugin_wunderground/local_weather.html`` 
template.  Any of the fields from the wunderground.com "conditions" api
call should be available in the template under the context variable 
``weather_info``.
