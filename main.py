import streamlit as st
import pandas as pd

data = {
    "Fruit": ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi", "Lemon", "Mango", "Orange"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Purple", "Purple", "Brown", "Yellow", "Orange", "Orange"]
}

df = pd.DataFrame(data)

input_text = st.text_input("Type to filter options:")
filtered_options = [option for option in df["Fruit"] if input_text.lower() in option.lower()]
selected_option = st.selectbox("Select an option:", filtered_options)

filtered_df = df[df["Fruit"] == selected_option]

st.write("Filtered Data:")
st.write(filtered_df)
