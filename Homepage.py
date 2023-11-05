import streamlit as st

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

st.title("Homepage")
st.sidebar.success("Select a page above.")

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""


my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)