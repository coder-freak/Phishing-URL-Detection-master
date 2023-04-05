import streamlit as st
from streamlit.components.v1 import html

# Load the HTML file contents
with open("templates/index.html", "r") as f:
    html_code = f.read()

# Render the HTML code in Streamlit
html(html_code)
