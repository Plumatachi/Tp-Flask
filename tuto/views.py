from tuto.app import app, db
from tuto.models import get_sample, get_author, get_book, get_books_by_author, Author, Book, User
from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField, FloatField
from wtforms.validators import DataRequired
import click
import yaml
from hashlib import sha256
from flask_login import login_user, current_user, logout_user, login_required
from flask import request

class AuthorForm(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom', validators=[DataRequired()])

class BookForm(FlaskForm):
    id = HiddenField('id')
    title = StringField('Titre', validators=[DataRequired()])
    price = FloatField('Prix', validators=[DataRequired()])
    img = StringField('Image')
    url = StringField('Url')
    author = StringField('Author')

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    next = HiddenField()

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

@app.route("/edit/author/<int:id>")
@login_required
def edit_author(id):
    a = get_author(id)
    f = AuthorForm(id=a.id, name=a.name)
    return render_template("edit_author.html", author=a, form=f)

@app.route("/save/author/", methods=("POST",))
def save_author():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        idd = int(f.id.data)
        a = get_author(idd)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('author', id=a.id))
    a = get_author(int(f.id.data))
    return render_template("edit_author.html", author=a, form=f)

@app.route("/add/author/")
def add_author():
    a = None
    f = AuthorForm()
    return render_template("add_author.html", author=a, form=f)

@app.route("/add/author/", methods=("POST",))
def add_author_succeed():
    a = None
    f = AuthorForm()
    if f.validate_on_submit():
        author_name = f.name.data
        existing_author = Author.query.filter_by(name=author_name).first()
        if existing_author:
            a = existing_author
        else:
            new_author = Author(name=author_name)
            db.session.add(new_author)
            db.session.commit()
            a = new_author
        return redirect(url_for('author', id=a.id))
    return render_template("add_author.html", author=a, form=f)

@app.route("/add/book")
def add_book():
    b = None
    f = BookForm()
    return render_template("add_book.html", book=b, form=f)

@app.route("/add/book", methods=('POST',))
def add_book_succeed():
    b = None
    f = BookForm()
    if f.validate_on_submit():
        title = f.title.data
        existing_book = Book.query.filter_by(title=title).first()
        if existing_book is None:
            author_name = f.author.data
            existing_author = Author.query.filter_by(name=author_name).first()
            if existing_author is None:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()
                author = new_author
            else:
                author = existing_author
            new_book = Book(title=title, price=f.price.data, img=f.img.data, url=f.url.data, author=author)
            db.session.add(new_book)
            db.session.commit()
            b = new_book
        else:
            b = existing_book
        return redirect(url_for('book', id=b.id))
    return render_template("add_book.html", book=b, form=f)

@app.route("/detail/author/<int:id>")
def author(id):
    a = get_author(id)
    list_books = get_books_by_author(a)
    return render_template("author.html", author_name=a.name, author_id = a.id, books=list_books)

@app.route("/detail/book/<int:id>")
def book(id):
    b = get_book(id)
    return render_template("book.html", book=b, author=b.author)

@app.route("/")
def home():
    return render_template("home.html", title="My Books!", books=get_sample())

@app.route("/login/", methods=("GET", "POST",))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data or url_for('home')
            return redirect(next)
    return render_template("login.html", form=f)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))
