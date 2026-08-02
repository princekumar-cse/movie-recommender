"""
Content-based recommendation logic for Project 4.
Same technique as Project 1 (TF-IDF), but used to measure
*similarity* between movies instead of classifying text.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data import build_movies_dataframe


def build_recommender():
    """
    Builds the TF-IDF matrix and the movie-to-movie similarity matrix.
    Returns (movies_df, similarity_matrix).
    """
    movies = build_movies_dataframe()

    vectorizer = TfidfVectorizer(stop_words="english")
    movie_matrix = vectorizer.fit_transform(movies["description"])

    similarity_matrix = cosine_similarity(movie_matrix)

    return movies, similarity_matrix


def recommend_movies(movies: pd.DataFrame, similarity_matrix, movie_title: str, number_of_recommendations: int = 5):
    """Returns a DataFrame of the most similar movies to movie_title."""
    if movie_title not in movies["title"].values:
        return None

    movie_index = movies.index[movies["title"] == movie_title][0]

    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = [item for item in similarity_scores if item[0] != movie_index]

    recommendations = []
    for index, score in similarity_scores[:number_of_recommendations]:
        recommendations.append({
            "movie": movies.iloc[index]["title"],
            "similarity": round(float(score), 3),
        })

    return pd.DataFrame(recommendations)
