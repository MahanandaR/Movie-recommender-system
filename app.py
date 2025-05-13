import streamlit as st
import pandas as pd
import pickle
import requests
import gdown


# Correct file ID and URL
file_id = '1TVj8UQ1s5RreSa9AOMGBFtYh98BtfuSC'
gdown.download(f'https://drive.google.com/uc?id={file_id}', 'similarity.pkl', quiet=False)

with open('similarity.pkl','rb') as file:
    similarity = pickle.load(file)

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0e320801c4cc2c20a5c77ae03b3514e1&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    names = []
    posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters


# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie to get recommendations:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Creating 5 columns for displaying the movie recommendations
    cols = st.columns(5)

    for idx in range(5):
        with cols[idx]:
            st.image(posters[idx], use_container_width=True)  # Display image using full container width
            # Truncate movie title if it's too long and display it centered
            short_title = names[idx][:25] + "..." if len(names[idx]) > 25 else names[idx]
            st.markdown(f"<p style='text-align:center; font-size:14px'>{short_title}</p>", unsafe_allow_html=True)
