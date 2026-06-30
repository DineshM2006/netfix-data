import streamlit as st
import pandas as pd
import joblib

# Load model
rf = joblib.load("netflix_rating_model.pkl")

st.title("Netflix Rating Prediction")

type_ = st.selectbox("Type", ["Movie", "TV Show"])
title = st.text_input("Title")
director = st.text_input("Director")
cast = st.text_input("Cast")
country = st.text_input("Country")
release_year = st.number_input("Release Year", 1900, 2035, 2020)
duration = st.text_input("Duration")
listed_in = st.text_input("Genre")
description = st.text_area("Description")

if st.button("Predict Rating"):

    input_data = pd.DataFrame({
        "type": [type_],
        "title": [title],
        "director": [director],
        "cast": [cast],
        "country": [country],
        "release_year": [release_year],
        "duration": [duration],
        "listed_in": [listed_in],
        "description": [description]
    })

    prediction = rf.predict(input_data)

    st.success(f"Predicted Rating: {prediction[0]}")