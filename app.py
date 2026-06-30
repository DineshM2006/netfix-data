import streamlit as st
import pickle
import pandas as pd

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Netflix Prediction")

show_id = st.text_input("Show ID")
type_ = st.text_input("Type")
title = st.text_input("Title")
cast = st.text_input("Cast")
rating = st.text_input("Rating")
duration = st.text_input("Duration")
listed_in = st.text_input("Listed In")
description = st.text_area("Description")
release_date = st.number_input("Release Date", value=1)

if st.button("Predict"):

    data = pd.DataFrame({
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

    data = pd.get_dummies(data)

    try:
        prediction = model.predict(data)
        st.success(f"Prediction: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")