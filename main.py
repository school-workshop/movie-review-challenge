"""
================================================================================
MAIN APPLICATION FILE - MOVIE REVIEW APP
================================================================================

This is the MAIN file that runs your web application!
Think of it as the "brain" of your app - it controls everything.

WHAT IS FastAPI?
----------------
FastAPI is a Python framework for building web applications.
A framework is like a toolkit that gives us pre-built tools to make websites.

FastAPI helps us:
- Create web pages (routes)
- Handle user requests (clicking links, submitting forms)
- Return HTML pages to the browser

HOW WEB APPLICATIONS WORK:
--------------------------
1. User opens their browser and goes to a URL (like http://localhost:8000)
2. The browser sends a REQUEST to our server
3. Our server (this Python code!) processes the request
4. We send back a RESPONSE (usually an HTML page)
5. The browser displays the page to the user

WHAT ARE ROUTES?
----------------
Routes are like addresses for different pages on your website.
- "/" is the home page (http://localhost:8000/)
- "/movie/1" is the page for movie with ID 1
- "/search" is the search results page

Each route has a function that runs when someone visits that page.

HOW TO RUN THIS APP:
--------------------
Open your terminal and run:
    uvicorn main:app --reload

Then open your browser to: http://127.0.0.1:8000

The --reload flag means the server restarts when you change code!

================================================================================
"""

# ============================================================================
# IMPORTS - Load the tools we need
# ============================================================================

# FastAPI is our web framework - it helps us build web applications
from fastapi import FastAPI, Request, Form

# HTMLResponse tells FastAPI we're returning HTML pages
# RedirectResponse sends users to a different page (like after submitting a form)
from fastapi.responses import HTMLResponse, RedirectResponse

# StaticFiles lets us serve CSS, images, and other static files
from fastapi.staticfiles import StaticFiles

# Jinja2Templates helps us use HTML templates with dynamic data
from fastapi.templating import Jinja2Templates

# Import our database functions
# These are the functions you'll complete in database.py!
from database import (
    load_movies,           # Challenge 1 - Load all movies
    get_movie_by_id,       # Challenge 2 - Find one movie
    add_review,            # Challenge 3 - Save a review
    get_average_rating,    # Challenge 4 - Calculate average rating
    search_movies,         # Challenge 5 - Search movies
    get_top_rated_movies   # Challenge 6 - Get top rated movies
)


# ============================================================================
# APP SETUP - Configure our web application
# ============================================================================

# Create our FastAPI application instance
# This is the main object that represents our web app
app = FastAPI()

# Mount static files (CSS, images, etc.)
# This tells FastAPI: "When someone requests /static/..., look in the 'static' folder"
# Example: /static/css/style.css -> static/css/style.css
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
# Templates are HTML files with placeholders for dynamic data
# Example: {{ movie.title }} gets replaced with the actual movie title
templates = Jinja2Templates(directory="templates")


