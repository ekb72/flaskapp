from flask import Flask
from flask-sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


@app.route('/')

def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about_page():
    return """Founded in 1999, the Sheep Milking Matchmakers is based in London.
    <h1>How we match potential Sheep!</h1>

      <img src="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiNn8XLno_hAhUwn-AKHY39D6AQjRx6BAgBEAU&url=https%3A%2F%2Funsplash.com%2Fsearch%2Fphotos%2Fsheep&psig=AOvVaw0ss3FAwZ5v96wiJwTa6Vt9&ust=1553120422563732"
      alt="map of newyork">

      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=newyork" alt="street view of newyork">
      """
@app.route('/contact us')
def _page():
    return """Founded in 1999, the Sheep Milking Matchmakers is based in London.
    <h1>Email us to reach us!</h1>
    <h2> sheepmilkisgud@farm.com <h2>

      <img src="https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiNn8XLno_hAhUwn-AKHY39D6AQjRx6BAgBEAU&url=https%3A%2F%2Funsplash.com%2Fsearch%2Fphotos%2Fsheep&psig=AOvVaw0ss3FAwZ5v96wiJwTa6Vt9&ust=1553120422563732"
      alt="map of newyork">

      <img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=newyork" alt="street view of newyork">
      """
