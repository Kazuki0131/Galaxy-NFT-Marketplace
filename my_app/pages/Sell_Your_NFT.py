import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.markdown("# Sell Your NFT")
st.sidebar.markdown("# Sell Your NFT")


# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

abi_file_list = ['./Starter_Files/contracts/compiled/GalaxyArtNFT_abi.json','./Starter_Files/contracts/compiled/GalaxyArtMarket_abi.json']
contract_address_list = ["GALAXY_ART_NFT_ADDRESS", "GALAXY_ART_MARKET_ADDRESS"]


@st.cache(allow_output_mutation=True)

def load_contract(abi_file, contract_address):

    # Load the contract ABI
    with open(Path(abi_file)) as f:
        galaxy_art_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv(contract_address)

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=galaxy_art_abi
    )

    return contract


# Load the contract (GalaxyArtMarket contract)
contract_2 = load_contract(abi_file_list[1],contract_address_list[1])



################################################################################
# Sell Your Artwork
################################################################################
st.title("Sell Your NFT")
account = st.text_input("Enter your wallet address")

token_id = st.text_input("What's your token ID?")

price = st.text_input("How much ETH do you wish to list your NFT for? Enter the price in Wei.")


if st.button("Sell"):
    # Get the art token's URI
    contract_address = os.getenv(contract_address_list[0])
    st.write(contract_address)
    #Get the NFT information
    NFT_info = contract_2.functions.addMarketItem(str(contract_address), int(token_id), int(price)).call({'from': account})
    
    #add NFT into marketplace
    contract_2.functions.addMarketItem(str(contract_address), int(token_id), int(price)).transact({'from': account, 'gas': 1000000})
    
    #show the Item ID
    st.write(f"Item ID: {NFT_info[0]}")
    
st.markdown("---")
st.markdown("### Get NFT information")
marketItem = st.text_input("What's your Item ID?")

if st.button("get MarketItem"):
    #call getMarketItem function to check the information of the selected MarketItem
    #The function will return a tuple (# NFT info: itemId, nftContract address, tokenId, owner address, seller address price, bool sold)
    marketItem_info = contract_2.functions.getMarketItem(int(marketItem)).call()
    # NFT info: 00. itemId, 01. nftContract, 02. tokenId; 03. owner; 04. seller; 05. price; 06. sold;
    st.markdown("#### NFT information:")
    st.write(f"Item ID:       {marketItem_info[0]}")
    st.write(f"NFT contract:  {marketItem_info[1]}")
    st.write(f"Token ID:      {marketItem_info[2]}")
    st.write(f"Seller:        {marketItem_info[4]}")
    st.write(f"Price:         {marketItem_info[5]}")