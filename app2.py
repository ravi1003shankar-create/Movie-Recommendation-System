import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

# Load the movies dataset
with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)

# Load the similarity matrix correctly without 'rb'
cs = joblib.load("cs.joblib")

def recommend(name_movie):
    # Fixed: Uses name_movie to match the function argument
    # Fixed: Simplified indexing to accurately get the single row location
    movie_index = movies[movies['title'] == name_movie].index[0]
    
    recommendations = cs[movie_index]
    
    movie_list = sorted(enumerate(recommendations), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies

# Fixed: Stored titles in a new variable so the 'movies' DataFrame stays intact
movie_titles = movies['title'].values

# Fixed: Uses movie_titles instead of overwriting 'movies'
name_movie = st.selectbox("Enter the Movie Name", movie_titles)

if st.button("Recommend"):
    r = recommend(name_movie)
    st.write("The Recommended Movies are :")
    
    for i in r:
        st.write(i)
