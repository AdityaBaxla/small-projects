from flask import Flask
from flask_security import Security, auth_required, roles_required, roles_accepted
from model import db
from config import DevConfig
from auth import user_datastore

app = Flask(__name__)

app.config.from_object(DevConfig)
db.init_app(app)
app.security = Security(app, user_datastore)


@app.route('/')
def home():
    return "this is home"

@app.route('/user')
@auth_required("token")
@roles_accepted('student', 'admin')
def user():
    return "this is student"

@app.route('/admin')
@roles_required('admin')
def admin():
    return "this is admin page"
if (__name__ == "__main__"):
    app.run(debug=True)  