EchoWatch is a beautiful and intuitive movie recommendation system built with Streamlit, using cosine similarity to suggest movies similar to your favorite ones. 
It fetches movie posters via TMDb API and supports dynamic styling with custom HTML/CSS.

Features:
----------------
1.Recommend top 5 similar movies based on your selection.
2.Movie posters fetched live via TMDb API.
3.Elegant UI with custom background, overlay, and themed styling.
4.Clickable movie links redirecting to TMDb movie pages.

Tech Stack
----------------
Frontend: Streamlit, HTML, CSS
Backend: Python, Pandas, Pickle, Requests
Data: Precomputed similarity matrix (similarity.pkl) and movie metadata (movies_dict.pkl)
External API: TMDb (The Movie Database)

