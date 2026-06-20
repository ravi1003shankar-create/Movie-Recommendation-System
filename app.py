import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with open("movies.pickle","rb") as m:
    movies=pickle.load(m)

cs=joblib.load("cs.joblib")

def recommend(name_movie):
    movie_index=movies[movies['title']==name_movie].index[0]  # never pass this under inverted commas

    recommendations=cs[movie_index]

    movie_list=sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies

movie_names=movies['title'].values

name_movie=st.selectbox("Enter the Movie Name",movie_names)

if st.button("Recommend"):
    r=recommend(name_movie)
    st.write("The Recommended Movies are : ")

    for i in r:
        st.write(i)
        