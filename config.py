# _*_ coding: utf-8 _*_
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = False
HOST = '0.0.0.0'
PORT = 5001
CSRF_ENABLED = True
SECRET_KEY = 'goodgoodstudydaydayup'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'}
]
MAIL_SERVER = 'smtp.126.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'kengrary@126.com'
MAIL_PASSWORD = '126mail@000181'

ADMINS = ['kengrary@126.com']

POSTS_PER_PAGE = 3

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

LANGUAGES = {
    'en': 'English',
    'zh': 'Chinese'
}