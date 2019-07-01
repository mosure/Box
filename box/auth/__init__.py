from flask import Flask

from injector import (
    Module,
    singleton
)

from .auth import Auth

class AuthModule(Module):
    """Handle auth"""

    @singleton
    @provides(Auth)
    def provide_auth(self):
        return Auth()
