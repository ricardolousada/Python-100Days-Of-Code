from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TelField, FloatField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
Bootstrap5(app)
##CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# Create the extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


class BookForm(FlaskForm):
    book_name = StringField(label="Book Name", validators=[DataRequired()])
    book_author = StringField(label="Book Author", validators=[DataRequired()])
    rating = StringField(label="Rating", validators=[DataRequired()])
    button = SubmitField(label="Add Book")


class ChangeRatingForm(FlaskForm):
    new_rating = FloatField(label="", validators=[DataRequired()])
    button = SubmitField(label="Change Rating")


@app.route('/')
def home():
    empty_lib = False
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    if not all_books:
        empty_lib = True
    return render_template('index.html', books=all_books, empty_lib=empty_lib)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        book_title = form.book_name.data
        book_author = form.book_author.data
        rating = form.rating.data
        new_book = Book(title=book_title, author=book_author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/edit", methods=["GET", "POST"])
def change_rating():
    change_form = ChangeRatingForm()
    book_id = request.values.get('id')
    if change_form.validate_on_submit():
        print("entrei no on-submit")
        book_to_update = db.get_or_404(Book, book_id)
        new_rating = change_form.new_rating
        book_to_update.rating=new_rating
        db.session.commit()
        return redirect(url_for('home'))
    book_to_update = db.get_or_404(Book, book_id)
    book_name = book_to_update.title
    rating = book_to_update.rating
    return render_template("change_rate.html", form = change_form, book_name=book_name, rating=rating)


if __name__ == "__main__":
    app.run(debug=True)
