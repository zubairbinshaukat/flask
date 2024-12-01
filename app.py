from flask import Flask, render_template

app = Flask(__name__)

# Dummy data for movies
movies = {
    1: {"title": "Inception", "description": "A mind-bending thriller", "poster": "inception.jpg"},
    2: {"title": "The Matrix", "description": "A hacker discovers the truth about reality", "poster": "matrix.jpg"},
    3: {"title": "Interstellar", "description": "Exploration of space and time", "poster": "interstellar.jpg"}
}

@app.route("/")
def home():
    return render_template("home.html", movies=movies)

@app.route("/movie/<int:movie_id>")
def movie(movie_id):
    movie_data = movies.get(movie_id)
    if not movie_data:
        return "Movie not found", 404
    return render_template("movie.html", movie=movie_data)

if __name__ == "__main__":
    app.run(debug=True)
