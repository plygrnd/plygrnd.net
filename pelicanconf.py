#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Dan Urson"
SITENAME = "Dan Urson's Blog"
SITETITLE = "Dan Urson"
SITESUBTITLE = "Gentleman Engineer"
SITELOGO = "/images/profile.jpg"
FAVICON = "/images/favicon.ico"
SITEURL = "https://plygrnd.net"

STATIC_PATHS = ['images']

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

MAIN_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./themes/Flex"

# Blogroll
"""
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)
"""
# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/durson'),
          ('github', 'https://www.github.com/plygrnd'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = '2018'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
