# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Home")
    st.sidebar.markdown("# Home")

def page2():
    st.markdown("# Register Your NFT")
    st.sidebar.markdown("# Register Your NFT")

def page3():
    st.markdown("# Sell Your NFT ")
    st.sidebar.markdown("# Sell Your NFT")

st.markdown("# Home")
st.sidebar.markdown("# Home")

#page_names_to_funcs = {
    #"Home": main_page,
    #"Register Your NFT": page2,
    #"Sell Your NFT": page3,
#}

#selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
#page_names_to_funcs[selected_page]()