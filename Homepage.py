import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="HomePage",
    page_icon="👋",
    menu_items={
        'Get Help': 'https://www.fanniemae.com/about-us/contact-us',
        'About': "https://www.fanniemae.com/about-us"
    }
)

logoUrl = 'https://www.fanniemae.com/sites/g/files/koqyhd191/files/2020-10/fannie-mae-logo-dark-blue.png'
st.image(logoUrl, width=500)

st.title("Welcome to ReadySetHome!")
st.header("\"Your Future, Your Home, Our Priority\"")

st.sidebar.success("Select a page above.")

people = "https://www.fanniemae.com/sites/g/files/koqyhd191/files/styles/16_9_letterbox/public/2023-07/lafm-stories-hero-image.jpg?h=acac93ba&itok=s_gjMgh8"
st.image(people, width=800)