# ============================================================================
# ROUTE 1: HOME PAGE
# URL: http://localhost:8000/
# ============================================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Display the home page with all movies.

    WHAT IS @app.get("/")?
    ----------------------
    This is called a "decorator" - it tells FastAPI:
    "When someone visits the root URL (/), run this function"

    @app.get means this handles GET requests (loading a page)
    "/" is the URL path (the home page)
    response_class=HTMLResponse means we're returning HTML

    WHAT IS 'request'?
    ------------------
    The 'request' parameter contains information about the user's request:
    - What URL they visited
    - What browser they're using
    - Any data they sent

    We pass it to our template so Jinja2 can use it.

    WHAT DOES THIS FUNCTION DO?
    ---------------------------
    1. Loads all movies from the database
    2. Calculates the average rating for each movie
    3. Gets the top 5 rated movies for the featured section
    4. Renders the index.html template with this data
    5. Returns the HTML page to the user's browser
    """
    # Step 1: Load all movies from the database
    # This calls the load_movies() function in database.py
    movies = load_movies()

    # Step 2: Add average rating to each movie for display
    # We loop through each movie and calculate its rating
    for movie in movies:
        # get_average_rating() returns 0 if no reviews, or the average
        movie["avg_rating"] = get_average_rating(movie["id"])

    # Step 3: Get top rated movies for the "Top 5" section
    # This shows users which movies are most popular
    top_movies = get_top_rated_movies(5)

    # Step 4: Render the template and return it
    # templates.TemplateResponse() loads an HTML file and fills in the data
    # We pass a dictionary with all the variables the template needs
    return templates.TemplateResponse("index.html", {
        "request": request,      # Required by FastAPI
        "movies": movies,        # All movies to display
        "top_movies": top_movies # Top 5 rated movies
    })


# ============================================================================
# ROUTE 2: MOVIE DETAIL PAGE
# URL: http://localhost:8000/movie/1 (where 1 is the movie ID)
# ============================================================================

@app.get("/movie/{movie_id}", response_class=HTMLResponse)
def movie_detail(request: Request, movie_id: int):
    """
    Display a single movie's details and reviews.

    WHAT IS {movie_id}?
    -------------------
    The curly braces create a "path parameter" - a variable part of the URL.
    When someone visits /movie/5, movie_id will be 5.
    When someone visits /movie/12, movie_id will be 12.

    The ": int" tells FastAPI that movie_id should be an integer (whole number).
    If someone visits /movie/abc, FastAPI will return an error automatically!

    WHAT DOES THIS FUNCTION DO?
    ---------------------------
    1. Looks up the movie by its ID
    2. If not found, shows an error page
    3. Gets the average rating for this movie
    4. Shows the movie details, reviews, and a form to add new reviews
    """
    # Step 1: Get the movie from the database
    # This calls get_movie_by_id() which you'll implement in database.py
    movie = get_movie_by_id(movie_id)

    # Step 2: Check if the movie was found
    # If get_movie_by_id returns None, the movie doesn't exist
    if movie is None:
        # Return an error page
        return templates.TemplateResponse("error.html", {
            "request": request,
            "message": "Movie not found"  # Error message to display
        })

    # Step 3: Get the average rating for this movie
    avg_rating = get_average_rating(movie_id)

    # Step 4: Render the movie detail page
    return templates.TemplateResponse("movie.html", {
        "request": request,
        "movie": movie,           # The movie data (title, plot, reviews, etc.)
        "avg_rating": avg_rating  # The calculated average rating
    })


# ============================================================================
# ROUTE 3: SUBMIT A REVIEW
# URL: POST to http://localhost:8000/movie/1/review
# ============================================================================

@app.post("/movie/{movie_id}/review")
def submit_review(
    movie_id: int,
    reviewer_name: str = Form(...),
    rating: int = Form(...),
    comment: str = Form(...)
):
    """
    Handle the review form submission.

    WHAT IS @app.post()?
    --------------------
    Unlike @app.get() which handles loading pages,
    @app.post() handles form submissions.

    When a user fills out a form and clicks "Submit",
    the browser sends a POST request with the form data.

    WHAT IS Form(...)?
    ------------------
    Form() tells FastAPI to get the value from the submitted form.
    The ... means the field is required - if it's missing, show an error.

    The form in movie.html has these fields:
    - reviewer_name: The user's name
    - rating: Their star rating (1-5)
    - comment: Their written review

    WHAT DOES THIS FUNCTION DO?
    ---------------------------
    1. Receives the form data from the user
    2. Creates a review dictionary with the data
    3. Saves the review to the database
    4. Redirects the user back to the movie page
    """
    # Step 1: Create a review dictionary with the submitted data
    # This is the format our add_review() function expects
    review = {
        "name": reviewer_name,  # Who wrote the review
        "rating": rating,       # Their star rating (1-5)
        "comment": comment      # Their written review
    }

    # Step 2: Save the review to the database
    # This calls add_review() which you'll implement in database.py
    add_review(movie_id, review)

    # Step 3: Redirect back to the movie page
    # RedirectResponse sends the user to a different URL
    # status_code=303 tells the browser to use GET for the redirect
    # This prevents the form from being resubmitted if they refresh
    return RedirectResponse(url=f"/movie/{movie_id}", status_code=303)


# ============================================================================
# ROUTE 4: SEARCH MOVIES
# URL: http://localhost:8000/search?q=spider
# ============================================================================

@app.get("/search", response_class=HTMLResponse)
def search(request: Request, q: str = ""):
    """
    Search for movies by title.

    WHAT IS 'q: str = ""'?
    ----------------------
    This is a "query parameter" - it comes from the URL after the ?
    Example: /search?q=spider means q will be "spider"

    The '= ""' means if no search term is provided, use an empty string.
    This prevents errors if someone visits /search without a query.

    QUERY PARAMETERS VS PATH PARAMETERS:
    ------------------------------------
    Path parameter: /movie/5 (movie_id = 5)
    Query parameter: /search?q=spider (q = "spider")

    Query parameters are optional and use the ? syntax.
    Path parameters are required parts of the URL.

    WHAT DOES THIS FUNCTION DO?
    ---------------------------
    1. Gets the search query from the URL
    2. Searches for movies matching that query
    3. Adds average ratings to each result
    4. Displays the results on the home page
    """
    # Step 1: Search for movies using the query
    # This calls search_movies() which you'll implement in database.py
    movies = search_movies(q)

    # Step 2: Add average rating to each movie
    # This is the same as the home page - we want to show ratings
    for movie in movies:
        movie["avg_rating"] = get_average_rating(movie["id"])

    # Step 3: Render the page with search results
    # We reuse index.html but pass the search_query so it shows
    # "Search results for: spider" at the top
    return templates.TemplateResponse("index.html", {
        "request": request,
        "movies": movies,         # The search results
        "search_query": q         # The search term (for display)
    })


# ============================================================================
# HOW TO RUN THIS APPLICATION
# ============================================================================

# To run the app, open your terminal and type:
#     uvicorn main:app --reload
#
# Then open your web browser and go to:
#     http://127.0.0.1:8000
#
# WHAT DOES THIS COMMAND MEAN?
# ----------------------------
# uvicorn: The server that runs our app
# main: The name of this file (main.py)
# app: The name of our FastAPI instance (see line 67)
# --reload: Automatically restart when you change code
#
# USEFUL URLs:
# ------------
# Home page:      http://127.0.0.1:8000
# Movie details:  http://127.0.0.1:8000/movie/1
# Search:         http://127.0.0.1:8000/search?q=dark
# API docs:       http://127.0.0.1:8000/docs (automatic documentation!)
