"""
================================================================================
DATABASE FUNCTIONS FOR THE MOVIE REVIEW APP
================================================================================

This file contains ALL the functions that work with our movie database.
We use SQLAlchemy - a popular Python library for working with databases.

WHAT IS A DATABASE?
-------------------
A database is like a super organized filing cabinet for your data.
Instead of storing data in text files, databases let you:
- Store large amounts of data efficiently
- Search and filter data quickly
- Keep data organized in tables (like spreadsheets)

WHAT IS SQLAlchemy?
-------------------
SQLAlchemy is a Python library that makes working with databases easier.
It provides two ways to work with databases:

1. ORM (Object-Relational Mapping) - Treat database rows as Python objects
2. Core - Write SQL-like queries in Python

We use SQLAlchemy because:
- It's used by many real-world Python applications
- It works with many different databases (SQLite, PostgreSQL, MySQL)
- It makes database code easier to read and write
- It's safer (helps prevent SQL injection attacks)

WHAT IS SQLite?
---------------
SQLite is a lightweight database that:
- Stores everything in ONE file (movies.db)
- Doesn't need a separate server to run
- Is perfect for learning and small applications
- Is used by many real apps (including your phone!)

HOW THIS FILE IS ORGANIZED:
---------------------------
1. Models - Define the structure of our database tables
2. Setup functions - Create the database and tables
3. Challenge functions - The coding challenges YOU will complete!

IMPORTANT: Complete the TODO challenges to make the app work!
================================================================================
"""

# ============================================================================
# IMPORTS - These are like toolboxes we need to use
# ============================================================================

# SQLAlchemy imports for database operations
# create_engine: Creates a connection to the database
# Column, Integer, String, Text, ForeignKey: Define table columns
# declarative_base: Base class for our models
# sessionmaker: Creates database sessions for queries
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# This is the connection string for our SQLite database
# "sqlite:///movies.db" means:
# - sqlite: the type of database
# - ///: three slashes for a relative path
# - movies.db: the database file name
DATABASE_URL = "sqlite:///movies.db"

# Create the database engine
# The engine is like a factory that creates database connections
# echo=False means don't print SQL queries to the console (set to True for debugging)
engine = create_engine(DATABASE_URL, echo=False)

# Create a base class for our models
# All our table classes will inherit from this Base
Base = declarative_base()

# Create a session factory
# Sessions are used to interact with the database
# autocommit=False means we control when changes are saved
# autoflush=False means we control when data is sent to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ============================================================================
# DATABASE MODELS - Define the structure of our tables
# ============================================================================

class Movie(Base):
    """
    The Movie model represents the 'movies' table in our database.

    WHAT IS A MODEL?
    ----------------
    A model is a Python class that represents a database table.
    Each attribute of the class becomes a column in the table.
    Each instance of the class represents a row in the table.

    WHAT IS __tablename__?
    ----------------------
    This tells SQLAlchemy what to name the table in the database.

    COLUMN TYPES:
    -------------
    - Integer: Whole numbers (1, 2, 3, etc.)
    - String(length): Text with a maximum length
    - Text: Text with no length limit (for long content like plot descriptions)

    WHAT IS primary_key?
    --------------------
    The primary key uniquely identifies each row in the table.
    No two movies can have the same id.

    WHAT IS nullable?
    -----------------
    nullable=False means this column MUST have a value.
    You cannot add a movie without a title, for example.
    """
    __tablename__ = "movies"

    # Primary key - unique identifier for each movie
    id = Column(Integer, primary_key=True, index=True)

    # Movie information columns
    title = Column(String(200), nullable=False)    # Movie title (max 200 characters)
    year = Column(Integer, nullable=False)          # Release year
    genre = Column(String(50), nullable=False)      # Genre (Action, Drama, etc.)
    poster = Column(String(500), nullable=False)    # URL to poster image
    plot = Column(Text, nullable=False)             # Plot description

    # Relationship to reviews
    # This creates a connection between Movie and Review
    # back_populates links this to the 'movie' attribute in Review
    reviews = relationship("Review", back_populates="movie")

    def to_dict(self):
        """
        Convert the Movie object to a dictionary.

        WHY DO WE NEED THIS?
        --------------------
        Our templates expect dictionaries, not SQLAlchemy objects.
        This method converts the object to a dictionary format.

        Returns:
            dict: Movie data as a dictionary
        """
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "genre": self.genre,
            "poster": self.poster,
            "plot": self.plot,
            "reviews": [review.to_dict() for review in self.reviews]
        }


