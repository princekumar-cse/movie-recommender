"""
AI Playground — Project 4: Movie Recommendation System
Streamlit app version.

Run locally:
    streamlit run app.py
"""

import streamlit as st

from model import build_recommender, recommend_movies

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered",
)


@st.cache_resource(show_spinner="Building the similarity matrix...")
def get_recommender():
    return build_recommender()


movies, similarity_matrix = get_recommender()

st.title("🎬 Movie Recommendation System")
st.caption("Content-based filtering: TF-IDF + cosine similarity, no user data needed.")

with st.expander("How this works"):
    st.markdown(
        """
        This is a **content-based** recommender — it suggests movies
        purely by comparing text descriptions, not by studying what
        other users watched.

        1. Every movie's description is converted to numbers with
           **TF-IDF** (same technique as Project 1).
        2. **Cosine similarity** compares every movie's numbers
           against every other movie's, producing a score from 0
           (unrelated) to 1 (identical) for every pair.
        3. To recommend, we just look up the row for your chosen
           movie and return the highest-scoring others.

        Nothing here was hard-coded like *"if you liked X, suggest Y"*
        — every suggestion comes purely from shared keywords in the
        descriptions.
        """
    )

st.subheader("Pick a movie")
selected_movie = st.selectbox("You liked:", movies["title"].tolist())
num_recs = st.slider("Number of recommendations", 1, 8, 5)

if st.button("Get Recommendations", type="primary"):
    result = recommend_movies(movies, similarity_matrix, selected_movie, num_recs)
    st.subheader(f"Because you liked {selected_movie}")
    st.dataframe(result, use_container_width=True, hide_index=True)

with st.expander("See the full movie catalog"):
    st.dataframe(movies, use_container_width=True, hide_index=True)

st.caption("Part of the AI Playground: 4 Real-World AI Projects series.")
