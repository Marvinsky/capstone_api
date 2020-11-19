from flask_mongoalchemy import MongoAlchemy
import datetime

DB_NAME = 'agencydb'

db = MongoAlchemy()

def setup_db(app, database_name=DB_NAME):
    app.config['MONGOALCHEMY_SERVER'] = "localhost"
    app.config['MONGOALCHEMY_PORT'] = 27017
    app.config['MONGOALCHEMY_USER'] = None
    app.config['MONGOALCHEMY_PASSWORD'] = None
    app.config['MONGOALCHEMY_DATABASE'] = DB_NAME

    db.app = app
    db.init_app(app)


class Show(db.Document):
    start_time = db.DateTimeField(required=True, default=datetime.datetime.now())

class Movie(db.Document):
    title = db.StringField()
    release_date = db.DateTimeField(required=True, default=datetime.datetime.now())

class Actor(db.Document):
    name = db.StringField()
    age = db.IntField()
    gender = db.StringField()

