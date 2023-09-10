import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv


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
load_dotenv()
API_KEY = os.getenv('TMBD_API_KEY')


# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

# Create the extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovie(FlaskForm):
    title = StringField("Movie Title")
    submit = SubmitField("Done")


"""
#Insert Movie 1
with app.app_context():

    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    db.session.add(new_movie)
    db.session.commit()


#Insert Movie 2
with app.app_context():

    new_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully "
                    "family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go "
                    "to keep each other safe, the battles they fight to stay alive, and the tragedies they "
                    "endure.",

        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )

    db.session.add(new_movie)
    db.session.commit()

"""

def get_movie_data(movie_title):

    url = ("https://api.themoviedb.org/3/search/movie?query=" + movie_title +
           "&include_adult=false&language=en-US&page=1")

    headers = {
        "accept": "application/json",
        "Authorization": API_KEY
    }

    response = requests.get(url, headers=headers, verify=False)

    return response.json()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all() # converts ScalarResult into Python list

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
        print(all_movies[i],":",all_movies[i].rating)
    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET","POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete", methods=["GET","POST"])
def delete_movie():

    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))



@app.route("/add", methods=["GET","POST"])
def add_movie():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        json_movie_data = get_movie_data(movie_title)
        movie_data = json_movie_data["results"]
        #print(movie_data)
        return render_template("select.html", movies=movie_data)
    return render_template("add.html",form=form)

@app.route("/create", methods=["GET","POST"])
def create_movie():
    update = True
    id = request.args.get("id")
    title = request.args.get("title")
    year = request.args.get("year")
    img_url = request.args.get("img_url")
    description = request.args.get("description")
    print(id, title,year,img_url,description)
    final_url = "https://image.tmdb.org/t/p/original" + img_url
    final_year = year.split('-')[0]
    print(final_url,final_year)
    new_movie = Movie(
        id = id,
        title = title,
        year= final_year,
        description= description,
        img_url=final_url
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('rate_movie', id=id))

if __name__ == '__main__':
    app.run(debug=True)
