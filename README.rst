Pony Pusher
===========

Thin wrapper for python pusher library allows you to send ad-hocs events or
Django model fields to Pusher app.

Installation
------------
::

	python setup.py install

Configuration
-------------
Add the following entries to your Django projects settings.py 

::

	PUSHER_APP_ID = 'YOUR_PUSHER_APP_ID'
	PUSHER_KEY = 'YOUR_PUSHER_KEY'
	PUSHER_SECRET = 'YOUR_PUSHER_SECRET'

Usage
-----
From you project's django shell

::

	>>> from ponypusher.ponypusher import PushMe
	>>> help(PushMe)