class Review(Base):
    """
    The Review model represents the 'reviews' table in our database.

    WHAT IS A FOREIGN KEY?
    ----------------------
    A foreign key links one table to another.
    movie_id is a foreign key that points to a movie's id.
    This tells us which movie the review is about.

    WHAT IS A RELATIONSHIP?
    -----------------------
    A relationship creates a connection between two models.
    This lets us easily access related data:
    - review.movie gives us the Movie object
    - movie.reviews gives us all Review objects for that movie
    """
    __tablename__ = "reviews"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign key - links to the movies table
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)

    # Review information columns
    reviewer_name = Column(String(100), nullable=False)  # Name of the reviewer
    rating = Column(Integer, nullable=False)              # Star rating (1-5)
    comment = Column(Text, nullable=False)                # The review text
    created_at = Column(DateTime, default=datetime.now)   # When the review was created

    # Relationship to movie
    movie = relationship("Movie", back_populates="reviews")

    def to_dict(self):
        """Convert the Review object to a dictionary."""
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "reviewer_name": self.reviewer_name,
            "name": self.reviewer_name,  # Alias for compatibility
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.strftime("%d %b %Y at %H:%M") if self.created_at else None
        }


# ============================================================================
# DATABASE SETUP - Create tables and seed data
# ============================================================================

def create_tables():
    """
    Create all database tables based on our models.

    HOW IT WORKS:
    -------------
    Base.metadata.create_all() looks at all classes that inherit from Base
    and creates the corresponding tables in the database if they don't exist.

    This is called when the app starts to make sure our tables exist.
    """
    Base.metadata.create_all(bind=engine)


def get_session():
    """
    Create a new database session.

    WHAT IS A SESSION?
    ------------------
    A session is like a conversation with the database.
    You use it to:
    - Query data (SELECT)
    - Add new data (INSERT)
    - Update existing data (UPDATE)
    - Delete data (DELETE)

    Always close the session when you're done!

    Returns:
        Session: A new database session
    """
    return SessionLocal()


