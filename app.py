import streamlit as st
from predict_page import show_predict_page

st.selectbox("explore or predict", ("explore", "predict"))


show_predict_page