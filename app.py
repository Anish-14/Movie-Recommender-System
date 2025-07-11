import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("movie recommender system")

selected_movie_name = st.selectbox(
    "Movie recommender system",
    movies['title'].values
)


if st.button("Recommend"):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)

