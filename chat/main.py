import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Chatbot",
    page_icon="👋",
)

st.write("# Welcome to my chatbot!")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This is my first chatbot. I hope you like it!
"""
)

st.image(Image.open("123.jpg"))