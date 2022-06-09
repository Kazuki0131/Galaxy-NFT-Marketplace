# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# Home")
    st.sidebar.markdown("# Home")

def page2():
    st.markdown("# Register Your NFT")
    st.sidebar.markdown("# Register Your NFT")

def page3():
    st.markdown("# Sell Your NFT")
    st.sidebar.markdown("# Sell Your NFT")

def page4():
    st.markdown("# Buy An NFT")
    st.sidebar.markdown("# Buy An NFT")

def page5():
    st.markdown("# Your NFT Collection")
    st.sidebar.markdown("# Your NFT Collection")

st.markdown("# Home")
st.sidebar.markdown("# Home")

st.title("Galaxy NFT Marketplace")

from PIL import Image
image = Image.open('./Images/galaxy.jpeg')

st.image(image, caption='Galaxy NFT Marketplace')

st.markdown("# Welcome to Galaxy NFT Marketplace, your one-stop shop for all of your non-fungible token needs!")

st.markdown("### Galaxy NFT Marketplace aims to make the entire NFT process simple and fun! From the beginning minting process, to listing and selling your NFT, and also exploring the marketplace and buying other popular NFTs, Galaxy NFT Marketplace is your one-stop shop!")
 ###