def seed_movies():
    """
    Add initial movie data to the database.

    WHAT IS SEEDING?
    ----------------
    "Seeding" means adding initial/starter data to your database.
    This gives us some movies to display when the app first runs.

    We check if movies already exist to avoid adding duplicates.
    """
    session = get_session()

    try:
        # Check if we already have movies
        existing_count = session.query(Movie).count()
        if existing_count > 0:
            return  # Database already seeded

        # List of movies to add
        movies_data = [
            {
                "title": "The Dark Knight",
                "year": 2008,
                "genre": "Action",
                "poster": "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX300.jpg",
                "plot": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."
            },
            {
                "title": "Inception",
                "year": 2010,
                "genre": "Sci-Fi",
                "poster": "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg",
                "plot": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."
            },
            {
                "title": "Spider-Man: Into the Spider-Verse",
                "year": 2018,
                "genre": "Animation",
                "poster": "https://m.media-amazon.com/images/M/MV5BMjMwNDkxMTgzOF5BMl5BanBnXkFtZTgwNTkwNTQ3NjM@._V1_SX300.jpg",
                "plot": "Teen Miles Morales becomes the Spider-Man of his universe, and must join with five spider-powered individuals from other dimensions to stop a threat for all realities."
            },
            {
                "title": "The Shawshank Redemption",
                "year": 1994,
                "genre": "Drama",
                "poster": "https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_SX300.jpg",
                "plot": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
            },
            {
                "title": "Interstellar",
                "year": 2014,
                "genre": "Sci-Fi",
                "poster": "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
                "plot": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."
            },
            {
                "title": "The Lion King",
                "year": 1994,
                "genre": "Animation",
                "poster": "https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_SX300.jpg",
                "plot": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself."
            },
            {
                "title": "Avengers: Endgame",
                "year": 2019,
                "genre": "Action",
                "poster": "https://m.media-amazon.com/images/M/MV5BMTc5MDE2ODcwNV5BMl5BanBnXkFtZTgwMzI2NzQ2NzM@._V1_SX300.jpg",
                "plot": "After the devastating events of Infinity War, the Avengers assemble once more to reverse Thanos' actions and restore balance to the universe."
            },
            {
                "title": "Parasite",
                "year": 2019,
                "genre": "Drama",
                "poster": "https://m.media-amazon.com/images/M/MV5BYWZjMjk3ZTItODQ2ZC00NTY5LWE0ZDYtZTI3MjcwN2Q5NTVkXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_SX300.jpg",
                "plot": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan."
            },
            {
                "title": "The Matrix",
                "year": 1999,
                "genre": "Sci-Fi",
                "poster": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
                "plot": "A computer hacker learns about the true nature of reality and his role in the war against its controllers."
            },
            {
                "title": "Forrest Gump",
                "year": 1994,
                "genre": "Drama",
                "poster": "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
                "plot": "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75."
            },
            {
                "title": "Toy Story",
                "year": 1995,
                "genre": "Animation",
                "poster": "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg",
                "plot": "A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom."
            },
            {
                "title": "Pulp Fiction",
                "year": 1994,
                "genre": "Crime",
                "poster": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
                "plot": "The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption."
            }
        ]

        # Add each movie to the database
        for movie_data in movies_data:
            movie = Movie(**movie_data)
            session.add(movie)

        # Save all changes
        session.commit()

    finally:
        session.close()


# ============================================================================
# CHALLENGE 1 - DONE FOR YOU!
# Load all movies from the database
# ============================================================================

def load_movies():
    """
    Load ALL movies from the database.

    CHALLENGE 1 - DONE FOR YOU!
    ---------------------------
    This shows you how to query data using SQLAlchemy.

    HOW IT WORKS:
    -------------
    1. Create a session (connection to database)
    2. Use session.query(Model).all() to get all rows
    3. Convert each Movie object to a dictionary
    4. Close the session
    5. Return the list of movies

    SQLALCHEMY QUERY METHODS:
    -------------------------
    - query(Model).all() - Get all rows
    - query(Model).first() - Get first row
    - query(Model).filter(...) - Filter rows
    - query(Model).count() - Count rows

    Returns:
        list: A list of all movie dictionaries
    """
    session = get_session()

    try:
        # Query all movies from the database
        movies = session.query(Movie).all()

        # Convert each Movie object to a dictionary
        return [movie.to_dict() for movie in movies]

    finally:
        # Always close the session when done
        session.close()


# ============================================================================
# CHALLENGE 2 - YOUR TURN!
# Find a single movie by its ID
# ============================================================================

