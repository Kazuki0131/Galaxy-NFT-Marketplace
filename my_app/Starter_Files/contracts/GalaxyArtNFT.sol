// contracts/GameItem.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract GalaxyArtNFT is ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    address contractAddress;

    constructor(address marketAddress) ERC721("GalaxyArtNFT", "GAN") {
        contractAddress = marketAddress;
    }
    //create NFTs
    function createToken(address owner, string memory tokenURI)
        public
        returns (uint256)
    {
        _tokenIds.increment();
        uint256 newItemId = _tokenIds.current();
        _mint(owner, newItemId);
        _setTokenURI(newItemId, tokenURI);
        //set approval to allow other contract to transfer the NFTs
        setApprovalForAll(contractAddress, true);
        return newItemId;
    }
}

contract GalaxyArtMarket {
    using Counters for Counters.Counter;
    Counters.Counter private _itemIds;
    Counters.Counter private _itemsSold;

    address payable owner;

    constructor(){
        owner = payable(msg.sender);
    }
    //create a MarketItem struct to store the information of NFT (item ID, NFT contract address, toekn ID, ...)
    struct MarketItem{
        uint itemId;
        address nftContract;
        uint256 tokenId;
        address payable owner;
        address payable seller;
        uint256 price;
        bool sold;
    }

    mapping(uint256 => MarketItem) private idToMarketItem;

    function getMarketItem(uint256 marketItemId) public view returns (MarketItem memory) {
   
        return idToMarketItem[marketItemId];
        
    }

    
    function addMarketItem(address nftContract, uint256 tokenId, uint256 price) public returns (MarketItem memory) {
        require(price > 0, "Price must be biger than 0");
        _itemIds.increment();
        uint256 itemId = _itemIds.current();
        //store the NFT information into the marketplace struct (idTOMarketItem)
        idToMarketItem[itemId] =  MarketItem(
            itemId,
            nftContract,
            tokenId,
            payable(address(0)),
            payable(msg.sender),
            price,
            false
        );
        //transfer the onwership to this contract from seller
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);
        
        return idToMarketItem[itemId];
    }

    function createMarketSale(address nftContract, uint256 itemId) public payable returns(MarketItem memory){
        uint price = idToMarketItem[itemId].price;
        uint tokenId = idToMarketItem[itemId].tokenId;
        require(msg.value == price, "Please submit the asking price in order to complete the purchase");
        //transfer ether to seller
        idToMarketItem[itemId].seller.transfer(msg.value);
        //transfer the NFTS from this contract to buyer
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);
        idToMarketItem[itemId].owner = payable(msg.sender);
        idToMarketItem[itemId].seller = payable(address(0));
        //change the sold variable to true
        idToMarketItem[itemId].sold = true;
        _itemsSold.increment();

        return idToMarketItem[itemId];
    }

    function listMarketItems() public view returns (MarketItem[] memory) {
    //list available NFTs in the Marketplace
        uint itemCount = _itemIds.current();
        uint unsoldItemCount = _itemIds.current() - _itemsSold.current();
        uint currentIndex = 0;

        MarketItem[] memory items = new MarketItem[](unsoldItemCount);
        for (uint i = 0; i < itemCount; i++) {
            //check if NFT is available for sale
            if (idToMarketItem[i + 1].owner == address(0)) {
                uint currentId = i + 1;
                MarketItem storage currentItem = idToMarketItem[currentId];
                items[currentIndex] = currentItem;
                currentIndex += 1;
            }
        }
   
        return items;
    }

    function listMyNFTs() public view returns (MarketItem[] memory) {
    //list NFTs that user owns
        uint totalItemCount = _itemIds.current();
        uint itemCount = 0;
        uint currentIndex = 0;

        for (uint i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                itemCount += 1;
            }
        }

        MarketItem[] memory items = new MarketItem[](itemCount);
        for (uint i = 0; i < totalItemCount; i++) {
            if (idToMarketItem[i + 1].owner == msg.sender) {
                uint currentId = i + 1;
                MarketItem storage currentItem = idToMarketItem[currentId];
                items[currentIndex] = currentItem;
                currentIndex += 1;
            }
        }
    
        return items;
    }


}