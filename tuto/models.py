import yaml, os.path
from tuto.app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username

class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    img = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author",
                             backref=db.backref("books", lazy="dynamic"))

    def __repr__(self):
        return "<Book (%d) %s>" % (self.id, self.title)

Books = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), "../data.yml")))

# Pour avoir un id
i = 0
for book in Books:
    book['id'] = i
    i += 1

def get_sample():
    return Book.query.limit(10).all()

def get_book(id):
    list_books = Book.query.all()
    for book in list_books:
        if book.id == id:
            return book

def get_author(id):
    list_authors = Author.query.all()
    for author in list_authors:
        if author.id == id:
            return author


def get_books_by_author(author):
    list_books_author = list()
    list_books = Book.query.all()
    for book in list_books:
        if book.author == author:
            list_books_author.append(book)
    return list_books_author

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
