from flask import Flask

from injector import (
    Module,
    singleton,
    provider
)

from .auth import Auth

class AuthModule(Module):
    """Handle auth"""

    @singleton
    @provider(Auth)
    def provide_auth(self):
        return Auth()
