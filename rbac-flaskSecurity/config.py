class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'
    SECURITY_PASSWORD_SALT = 'salty'
    WTF_CSRF_ENABLED = False