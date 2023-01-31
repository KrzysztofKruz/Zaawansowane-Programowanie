from flask import Flask
from flask import render_template
# from flask_navigation import Navigation
from Model.MoviesLogic import MoviesLogic
from Model.TagsLogic import TagsLogic
from Model.RatingsLogic import RatingsLogic
from Model.LinksLogic import LinksLogic


app = Flask(__name__, template_folder='View')
# nav = Navigation(app)

# nav.Bar('top', [
#     nav.Item('Home', 'home'),
#     nav.Item('Movies', 'movies'),
#     nav.Item('Links', 'links'),
#     nav.Item('Ratings', 'ratings'),
#     nav.Item('Tags', 'tags')
# ])


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html", title="Home page (it's empty!)", display=False)


@app.route('/movies/<item_count>', methods=['GET'])
def movies(item_count: int):
    logic = MoviesLogic()
    movies = logic.read_movies("Database/movies.csv", item_count)
    return render_template("index.html", data=movies, title="Movies", display=True)


@app.route('/get_movies/<item_count>', methods=['GET'])
def get_movies(item_count: int):
    logic = MoviesLogic()
    movies = logic.read_movies("Database/movies.csv", item_count)
    return movies


@app.route('/links/<item_count>', methods=['GET'])
def links(item_count: int):
    logic = LinksLogic()
    links = logic.read_links("Database/links.csv", item_count)
    return render_template("links.html", data=links, title="Links", display=True)


@app.route('/get_links/<item_count>', methods=['GET'])
def get_links(item_count: int):
    logic = LinksLogic()
    links = logic.read_links("Database/links.csv", item_count)
    return links


@app.route('/ratings', methods=['GET'])
def ratings():
    logic = RatingsLogic()
    ratings = logic.read_ratings("Database/ratings.csv")
    return render_template("index.html", data=ratings, title="Ratings", display=True)


@app.route('/tags', methods=['GET'])
def tags():
    logic = TagsLogic()
    tags = logic.read_tags("Database/tags.csv")
    return render_template("index.html", data=tags, title="Tags", display=True)
