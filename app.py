import streamlit as st

st.set_page_config(
    page_title="My Streamlit Site",
    page_icon="📊",
    layout="wide"
)

st.title(" Welcome to My Streamlit Site")
st.markdown(
    """
    This is a two-page Streamlit app:
    - **EDA_Gallery**:  

    Use the left sidebar to switch pages.
    """
)


st.caption("Built with Streamlit • Class template")
