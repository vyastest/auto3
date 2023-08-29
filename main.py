import streamlit as st
import pandas as pd

data = {
    "Fruit": ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon", "Mango", "Orange"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Purple", "Purple", "Brown", "Yellow", "Orange", "Orange"]
}

df = pd.DataFrame(data)

selection = st.selectbox("Select an option:", df["Fruit"], key="dropdown")

if selection:
    filtered_df = df[df["Fruit"] == selection]

    st.write("Filtered Data:")
    st.write(filtered_df)
