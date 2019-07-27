class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'bolt:/localhost:7687'
    DATABASE_USERNAME = 'neo4j'
    DATABASE_PASSWORD = 'local'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
