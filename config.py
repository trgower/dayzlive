import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dayzliveweb:XuytQuwk3-Cifo@localhost/dayzlist?unix_socket=/var/run/mysqld/mysqld.sock'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'CehiZiyeRufp4]'
