pragma solidity ^0.5.0;

import "./GalaxyTokenLine.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract GalaxyTokenCrowdsale is Crowdsale, MintedCrowdsale {
    constructor(
        uint rate,
        address payable wallet,
        GalaxyTokenLine token
    )
        Crowdsale(rate, wallet, token)
        public
    {
        // constructor body can stay empty
    }
}

contract GalaxyTokenCrowdsaleDeployer {
    address public galaxy_token_address;
    address public galaxy_crowdsale_address;

    function CreateNFTLine
   
    {
        GalaxyToken token = new GalaxyToken(name, symbol, 0);
        galaxy_token_address = address(token);

        GalaxyTokenCrowdsale arcade_crowdsale = new GalaxyTokenCrowdsale(1, wallet, token);
        galaxy_crowdsale_address = address(galaxy_crowdsale);

        token.addMinter(galaxy_crowdsale_address);
        token.renounceMinter();
    }
}