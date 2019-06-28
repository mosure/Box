import os

from injector import Module, provides, singleton


class ConfigurationModule(Module):
    @singleton
    @provides(Configuration)
    def provide_configuration(self):
        return Configuration()

class Configuration():
    def __init__(self):
        self.database = os.getenv('DATABASE', 'sql')
        self.database_uri = os.getenv('DATABASE_URI', 'sqlite:///:memory:')
