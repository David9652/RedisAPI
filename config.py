class Config(object):
    """ Used to set up main environment settings """
    DEBUG = False # Whether debug mode is enabled
    TESTING = False # Enable testing mode. Exceptions are propagated rather than handled by the the app’s error handlers
    TRAP_HTTP_EXCEPTIONS=False # If there is no handler for an HTTPException-type exception, re-raise it to be handled by the interactive debugger instead of returning it as a simple error response

class ProductionConfig(Config):
    """ Used to set up production environment settings """
    pass

class DevelopmentConfig(Config):
    """ Used to set up development environment settings """
    DEBUG = True

class TestingConfig(Config):
    """ Used to set up unit and integration testing """
    DEBUG = True
    TESTING = True