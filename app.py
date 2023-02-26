from flask import Flask, render_template, request, jsonify
from cs50 import SQL
from wordcloud import WordCloud
import io
import base64

app = Flask(__name__)

db = SQL("sqlite:///movies.db")


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # Retrieve all movie names from the database
        movie_names = db.execute("SELECT name FROM movies")

        # Extract the movie names from the returned dictionaries and store them in a list
        movie_names = [movie['name'] for movie in movie_names]
        
        # Pass the movie names to the home.html template
        return render_template("home.html", movie_names=movie_names)

    else:

        # Read the corresponding script file or data from the database
        movie_name = request.form.get('movie_name')
        movie_script = db.execute("SELECT script FROM movies WHERE name = ?", movie_name)
        
        # Handle exception cases
        if not movie_script:
            error = "Movie not found"
            return render_template("home.html", error = error)

        # Generate the word cloud        
        movie_script = movie_script[0]['script']
        wordcloud = WordCloud(width=600, height=600, background_color = '#1c1e1f', mode='RGB').generate(movie_script)

        # Save the image to a file object
        img_buffer = io.BytesIO()
        wordcloud.to_image().save(img_buffer, format='PNG')
        img_buffer.seek(0)

        # Encode the image in base64 format for display in the template
        img_str = base64.b64encode(img_buffer.getvalue()).decode('ascii')

        # Pass the image data to the template and render it
        return render_template("home.html", image_data=img_str)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('q')
    movies = db.execute("SELECT name FROM movies WHERE name LIKE :query LIMIT 5", query=f"%{query}%")
    movies = [movie['name'] for movie in movies]
    return jsonify(movies)
