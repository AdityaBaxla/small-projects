from model import db, User, Role
from flask_security import SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db, User, Role)