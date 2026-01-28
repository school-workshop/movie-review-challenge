# Student Challenge Guide

## How This Works

All your challenges are in one file: `database.py`

Open it and look for the `TODO` comments. Complete each challenge in order!

**This app uses SQLAlchemy** - a popular Python library for working with databases.
The database file is called `movies.db` and it's created automatically when you run the app.

---

## About the Movie Data

Your app has access to **9,800+ real movies** from TMDB (The Movie Database)!

This data was loaded from [Hugging Face](https://huggingface.co/datasets/Pablinho/movies-dataset) - a website where developers share datasets. Pretty cool, right? You're working with real movie data that includes:
- Movie titles and release years
- Plot descriptions (what the movie is about)
- Genres like Action, Comedy, Drama, Horror, Animation
- Movie poster images

This means when you build the search feature, you'll have thousands of movies to search through!

---

## Challenge 1: Load Movies (DONE!)
**Already completed for you!**

Look at the `load_movies()` function to see how it works. It shows you:
- How to create a session (connection to the database)
- How to query data using `session.query(Model).all()`
- How to convert objects to dictionaries

Use it as a reference for the other challenges!

---

## Challenge 2: Find a Movie by ID
**Difficulty:** Easy | **Time:** 10 mins

### Goal
When someone clicks a movie card, we need to find that specific movie's data.

### The Function
```python
def get_movie_by_id(movie_id):
    # Your code here!
    pass
```

### What to Do
1. Create a session: `session = get_session()`
2. Query the movie using filter:
   `movie = session.query(Movie).filter(Movie.id == movie_id).first()`
3. Check if movie was found: `if movie is None: return None`
4. Convert to dictionary: `result = movie.to_dict()`
5. Close session: `session.close()`
6. Return the result

### Hints
```python
session = get_session()

try:
    movie = session.query(Movie).filter(Movie.id == movie_id).first()

    if movie is None:
        return None

    return movie.to_dict()

finally:
    session.close()
```

### Test It
Click on any movie poster. The movie detail page should load with the correct title, poster, and plot.

---

## Challenge 3: Save a Review
**Difficulty:** Medium | **Time:** 15 mins

### Goal
When someone submits the review form, save their review to the database!

### The Function
```python
def add_review(movie_id, review):
    # Your code here!
    pass
```

### What to Do
1. Create a session: `session = get_session()`
2. Create a Review object with the data
3. Add it to the session: `session.add(new_review)`
4. Commit changes: `session.commit()`
5. Close session: `session.close()`

### Hints
```python
session = get_session()

try:
    new_review = Review(
        movie_id=movie_id,
        reviewer_name=review["name"],
        rating=review["rating"],
        comment=review["comment"]
    )

    session.add(new_review)
    session.commit()

finally:
    session.close()
```

### Test It
1. Click a movie to open its detail page
2. Fill in your name, select stars, write a comment
3. Click "Submit Review"
4. Your review should appear below the form!

---

## Challenge 4: Calculate Average Rating
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Show the average star rating based on all reviews.

### The Function
```python
def get_average_rating(movie_id):
    # Your code here!
    return 0
```

### What to Do
1. Get movie: `movie = get_movie_by_id(movie_id)`
2. Check if movie exists: `if movie is None: return 0`
3. Get reviews: `reviews = movie.get("reviews", [])`
4. If no reviews (length is 0), return `0`
5. Add up all the ratings using a loop
6. Divide total by number of reviews
7. Use `round(average, 1)` to round to 1 decimal place

### Hints
```python
movie = get_movie_by_id(movie_id)

if movie is None:
    return 0

reviews = movie.get("reviews", [])

if len(reviews) == 0:
    return 0

total = 0
for review in reviews:
    total = total + review["rating"]

average = total / len(reviews)
return round(average, 1)
```

### Test It
1. Add a few reviews with different star ratings
2. The star display should update to show the average
3. The rating number (like "4.2") should be accurate

---

## Challenge 5: Search Movies
**Difficulty:** Easy | **Time:** 10 mins

### Goal
Make the search bar work!

### The Function
```python
def search_movies(query):
    # Your code here!
    return load_movies()
```

### What to Do
1. If query is empty, return all movies: `return load_movies()`
2. Load all movies: `movies = load_movies()`
3. Convert query to lowercase: `query.lower()`
4. Loop through movies
5. Check if query is in the movie title (also lowercase)
6. Add matching movies to a results list
7. Return the results

### Hints
```python
if query == "":
    return load_movies()

movies = load_movies()
query_lower = query.lower()
results = []

for movie in movies:
    if query_lower in movie["title"].lower():
        results.append(movie)

return results
```

### Test It
- Type "batman" - should show all Batman movies
- Type "SPIDER" - should show all Spider-Man movies
- Type "avengers" - should show all Avengers movies
- Type "xyz123" - should show "No movies found"

With 9,800+ movies, searching is way more fun!

---

## Challenge 6: Top 5 Highest Rated
**Difficulty:** Medium | **Time:** 15 mins

### Goal
Show the user's top 5 highest-rated movies on the home page!

### The Function
```python
def get_top_rated_movies(limit=5):
    # Your code here!
    return []
```

### What to Do
1. Get all movies: `movies = load_movies()`
2. Create an empty list for movies with ratings
3. Loop through each movie
4. Get the average rating using `get_average_rating(movie["id"])`
5. Only include movies that have reviews (rating > 0)
6. Add the rating to the movie: `movie["avg_rating"] = rating`
7. Append the movie to your list
8. Sort the list by rating (highest first)
9. Return only the first `limit` movies

### Hints
```python
movies = load_movies()
rated_movies = []

for movie in movies:
    rating = get_average_rating(movie["id"])
    if rating > 0:
        movie["avg_rating"] = rating
        rated_movies.append(movie)

# Sort by rating, highest first
sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

# Return only the top 'limit' movies
return sorted_movies[:limit]
```

### Test It
1. First, add reviews to a few movies with different ratings
2. Go back to the home page
3. You should see a "Top 5 Highest Rated" section appear
4. Movies should be ranked from highest to lowest rating

---

# BONUS CHALLENGES!

Finished the main challenges? Try these bonus ones!

---

## Challenge 7: Filter by Genre (BONUS)
**Difficulty:** Easy | **Time:** 10 mins

### Goal
Get all movies of a specific genre (like "Action" or "Drama").

### The Function
```python
def get_movies_by_genre(genre):
    # Your code here!
    return load_movies()
```

### Hints
```python
movies = load_movies()

if genre == "":
    return movies

genre_lower = genre.lower()
results = []

for movie in movies:
    if movie["genre"].lower() == genre_lower:
        results.append(movie)

return results
```

---

## Challenge 8: Count Reviews (BONUS)
**Difficulty:** Easy | **Time:** 5 mins

### Goal
Count how many reviews a movie has.

### The Function
```python
def count_reviews(movie_id):
    # Your code here!
    return 0
```

### Hints
```python
movie = get_movie_by_id(movie_id)
if movie is None:
    return 0
return len(movie.get("reviews", []))
```

---

## Challenge 9: Get All Genres (BONUS)
**Difficulty:** Medium | **Time:** 10 mins

### Goal
Get a list of all unique genres (no duplicates).

### The Function
```python
def get_all_genres():
    # Your code here!
    return []
```

### Hints
```python
movies = load_movies()
genres = []

for movie in movies:
    if movie["genre"] not in genres:
        genres.append(movie["genre"])

genres.sort()
return genres
```

---

## Challenge 10: Delete a Review (BONUS)
**Difficulty:** Medium | **Time:** 10 mins

### Goal
Remove a review from the database.

### The Function
```python
def delete_review(review_id):
    # Your code here!
    pass
```

### Hints
```python
session = get_session()

try:
    review = session.query(Review).filter(Review.id == review_id).first()

    if review:
        session.delete(review)
        session.commit()

finally:
    session.close()
```

---

## Finished Everything?

Amazing work! You've built a complete web application with a real database!

### What You Learned
- Python fundamentals (functions, loops, dictionaries)
- **SQLAlchemy ORM** - industry-standard database library
- **Database Models** - representing tables as Python classes
- **Sessions** - managing database connections
- **Real-world data** - working with a dataset of 9,800+ movies from Hugging Face
- FastAPI for web routes
- HTML templates with Jinja2
- Form handling

### Next Steps
1. Show a mentor to get your completion certificate!
2. Try adding more features to the app

### Want to Learn More About Data?
The movie data in this app came from **Hugging Face** (huggingface.co) - a free platform where developers share:
- **Datasets** - collections of data like our movies
- **AI Models** - pre-trained artificial intelligence you can use
- **Code** - examples and tutorials

Check it out if you want to build more cool projects with real data!

---

## Quick Reference

### SQLAlchemy Query Methods
```python
# Get all rows
movies = session.query(Movie).all()

# Get one row by filter
movie = session.query(Movie).filter(Movie.id == 1).first()

# Count rows
count = session.query(Movie).count()

# Add new row
session.add(new_movie)
session.commit()

# Delete row
session.delete(movie)
session.commit()
```

### Session Pattern (Always use try/finally!)
```python
session = get_session()

try:
    # Your database code here
    movies = session.query(Movie).all()
    return [m.to_dict() for m in movies]

finally:
    session.close()  # Always close the session!
```

### Dictionaries (like JavaScript objects)
```python
# Create
movie = {
    "title": "Batman",
    "year": 2022
}

# Access
movie["title"]      # "Batman"
movie.get("year")   # 2022
```

### Lists (like JavaScript arrays)
```python
# Create
movies = ["Batman", "Spider-Man"]

# Loop
for movie in movies:
    print(movie)

# Add item
movies.append("Avatar")
```

### Loops
```python
# Loop through list
for movie in movies:
    print(movie["title"])

# Loop with counting
total = 0
for review in reviews:
    total = total + review["rating"]
```

### If Statements
```python
if query == "":
    return load_movies()

if len(reviews) == 0:
    return 0
```
