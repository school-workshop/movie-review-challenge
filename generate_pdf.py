from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors

def create_solutions_pdf():
    doc = SimpleDocTemplate(
        "SOLUTIONS.pdf",
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        textColor=colors.darkblue
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=10,
        textColor=colors.darkblue
    )

    subheading_style = ParagraphStyle(
        'CustomSubheading',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=15,
        spaceAfter=8,
        textColor=colors.black
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=8,
        leading=14
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        backColor=colors.Color(0.95, 0.95, 0.95),
        leftIndent=10,
        rightIndent=10,
        spaceAfter=10,
        leading=12
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=4
    )

    story = []

    # Title
    story.append(Paragraph("Movie Review App - Database Solutions", title_style))
    story.append(Paragraph("Complete Solutions for All Challenges", body_style))
    story.append(Spacer(1, 30))

    # Challenge 2
    story.append(Paragraph("Challenge 2: Get Movie by ID (Easy)", heading_style))
    story.append(Paragraph("<b>Task:</b> Find and return ONE specific movie from the database.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code2 = """def get_movie_by_id(movie_id):
    session = get_session()
    try:
        movie = session.query(Movie).filter(Movie.id == movie_id).first()

        # Check if movie is None
        if movie is None:
            return None

        # Convert to dictionary and return
        return movie.to_dict()

    finally:
        session.close()"""
    story.append(Preformatted(code2, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Use filter(Movie.id == movie_id) to find the specific movie", bullet_style))
    story.append(Paragraph("• Use .first() to get one result (or None if not found)", bullet_style))
    story.append(Paragraph("• Always check if the result is None before calling .to_dict()", bullet_style))
    story.append(Paragraph("• Always close the session in the finally block", bullet_style))

    story.append(PageBreak())

    # Challenge 3
    story.append(Paragraph("Challenge 3: Add a Review (Medium)", heading_style))
    story.append(Paragraph("<b>Task:</b> Create a new Review object and add it to the database.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code3 = """def add_review(movie_id, review):
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
        session.close()"""
    story.append(Preformatted(code3, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph('• Access dictionary values using review["name"], review["rating"], review["comment"]', bullet_style))
    story.append(Paragraph("• Use session.add() to add the new object", bullet_style))
    story.append(Paragraph("• Use session.commit() to save changes to the database", bullet_style))
    story.append(Paragraph("• The movie_id parameter links the review to the correct movie", bullet_style))

    story.append(PageBreak())

    # Challenge 4
    story.append(Paragraph("Challenge 4: Get Average Rating (Medium)", heading_style))
    story.append(Paragraph("<b>Task:</b> Calculate the average (mean) of all ratings for a movie.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code4 = """def get_average_rating(movie_id):
    movie = get_movie_by_id(movie_id)

    if movie is None:
        return 0

    reviews = movie.get("reviews", [])

    if len(reviews) == 0:
        return 0

    # Add up all the ratings
    total = 0
    for review in reviews:
        total = total + review["rating"]

    # Divide by number of reviews
    average = total / len(reviews)

    # Round to 1 decimal place and return
    return round(average, 1)"""
    story.append(Preformatted(code4, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• First get the movie and check if it exists", bullet_style))
    story.append(Paragraph("• Get the reviews list from the movie dictionary", bullet_style))
    story.append(Paragraph("• Check if there are no reviews (return 0)", bullet_style))
    story.append(Paragraph("• Loop through reviews and add up all ratings", bullet_style))
    story.append(Paragraph("• Divide total by count to get average", bullet_style))
    story.append(Paragraph("• Use round(average, 1) to round to 1 decimal place", bullet_style))

    story.append(PageBreak())

    # Challenge 5
    story.append(Paragraph("Challenge 5: Search Movies (Easy)", heading_style))
    story.append(Paragraph("<b>Task:</b> Search for movies where the title contains the search query (case-insensitive).", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code5 = """def search_movies(query):
    # Handle empty queries
    if query == "":
        return load_movies()

    # Get all movies
    movies = load_movies()

    # Convert query to lowercase
    query_lower = query.lower()
    results = []

    # Check if query is in the title
    for movie in movies:
        if query_lower in movie["title"].lower():
            results.append(movie)

    return results"""
    story.append(Preformatted(code5, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Return all movies if query is empty", bullet_style))
    story.append(Paragraph("• Convert both query and title to lowercase for case-insensitive search", bullet_style))
    story.append(Paragraph("• Use 'in' operator to check if query is part of the title", bullet_style))
    story.append(Paragraph("• Build a results list with matching movies", bullet_style))

    story.append(PageBreak())

    # Challenge 6
    story.append(Paragraph("Challenge 6: Get Top Rated Movies (Medium)", heading_style))
    story.append(Paragraph("<b>Task:</b> Find movies with reviews, sort by rating (highest first), return top 'limit' movies.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code6 = """def get_top_rated_movies(limit=5):
    movies = load_movies()
    rated_movies = []

    # Populate rated_movies with movies that have reviews
    for movie in movies:
        rating = get_average_rating(movie["id"])
        if rating > 0:
            movie["avg_rating"] = rating
            rated_movies.append(movie)

    # Sort by rating, highest first
    sorted_movies = sorted(rated_movies,
                           key=lambda m: m["avg_rating"],
                           reverse=True)

    # Return only the top 'limit' movies
    return sorted_movies[:limit]"""
    story.append(Preformatted(code6, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Loop through all movies and calculate their average rating", bullet_style))
    story.append(Paragraph("• Only include movies with rating > 0 (meaning they have reviews)", bullet_style))
    story.append(Paragraph("• Add the avg_rating to each movie dictionary", bullet_style))
    story.append(Paragraph("• Use sorted() with lambda to sort by avg_rating", bullet_style))
    story.append(Paragraph("• Use reverse=True for highest to lowest", bullet_style))
    story.append(Paragraph("• Use slicing [:limit] to get only the first 'limit' movies", bullet_style))

    story.append(PageBreak())

    # Challenge 7
    story.append(Paragraph("Challenge 7: Get Movies by Genre (Bonus - Easy)", heading_style))
    story.append(Paragraph("<b>Task:</b> Filter movies to show only those matching the given genre (case-insensitive).", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code7 = """def get_movies_by_genre(genre):
    movies = load_movies()

    # Handle empty genre
    if genre == "":
        return movies

    # Convert genre to lowercase for comparison
    genre_lower = genre.lower()
    results = []

    # Check each film for matching genre
    for movie in movies:
        if movie["genre"].lower() == genre_lower:
            results.append(movie)

    return results"""
    story.append(Preformatted(code7, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Return all movies if genre is empty", bullet_style))
    story.append(Paragraph("• Convert both input genre and movie genre to lowercase", bullet_style))
    story.append(Paragraph("• Use == for exact match (not 'in')", bullet_style))

    story.append(PageBreak())

    # Challenge 8
    story.append(Paragraph("Challenge 8: Count Reviews (Bonus - Easy)", heading_style))
    story.append(Paragraph("<b>Task:</b> Return the number of reviews for a specific movie.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code8 = """def count_reviews(movie_id):
    movie = get_movie_by_id(movie_id)

    if movie is None:
        return 0

    return len(movie.get("reviews", []))"""
    story.append(Preformatted(code8, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Get the movie first", bullet_style))
    story.append(Paragraph("• Check if movie exists (return 0 if not)", bullet_style))
    story.append(Paragraph("• Use len() to count the reviews list", bullet_style))
    story.append(Paragraph('• Use .get("reviews", []) to safely get reviews (empty list if none)', bullet_style))

    story.append(Spacer(1, 30))

    # Challenge 9
    story.append(Paragraph("Challenge 9: Get All Genres (Bonus - Medium)", heading_style))
    story.append(Paragraph("<b>Task:</b> Return a list of all unique genres (no duplicates), sorted alphabetically.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code9 = """def get_all_genres():
    movies = load_movies()
    genres = []

    for movie in movies:
        genre = movie["genre"]
        if genre not in genres:
            genres.append(genre)

    # Sort alphabetically
    genres.sort()
    return genres"""
    story.append(Preformatted(code9, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Create an empty list to store unique genres", bullet_style))
    story.append(Paragraph("• Loop through movies and check if genre already exists", bullet_style))
    story.append(Paragraph("• Only add genre if it's not already in the list", bullet_style))
    story.append(Paragraph("• Sort the list alphabetically before returning", bullet_style))

    story.append(PageBreak())

    # Challenge 10
    story.append(Paragraph("Challenge 10: Delete a Review (Bonus - Medium)", heading_style))
    story.append(Paragraph("<b>Task:</b> Remove a review from the database using its ID.", body_style))
    story.append(Paragraph("<b>Solution:</b>", subheading_style))

    code10 = """def delete_review(review_id):
    session = get_session()
    try:
        review = session.query(Review).filter(Review.id == review_id).first()
        if review:
            session.delete(review)
            session.commit()
    finally:
        session.close()"""
    story.append(Preformatted(code10, code_style))

    story.append(Paragraph("<b>Key Points:</b>", subheading_style))
    story.append(Paragraph("• Create a session", bullet_style))
    story.append(Paragraph("• Find the review using filter() and .first()", bullet_style))
    story.append(Paragraph("• Check if review exists before deleting", bullet_style))
    story.append(Paragraph("• Use session.delete() to remove the object", bullet_style))
    story.append(Paragraph("• Use session.commit() to save the deletion", bullet_style))
    story.append(Paragraph("• Always close session in finally block", bullet_style))

    story.append(PageBreak())

    # Quick Reference
    story.append(Paragraph("Quick Reference Card", heading_style))
    story.append(Spacer(1, 10))

    refs = [
        ("<b>Challenge 2 (Get by ID):</b> movie.to_dict() if movie else None", body_style),
        ('<b>Challenge 3 (Add Review):</b> review["name"], review["rating"], review["comment"]', body_style),
        ("<b>Challenge 4 (Average):</b> total / len(reviews), round(avg, 1)", body_style),
        ("<b>Challenge 5 (Search):</b> query.lower() in title.lower()", body_style),
        ('<b>Challenge 6 (Top Rated):</b> sorted(..., key=lambda m: m["avg_rating"], reverse=True)[:limit]', body_style),
        ('<b>Challenge 7 (By Genre):</b> movie["genre"].lower() == genre.lower()', body_style),
        ('<b>Challenge 8 (Count):</b> len(movie.get("reviews", []))', body_style),
        ("<b>Challenge 9 (All Genres):</b> if genre not in genres: genres.append(genre)", body_style),
        ("<b>Challenge 10 (Delete):</b> session.delete(review), session.commit()", body_style),
    ]

    for text, style in refs:
        story.append(Paragraph(text, style))
        story.append(Spacer(1, 8))

    doc.build(story)
    print("PDF created successfully: SOLUTIONS.pdf")

if __name__ == "__main__":
    create_solutions_pdf()
