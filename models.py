from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime
)
from flask_sqlalchemy import SQLAlchemy
DB_NAME = 'agencydb'
DATABASE_NAME = 'postgresql://{}@{}:{}/{}'.format('student', 'localhost', '5432', DB_NAME)

db = SQLAlchemy()

def setup_db(app, database_path=DATABASE_NAME):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


class Show(db.Model):
    __tablename__ = 'Show'
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime, nullable=False)
    movie_id = Column(Integer, db.ForeignKey('Movie.id'), nullable=False)
    actor_id = Column(Integer, db.ForeignKey('Actor.id'), nullable=False)
    movie = db.relationship('Movie', backref=db.backref('shows', cascade='all, delete'))
    actor = db.relationship('Actor', backref=db.backref('shows', cascade='all, delete'))

    def __repr__(self):
        return f'Show -> id:{self.id}, start_time:{self.start_time}, movie_id:{self.movie_id}, actor_id:{self.actor_id}'

class Movie(db.Model):
    __tablename__ = 'Movie'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    release_date = Column(DateTime, nullable=False)

    def __repr__(self):
        return f'Movie -> id:{self.id}, title:{self.title},release_date:{self.release_date}}}'

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date 
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Actor(db.Model):
    __tablename__ = 'Actor'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    age = Column(Integer)
    gender = Column(String(1))

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender 
        }

    def __repr__(self):
        return f'Actor -> id:{self.id}, name: {self.name}, age:{self.age}, gender:{self.age}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