def get_movie_by_id(movie_id):
    """
    Find a single movie by its ID.

    CHALLENGE 2 - YOUR TURN!
    ========================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Find and return ONE specific movie from the database.

    SQLALCHEMY METHODS YOU'LL USE:
    ------------------------------
    - session.query(Movie).filter(Movie.id == movie_id).first()

    This queries the Movie table, filters where id matches, and gets the first result.
    .first() returns None if no movie is found.

    STEP-BY-STEP HINTS:
    -------------------
    1. Create a session: session = get_session()
    2. Query the movie:
       movie = session.query(Movie).filter(Movie.id == movie_id).first()
    3. Check if movie exists: if movie is None: return None
    4. Convert to dictionary: result = movie.to_dict()
    5. Close session: session.close()
    6. Return the result

    IMPORTANT: Use try/finally to ensure session is closed!

    Args:
        movie_id (int): The ID of the movie to find

    Returns:
        dict: The movie dictionary if found, None if not found

    EXAMPLE:
    --------
    movie = get_movie_by_id(1)
    # Returns: {"id": 1, "title": "The Dark Knight", ...}

    movie = get_movie_by_id(999)
    # Returns: None (movie doesn't exist)
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Create a session
    # 2. Query the movie using filter
    # 3. Check if movie is None
    # 4. Convert to dictionary
    # 5. Close the session
    # 6. Return the result
    pass


# ============================================================================
# CHALLENGE 3 - YOUR TURN!
# Save a new review to the database
# ============================================================================

def add_review(movie_id, review):
    """
    Save a new review for a movie to the database.

    CHALLENGE 3 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Create a new Review object and add it to the database.

    THE REVIEW PARAMETER:
    ---------------------
    The 'review' parameter is a dictionary that looks like this:
    {
        "name": "John",
        "rating": 5,
        "comment": "Great movie!"
    }

    SQLALCHEMY METHODS YOU'LL USE:
    ------------------------------
    - session.add(object) - Add a new object to the session
    - session.commit() - Save all changes to the database

    STEP-BY-STEP HINTS:
    -------------------
    1. Create a session: session = get_session()
    2. Create a Review object:
       new_review = Review(
           movie_id=movie_id,
           reviewer_name=review["name"],
           rating=review["rating"],
           comment=review["comment"]
       )
    3. Add to session: session.add(new_review)
    4. Commit changes: session.commit()
    5. Close session

    Args:
        movie_id (int): The ID of the movie being reviewed
        review (dict): A dictionary with keys: "name", "rating", "comment"

    Returns:
        None (this function doesn't need to return anything)

    EXAMPLE:
    --------
    review = {"name": "Alice", "rating": 5, "comment": "Amazing!"}
    add_review(1, review)
    # This adds a new review for movie with id=1
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Create a session
    # 2. Create a Review object with the data
    # 3. Add it to the session
    # 4. Commit the changes
    # 5. Close the session
    pass


# ============================================================================
# CHALLENGE 4 - YOUR TURN!
# Calculate the average rating for a movie
# ============================================================================

def get_average_rating(movie_id):
    """
    Calculate the average star rating for a movie.

    CHALLENGE 4 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Calculate the average (mean) of all ratings for a movie.

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python (Recommended for beginners):
    1. Get the movie using get_movie_by_id()
    2. Get its reviews
    3. If no reviews, return 0
    4. Add up all the ratings
    5. Divide by the number of reviews
    6. Round to 1 decimal place

    METHOD 2 - Using SQLAlchemy (Advanced):
    from sqlalchemy import func
    avg = session.query(func.avg(Review.rating)).filter(Review.movie_id == movie_id).scalar()

    STEP-BY-STEP HINTS (Method 1):
    ------------------------------
    1. Get movie: movie = get_movie_by_id(movie_id)
    2. Check if movie exists: if movie is None: return 0
    3. Get reviews: reviews = movie.get("reviews", [])
    4. Check if empty: if len(reviews) == 0: return 0
    5. Calculate total:
       total = 0
       for review in reviews:
           total = total + review["rating"]
    6. Calculate average: average = total / len(reviews)
    7. Return rounded: return round(average, 1)

    Args:
        movie_id (int): The ID of the movie

    Returns:
        float: The average rating (0 if no reviews)

    EXAMPLE:
    --------
    # If movie 1 has reviews with ratings: 5, 4, 5
    get_average_rating(1)
    # Returns: 4.7 (which is (5+4+5)/3 = 14/3 = 4.666... rounded to 4.7)

    # If movie 2 has no reviews
    get_average_rating(2)
    # Returns: 0
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Get the movie using get_movie_by_id()
    # 2. Check if movie exists
    # 3. Get the reviews from the movie
    # 4. Check if there are no reviews (return 0)
    # 5. Add up all the ratings
    # 6. Divide by the number of reviews
    # 7. Round to 1 decimal place
    return 0


# ============================================================================
# CHALLENGE 5 - YOUR TURN!
# Search for movies by title
# ============================================================================

def search_movies(query):
    """
    Search for movies by title.

    CHALLENGE 5 - YOUR TURN!
    ========================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Search for movies where the title contains the search query.
    The search should be case-insensitive (ignore capitals).

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python (Recommended for beginners):
    1. If query is empty, return all movies
    2. Load all movies
    3. Filter movies where query is in the title (case-insensitive)

    METHOD 2 - Using SQLAlchemy (Advanced):
    movies = session.query(Movie).filter(Movie.title.ilike(f"%{query}%")).all()
    ilike() is case-insensitive LIKE

    STEP-BY-STEP HINTS (Method 1):
    ------------------------------
    1. Check if empty query: if query == "": return load_movies()
    2. Load all movies: movies = load_movies()
    3. Convert query to lowercase: query_lower = query.lower()
    4. Create results list: results = []
    5. Loop through movies:
       for movie in movies:
           if query_lower in movie["title"].lower():
               results.append(movie)
    6. Return results

    Args:
        query (str): The search term to look for in movie titles

    Returns:
        list: Movies that match the search (or all movies if query is empty)

    EXAMPLE:
    --------
    search_movies("dark")
    # Returns: [{"title": "The Dark Knight", ...}]

    search_movies("SPIDER")  # Case insensitive!
    # Returns: [{"title": "Spider-Man: Into the Spider-Verse", ...}]

    search_movies("")
    # Returns: all movies
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Handle empty query (return all movies)
    # 2. Make search case-insensitive using .lower()
    # 3. Check if query is IN the title
    # 4. Return matching movies
    return load_movies()


# ============================================================================
# CHALLENGE 6 - YOUR TURN!
# Get the top rated movies
# ============================================================================

def get_top_rated_movies(limit=5):
    """
    Get the top rated movies based on average review ratings.

    CHALLENGE 6 - YOUR TURN!
    ========================

    DIFFICULTY: Medium
    TIME: ~15 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Find movies that have reviews, sort them by rating (highest first),
    and return the top 'limit' movies.

    STEP-BY-STEP HINTS:
    -------------------
    1. Get all movies: movies = load_movies()
    2. Create empty list for rated movies: rated_movies = []
    3. Loop through movies:
       for movie in movies:
           rating = get_average_rating(movie["id"])
           if rating > 0:  # Only include movies WITH reviews
               movie["avg_rating"] = rating
               rated_movies.append(movie)
    4. Sort by rating (highest first):
       sorted_movies = sorted(rated_movies, key=lambda m: m["avg_rating"], reverse=True)

       WHAT IS LAMBDA?
       ---------------
       lambda is a mini function! "lambda m: m["avg_rating"]" means:
       "for each movie m, use its avg_rating value for sorting"

       reverse=True means highest to lowest (descending order)

    5. Return only the first 'limit' movies:
       return sorted_movies[:limit]

       The [:limit] is called "slicing" - it takes the first 'limit' items

    Args:
        limit (int): How many movies to return (default 5)

    Returns:
        list: The top rated movies, sorted from highest to lowest rating

    EXAMPLE:
    --------
    get_top_rated_movies(3)
    # Returns the 3 highest rated movies (only those with reviews)
    """
    # TODO: Write your code here!
    # Remember:
    # 1. Get all movies
    # 2. Calculate average rating for each
    # 3. Only include movies with reviews (rating > 0)
    # 4. Sort by rating (highest first)
    # 5. Return only the first 'limit' movies
    return []


# ============================================================================
# CHALLENGE 7 - YOUR TURN! (BONUS)
# Get movies by genre
# ============================================================================

def get_movies_by_genre(genre):
    """
    Get all movies that match a specific genre.

    CHALLENGE 7 - BONUS CHALLENGE!
    ==============================

    DIFFICULTY: Easy
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Filter movies to only show those matching the given genre.
    The search should be case-insensitive.

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python:
    1. Load all movies
    2. If genre is empty, return all movies
    3. Filter movies where genre matches

    METHOD 2 - Using SQLAlchemy:
    movies = session.query(Movie).filter(Movie.genre.ilike(genre)).all()

    Args:
        genre (str): The genre to filter by (e.g., "Action", "Drama")

    Returns:
        list: Movies that match the genre

    EXAMPLE:
    --------
    get_movies_by_genre("Action")
    # Returns: [{"title": "The Dark Knight", ...}, {"title": "Avengers: Endgame", ...}]
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return load_movies()


# ============================================================================
# CHALLENGE 8 - YOUR TURN! (BONUS)
# Count total reviews for a movie
# ============================================================================

def count_reviews(movie_id):
    """
    Count how many reviews a movie has.

    CHALLENGE 8 - BONUS CHALLENGE!
    ==============================

    DIFFICULTY: Easy
    TIME: ~5 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Return the number of reviews for a specific movie.

    TWO WAYS TO DO THIS:
    --------------------

    METHOD 1 - Using Python:
    movie = get_movie_by_id(movie_id)
    return len(movie["reviews"]) if movie else 0

    METHOD 2 - Using SQLAlchemy:
    count = session.query(Review).filter(Review.movie_id == movie_id).count()

    Args:
        movie_id (int): The ID of the movie

    Returns:
        int: The number of reviews for this movie

    EXAMPLE:
    --------
    count_reviews(1)
    # Returns: 3 (if movie 1 has 3 reviews)
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return 0


# ============================================================================
# CHALLENGE 9 - YOUR TURN! (BONUS - ADVANCED)
# Get all unique genres
# ============================================================================

def get_all_genres():
    """
    Get a list of all unique genres in the database.

    CHALLENGE 9 - BONUS CHALLENGE (ADVANCED)!
    =========================================

    DIFFICULTY: Medium
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Return a list of all different genres (no duplicates).

    METHOD 1 - Using Python:
    1. Load all movies
    2. Create an empty list for genres
    3. Loop through movies and collect unique genres
    4. Sort alphabetically

    METHOD 2 - Using SQLAlchemy:
    from sqlalchemy import distinct
    genres = session.query(distinct(Movie.genre)).all()

    Args:
        None

    Returns:
        list: A list of unique genre strings

    EXAMPLE:
    --------
    get_all_genres()
    # Returns: ["Action", "Animation", "Crime", "Drama", "Sci-Fi"]
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    return []


# ============================================================================
# CHALLENGE 10 - YOUR TURN! (BONUS - ADVANCED)
# Delete a review
# ============================================================================

def delete_review(review_id):
    """
    Delete a review from the database.

    CHALLENGE 10 - BONUS CHALLENGE (ADVANCED)!
    ==========================================

    DIFFICULTY: Medium
    TIME: ~10 minutes

    WHAT YOU NEED TO DO:
    --------------------
    Remove a review from the database using its ID.

    SQLALCHEMY METHODS YOU'LL USE:
    ------------------------------
    - session.query(Review).filter(Review.id == review_id).first()
    - session.delete(object)
    - session.commit()

    STEP-BY-STEP HINTS:
    -------------------
    1. Create a session
    2. Find the review: review = session.query(Review).filter(Review.id == review_id).first()
    3. Check if it exists: if review: session.delete(review)
    4. Commit changes: session.commit()
    5. Close session

    Args:
        review_id (int): The ID of the review to delete

    Returns:
        None

    EXAMPLE:
    --------
    delete_review(1)
    # Removes the review with id=1 from the database
    """
    # TODO: Write your code here!
    # This is a BONUS challenge - try it if you finish the others!
    pass


# ============================================================================
# INITIALIZATION - Run when the app starts
# ============================================================================

# This code runs automatically when this file is loaded
# It makes sure our database and tables exist before the app starts

# Create the tables (if they don't exist)
create_tables()

# Add initial movie data (if not already added)
seed_movies()
