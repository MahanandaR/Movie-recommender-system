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

Working:
--------
* The dataset contains metadata for each movie including keywords, genres, cast, crew and overview.
![image](https://github.com/user-attachments/assets/2b7d645e-4e28-48ed-9e0d-d62fa8745f49)

* All these features are combined into a new column called tags to create a unified representation of each movie.
![image](https://github.com/user-attachments/assets/7561c603-0b27-4021-9277-41157086d980)

* Text preprocessing is applied to the tags column :
  All text is converted to lowercase (e.g., "Action, Thriller" becomes "action, thriller").
  Spaces between words are removed (e.g., "action movie" becomes "actionmovie").
  Stemming is performed using PorterStemmer to reduce words to their root form.
  ![image](https://github.com/user-attachments/assets/585acdc3-9da4-4668-aeb1-dcc9a23166f9)

* CountVectorizer is used to convert the tags column into numerical feature vectors.
    Cosine similarity is used to calculate similarity between the vector representations of all the movies.
    The resulting similarity matrix is serialized and saved as a .pkl file for efficient loading during recommendation.
    A Streamlit web application is built to provide an interactive interface for movie selection and recommendation :
    User select a movie from the dropdown list.
    The system recommends top 5 most similar movies based on the similarity score.
    Movie posters are fetched using the TMDB API to enhance the visual appeal of the recommendations.
  
  ![image](https://github.com/user-attachments/assets/514f9fc7-ecb0-422b-8d21-1817d32dae6e)

