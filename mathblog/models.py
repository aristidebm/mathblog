from datetime import datetime

from flask_login import UserMixin
from mathblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # metadata
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(65), unique=True)
    email = db.Column(db.String(225), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(255), nullable=True)
    # [baref="author"] let we access author of a question instance.
    questions = db.relationship("Question", backref="author", lazy=True)
    answers = db.relationship("Answer", backref="author", lazy=True)

    def __repr__(self) -> str:
        return "User<{self.username}>".format(self=self)


class Question(db.Model):
    # metadata
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)  # don't allow post without content
    # Something like the domain of math in that the question can be classified
    # it is readonly field that must be deduced automatically just after the question
    # is post.
    topic = db.Column(db.String(50), nullable=False)
    # ( lazy=True ) make object available on demand.
    answers = db.relationship("Answer", backref="question", lazy=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified_at = db.Column(
        db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self):
        return "Post<{self.title}>".format(self=self)


class Answer(db.Model):
    __tablename__ = "answers"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    is_voted = db.Column(db.Boolean, default=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modified_at = db.Column(
        db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self):
        return "Post<{self.title}>".format(self=self)
