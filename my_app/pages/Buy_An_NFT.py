import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.markdown("# Buy NFT")
st.sidebar.markdown("# Buy NFT")


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


# Load the contract
contract_1 = load_contract(abi_file_list[0],contract_address_list[0])
contract_2 = load_contract(abi_file_list[1],contract_address_list[1])



################################################################################
# List NFTs
################################################################################
NFTs_info = contract_2.functions.listMarketItems().call()

 # NFT info: 00. itemId, 01. nftContract, 02. tokenId; 03. owner; 04. seller; 05. price; 06. sold;
token_uri = contract_1.functions.tokenURI(NFTs_info[0][2]).call()
#st.write(token_uri)
st.image(token_uri)
st.write("Item ID:")
st.write(NFTs_info[0][0])
st.write("Price:")
st.write(NFTs_info[0][5])