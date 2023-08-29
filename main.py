import streamlit as st
import pandas as pd

data = {
    "Fruit": ["I Pathan","Yusuf Pathan","Sam Curran","Sam Billings","Tom Curran","Tommy h"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Purple", "Purple"]
}

df = pd.DataFrame(data)

selection = st.selectbox("Select an option:", df["Fruit"], key="dropdown")

if selection:
    filtered_df = df[df["Fruit"] == selection]

    st.write("Filtered Data:")
    st.write(filtered_df)
