# -*- coding: utf8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

WHOOSH_ENABLED = os.environ.get('HEROKU') is None

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
    
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '../../../../Downloads/microblog-0.14/db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# email server
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'you'
MAIL_PASSWORD = 'your-password'

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

SQLALCHEMY_RECORD_QUERIES = True

# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

WHOOSH_ENABLED = os.environ.get('HEROKU') is None
