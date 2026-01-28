"""
Script to load TMDB movie data from Hugging Face datasets into the SQLite database.

Usage:
    python load_tmdb_data.py [--limit N]

Options:
    --limit N   Only load the first N movies (default: load all ~9800 movies)
"""

from datasets import load_dataset
from database import get_session, Movie, create_tables
import argparse


def extract_year(release_date):
    """Extract year from release date string like '2021-12-15'."""
    if not release_date or release_date == "":
        return None
    try:
        return int(release_date.split("-")[0])
    except (ValueError, IndexError):
        return None


def get_primary_genre(genre_string):
    """Get the first/primary genre from a comma-separated genre string."""
    if not genre_string or genre_string == "":
        return "Unknown"
    # Take the first genre if multiple are listed
    return genre_string.split(",")[0].strip()


def load_tmdb_movies(limit=None):
    """
    Load movies from the TMDB dataset into the database.

    Args:
        limit: Maximum number of movies to load. None means load all.
    """
    print("Loading TMDB dataset from Hugging Face...")
    dataset = load_dataset("Pablinho/movies-dataset")

    session = get_session()

    try:
        # Clear existing movies
        existing_count = session.query(Movie).count()
        if existing_count > 0:
            print(f"Clearing {existing_count} existing movies...")
            session.query(Movie).delete()
            session.commit()

        movies_data = dataset["train"]
        total = len(movies_data) if limit is None else min(limit, len(movies_data))

        print(f"Loading {total} movies into database...")

        loaded = 0
        skipped = 0

        for i, record in enumerate(movies_data):
            if limit and i >= limit:
                break

            # Extract and validate data (handle None values)
            title = (record.get("Title") or "").strip()
            year = extract_year(record.get("Release_Date") or "")
            genre = get_primary_genre(record.get("Genre") or "")
            poster = record.get("Poster_Url") or ""
            plot = (record.get("Overview") or "").strip()

            # Skip if missing required fields
            if not title or not year or not plot:
                skipped += 1
                continue

            # Create movie object
            movie = Movie(
                title=title,
                year=year,
                genre=genre,
                poster=poster if poster else "https://via.placeholder.com/300x450?text=No+Poster",
                plot=plot
            )
            session.add(movie)
            loaded += 1

            # Commit in batches for performance
            if loaded % 500 == 0:
                session.commit()
                print(f"  Loaded {loaded} movies...")

        # Final commit
        session.commit()
        print(f"\nDone! Loaded {loaded} movies ({skipped} skipped due to missing data)")

    finally:
        session.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load TMDB movies into the database")
    parser.add_argument("--limit", type=int, default=None,
                        help="Maximum number of movies to load (default: all)")
    args = parser.parse_args()

    # Ensure tables exist
    create_tables()

    # Load movies
    load_tmdb_movies(limit=args.limit)
