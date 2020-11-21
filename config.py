
class Config():
    DEBUG = False
    TESTING = False

    SECRET_KEY = '\x10\xca\xad\xb3Y\x83\x81\x1e]\xf4'

    DB_NAME = 'production-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True

    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    TESTING = True

    DB_NAME = 'development-db'
    DB_USERNAME = 'root'
    DB_PASSWORD = 'example'

    SESSION_COOKIE_SECURE = True
