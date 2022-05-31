
from flask import Flask, render_template, request, url_for, redirect
import tmdb_client


app = Flask(__name__)

current_list = ("popular", "top_rated", "upcoming", "now_playing")
@app.route('/')
def homepage():
    selected_list = request.args.get("list_type", "popular")
    if selected_list in current_list:
        movies = (tmdb_client.get_movies(how_many=8, list_type=selected_list))
        return render_template("homepage.html", movies=movies, current_list=current_list, selected_list=selected_list)
    else:
        return redirect(url_for("homepage", list_type="popular"))

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}  

def get_movie_info():
    data = tmdb_client.get_popular_movies()
    for result in data["results"]:
        movie_title=result["title"]
        path = result["poster_path"]
        poster_url = tmdb_client.get_poster_url(path, size="w342")
        dict = {movie_title:poster_url}
        return dict

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)[:8]
    return render_template("movie_details.html", movie=details, cast=cast, details=details)


if __name__ == '__main__':
    app.run(debug=True)