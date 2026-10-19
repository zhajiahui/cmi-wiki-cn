## Overview

Wallets are a way to make the merchants seem more realistic by giving them a predefined amount of money to trade with. They also grant you better control over your server economy. In addition they are the only way players can manage account balance of the traders they created themselves.

## Wallet types

Seven wallet types are currently supported:

- **infinite** (admin only) - The trader has limitless money.
- **NPC** - The trader has his own separate wallet and can't buy items unless he can afford it. The trader's owner can transfer funds between him and the trader.
- **owner** - Allows the trader to directly use his owner's in-game money. Any transactions performed by the trader will affect that player's balance.
- **bank** - The trader uses a specified bank account. You must be that bank's owner to use this feature.

IMPORTANT:  This wallets are no longer supported, they will be added through another plugin, sorry for this

- **SimpleClans** - The trader uses a specified clan's bank account. A clan tag has to be provided.
- **Factions** - The trader uses a specified faction's bank account. A faction tag has to be provided.
- **Towny** - The trader uses a specified town's bank account. A town tag has to be provided.

## Setting the wallet type

To set the wallet type use:  
  
/trader wallet [wallet-type] [bank-name *OR* clan/faction/town tag]  
  
When no arguments are supplied the commands returns the current wallet type.

## Managing a wallet

To manage a trader with the NPC wallet type use the following commands:  
  
/trader balance  
/trader withdraw <amount>  
/trader deposit <amount> *(a fix for this command will be included in v2.3.0 Beta)*  
  
Note: Commands will be executed on the currently selected NPC.
