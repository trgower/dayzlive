import os
basedir = os.path.abspath(os.path.dirname(__file__))
#mysql+pymysql://dayzliveweb:XuytQuwk3-Cifo@localhost/dayzlist?unix_socket=/var/run/mysqld/mysqld.sock
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://tanner:Gomwer5676567``@localhost:3306/dayzlist'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'CehiZiyeRufp4]'
