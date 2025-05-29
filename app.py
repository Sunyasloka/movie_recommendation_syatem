
import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_ind = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_ind]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

with open('movies.pkl', 'rb') as f:
    similarity = pickle.load(f)

with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)



movies = pd.DataFrame(movies_dict)

st.title("Movie Recommended System")
selected_movie = st.selectbox (
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:
        st.write(i)
