"""
Movie dataset for Project 4.
12 movies, each with a short keyword-style description covering
genre, themes, and setting — this is what the system compares.
"""

import pandas as pd


def build_movies_dataframe() -> pd.DataFrame:
    return pd.DataFrame({
        "title": [
            "Interstellar", "Inception", "The Martian", "Arrival",
            "The Matrix", "Avatar", "Titanic", "The Notebook",
            "Avengers: Endgame", "Iron Man", "Jurassic Park", "The Dark Knight",
        ],
        "description": [
            "space science fiction astronauts future adventure",
            "science fiction dreams technology thriller mind bending",
            "space science fiction astronaut survival mars adventure",
            "science fiction aliens language space mystery",
            "science fiction technology artificial intelligence action",
            "science fiction space aliens adventure fantasy",
            "romance drama ship ocean historical tragedy",
            "romance relationship love drama emotional",
            "superhero action marvel time travel adventure",
            "superhero action technology marvel engineering",
            "dinosaurs science adventure action island",
            "superhero action crime batman thriller",
        ],
    })
