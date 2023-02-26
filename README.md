# Let's get cloud

This project is a web application that generates a word cloud from the script of a user's favorite movie. Users can search for a movie by typing its name in a search box, and the application will retrieve the movie script from a database and generate a word cloud visualization. The word cloud displays the most frequent words from the movie script, with the size of each word representing its frequency. Users can customize the word cloud by changing its size, colors, and font. The application also includes autocomplete functionality for the search box, allowing users to quickly find the movie they're looking for. This project is built using Flask, Python, JavaScript, and various libraries for data visualization and web development.

## Usage

Clone the repository and navigate to the project directory in your terminal:

```
git clone https://github.com/armferreira/lets-get-cloud
cd lets-get-cloud
```

Install the required Python packages using pip:

```
pip install -r requirements.txt
```

Initialize the database and import movie scripts by running the init_db.py script:

```
python init_db.py
```

Start the Flask application:

```
flask run
```

Open a web browser and navigate to http://localhost:5000 to use the word cloud generator.

Type in the name of a movie in the search box and click "Generate" to create a word cloud from the movie script. The word cloud will be displayed on the same page.

To learn more about the project, click on the "About" link in the navigation bar.


## Dependencies

As stated above, you can check all requirements on the requirements.txt file and install them by simply running the following code:

```
pip install -r requirements.txt
```

## Directory structure

After running all the steps, your folder structure should look something like this:

```
lets-get-cloud
│
├── static
│   └── styles.css
│
├── templates
│   ├── about.html
│   ├── home.html
│   └── layout.html
│
├── app.py
│  
├── movies.db
│
├── README.md
│
└── requirements.txt
```

## Credits

1. The database was built with the help of this script:

```
@misc{Saha_Movie_Script_Database_2021,
    author = {Saha, Aveek},
    month = {7},
    title = {{Movie Script Database}},
    url = {https://github.com/Aveek-Saha Movie-Script-Database},
    year = {2021}
}
```
2. The WordlCloud library can be found here:
```
@misc{word_cloud,
    author = {Andreas, Muller},
    month = {8},
    title = {{World Cloud}},
    url = {https://github.com/amueller/word_cloud},
    year = {2018}
}
```