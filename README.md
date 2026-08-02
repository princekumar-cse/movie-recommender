# 🎬 Movie Recommendation System — Streamlit App

Part of the **AI Playground: 4 Real-World AI Projects** series.

Pick a movie you liked, and this app recommends similar ones using a
**content-based recommender**: TF-IDF (same technique as Project 1)
plus **cosine similarity**, comparing movie descriptions — not user
behavior or ratings.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Files

- `app.py` — Streamlit UI (movie picker, recommendation display)
- `model.py` — builds the TF-IDF + similarity matrix, recommendation logic
- `data.py` — the 12-movie dataset with keyword descriptions
- `requirements.txt` — dependencies

## Deploy on Streamlit Community Cloud

1. Push this folder to its own GitHub repo (e.g. `movie-recommender`).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Pick the repo/branch, set **Main file path** to `app.py`.
4. Deploy.
