# Movie Review App Challenge

Build a movie review web application using **Python**, **FastAPI**, and **SQLAlchemy**!

## What You'll Build

- Browse **9,800+ real movies** from TMDB (The Movie Database)
- Click to view movie details
- Submit reviews with star ratings (1-5)
- See average ratings calculated from reviews
- Search movies by title
- View Top 5 highest-rated movies

## Getting Started

### 1. Clone this repository

```bash
git clone https://github.com/school-workshop/movie-review-challenge.git
cd movie-review-challenge
```

### 2. Create a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
uvicorn main:app --reload
```

### 5. Open in browser

Go to: **http://127.0.0.1:8000**

## The Challenges

Open `database.py` and complete the `TODO` challenges!

| Challenge | Function | Difficulty |
|-----------|----------|------------|
| 1 | `load_movies()` | Done for you |
| 2 | `get_movie_by_id()` | Easy |
| 3 | `add_review()` | Medium |
| 4 | `get_average_rating()` | Medium |
| 5 | `search_movies()` | Easy |
| 6 | `get_top_rated_movies()` | Medium |
| 7 | `get_movies_by_genre()` | Bonus |
| 8 | `count_reviews()` | Bonus |
| 9 | `get_all_genres()` | Bonus |
| 10 | `delete_review()` | Bonus |

See **STUDENT_CHALLENGES.md** for detailed instructions and hints!

## Deploy Your App (Optional)

Want to share your app with friends? Deploy it for free on Render!

1. Go to [render.com](https://render.com) and sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Connect this repository
4. Configure:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**

Your app will be live at `https://your-app-name.onrender.com`!

## Need Help?

- Check the hints in `STUDENT_CHALLENGES.md`
- New to Git? Read our **[GIT_GUIDE.md](GIT_GUIDE.md)** for beginners
- Ask a mentor for guidance
- Look at the example code in `load_movies()` function

Good luck and have fun!
