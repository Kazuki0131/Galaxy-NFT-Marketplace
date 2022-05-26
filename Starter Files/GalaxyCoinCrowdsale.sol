pragma solidity ^0.5.0;

import "./GalaxyCoinMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract GalaxyCoinCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        GalaxyCoin token
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor body can stay empty
    }
}

contract GalaxyCoinCrowdsaleDeployer {
    address public galaxycoin_address;
    address public galaxycoin_crowdsale_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    )
        public
    {
        GalaxyCoin token = new GalaxyCoin(name, symbol);
        galaxycoin_address = address(token);

        GalaxyCoinCrowdsale galaxycoin_crowdsale = new GalaxyCoinCrowdsale(1, wallet, token);
        galaxycoin_crowdsale_address = address(galaxycoin_crowdsale);

        token.addMinter(galaxycoin_crowdsale_address);
        token.renounceMinter();
    }
}