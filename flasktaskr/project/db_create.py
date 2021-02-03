# project/db_create.py

from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()

# insert data
db.session.add(Task("Train People to like working for you", date(2021, 2, 2), 10, 1))
db.session.add(Task("God Bless our homeland", date(2021, 2, 2), 10, 1))

# commit the changes
db.session.commit()
