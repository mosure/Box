from flask_security import (
    Security,
    SQLAlchemySessionUserDatastore
)

from injector import (
    inject
)

from ..db.sql.models import (
    SQLRole,
    SQLUser
)

from ..db.sql import db

class Auth:
    @inject(app=Flask)
    def __init__(self, app: Flask):
        self.datastore = SQLAlchemySessionUserDatastore(db, SQLUser, SQLRole)
        self.security = Security(
            app=app,
            datastore=self.datastore
        )
