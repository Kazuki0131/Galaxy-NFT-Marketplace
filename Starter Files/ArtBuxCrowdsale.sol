pragma solidity ^0.5.0;

import "./ArtBuxMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract ArtBuxCoinCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        ArtBuxCoin token
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor body can stay empty
    }
}

contract ArtBuxCoinCrowdsaleDeployer {
    address public artbuxcoin_address;
    address public artbuxcoin_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        ArtBuxCoin token = new ArtBuxCoin(name, symbol, 0);
        artbuxcoin_address = address(token);

        ArtBuxCoinCrowdsale artbuxcoin_crowdsale = new ArtBuxCoinCrowdsale(1, wallet, token);
        artbuxcoin_crowdsale_address = address(arcade_crowdsale);

        token.addMinter(artbuxcoin_crowdsale_address);
        token.renounceMinter();
    }
}
