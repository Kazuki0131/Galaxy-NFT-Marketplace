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
#st.write(len(NFTs_info))

item_counter = 0

st.title("NFT Market")

 # NFT info: 00. itemId, 01. nftContract, 02. tokenId; 03. owner; 04. seller; 05. price; 06. sold;

while item_counter < len(NFTs_info):
    cols = st.columns(2)
    if NFTs_info[item_counter][6] == True:
        item_counter += 1
    else:
        cols[0].image(contract_1.functions.tokenURI(NFTs_info[item_counter][2]).call(), use_column_width="always")
        cols[0].write("Item ID")
        cols[0].write(NFTs_info[item_counter][0])
        cols[0].write("Price")
        cols[0].write(NFTs_info[item_counter][5])
        item_counter += 1
        if item_counter < len(NFTs_info):
            if NFTs_info[item_counter][6] == True:
                item_counter += 1
            else:
                cols[1].image(contract_1.functions.tokenURI(NFTs_info[item_counter][2]).call(),use_column_width="always")
                cols[1].write("Item ID")
                cols[1].write(NFTs_info[item_counter][0])
                cols[1].write("Price")
                cols[1].write(NFTs_info[item_counter][5])
                item_counter += 1
        else:
            break
st.markdown("---")

################################################################################
# Purchase NFT
################################################################################
NFT_contract_address = os.getenv(contract_address_list[0])

st.title("Buy NFT")
account = st.text_input("Enter your wallet address")
item_id = st.text_input("What's your item ID?")
price = st.text_input("The price:")

if st.button("Buy"):
    contract_2.functions.createMarketSale(str(NFT_contract_address), int(item_id)).transact({'from':account, 'gas':1000000, 'value': int(price)})
    st.write("Your transaction is complete!")