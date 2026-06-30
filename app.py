import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Netflix Release Year Prediction")

show_id = st.text_input("Show ID")
type_ = st.selectbox("Type", ["Movie", "TV Show"])
title = st.text_input("Title")
cast = st.text_input("Cast")
rating = st.text_input("Rating")
duration = st.text_input("Duration")
listed_in = st.text_input("Genre")
description = st.text_area("Description")
release_date = st.number_input("Release Date", min_value=0, value=1)

if st.button("Predict"):
    df = pd.DataFrame({
        "show_id": [show_id],
        "type": [type_],
        "title": [title],
        "cast": [cast],
        "rating": [rating],
        "duration": [duration],
        "listed_in": [listed_in],
        "description": [description],
        "release_date": [release_date]
    })

    prediction = model.predict(df)
    st.success(f"Predicted Release Year: {prediction[0]}")
