from main import app, user_datastore
from flask_security import hash_password
from model import db

with app.app_context():
    # add database 
    db.create_all()

    # Ensure roles exist
    admin_role = user_datastore.find_or_create_role(name='admin', description='this is admin role')
    student_role = user_datastore.find_or_create_role(name='student', description='this is student role')

    # Create users
    user1 = user_datastore.create_user(
        username="user1",
        password=hash_password('pass1'),
        email="user1@gmail.com",
    )
    if student_role not in user1.roles:
        user_datastore.add_role_to_user(user1, student_role)

    admin = user_datastore.create_user(
        username="admin",
        password=hash_password('pass1'),
        email="admin@gmail.com",
    )
    if admin_role not in admin.roles:
        user_datastore.add_role_to_user(admin, admin_role)

    db.session.commit()
