import os

# globals
WTF_CSRF_ENABLED = True
SECRET_KEY = '^&H2i@Wtq&9pd8pa6#EtUheKvENfS2'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'bushings.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# end
