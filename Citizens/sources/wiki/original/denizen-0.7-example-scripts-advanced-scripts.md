For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

These scripts use all the powerful features of Denizen to do some really cool things.

#### Maggie's Magic Shop

Maggie sells magic odds and ends. This set of scripts simulates a vendor. She will greet the player, offer her wares, and check for the proper amount of money. This is a great example of how to use Flags.

[![](https://wiki.citizensnpcs.co/images/8/89/Maggie_Choice_Debug.png)](https://wiki.citizensnpcs.co/File:Maggie_Choice_Debug.png)

Maggie's Script: What would you like to buy?

[![](https://wiki.citizensnpcs.co/images/c/c3/Maggie_Buying_Feathers.png)](https://wiki.citizensnpcs.co/File:Maggie_Buying_Feathers.png)

Maggie's Script: Buying Feathers game screen

[![](https://wiki.citizensnpcs.co/images/d/de/Maggie_Feather_Debug.png)](https://wiki.citizensnpcs.co/File:Maggie_Feather_Debug.png)

Maggie's Script: Buying Feathers debug screen

```
# Maggie sells some magic items for money.
# Version 1.1

# ASSIGNMENTS
#
#  Maggie:
#    Interact Scripts:
#    - 0 Magic Shop
#    - 10 ^Magic Shop Not Enough Money
#    - 20 ^Magic Shop Feathers
#    - 20 ^Magic Shop Dust
    
# MAGGIES MAGIC SHOP.YML ----

'Magic Shop':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Proximity Trigger:
        Script:
        - CHAT 'Welcome to my shop! Have a look around!'
      Click Trigger:
        Script:
        - CHAT 'What would you like to buy?'
        - HINT
      Chat Trigger:
        1:
          Trigger: I would like to buy some /feathers/
          Script:
          - CHAT 'Great! Feathers are 20 coins.'
          - ^NARRATE 'Right click to purchase some feathers.'
          - FLAG 'MAGICSHOPITEM:FEATHER' 'DURATION:15'
        2:
          Trigger: I would like to buy some /glowstone dust/
          Script:
          - CHAT 'Great! Glowstone dust is 50 coins.'
          - ^NARRATE 'Right click to purchase some glowstone dust.'
          - FLAG 'MAGICSHOPITEM:DUST' 'DURATION:15'
        3:
          Trigger: I would like to buy some /*/
          Script:
          - CHAT "Ah! Sorry, I don't sell any of that!"

          
'Magic Shop Not Enough Money':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM'
  Steps:
    1:
      Click Trigger:
        Script:
        - ^NARRATE "Erm... seems you don't have enough money."
        - RESET 'FLAG:MAGICSHOPITEM'

        
'Magic Shop Feathers':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM:FEATHER'
    - MONEY 20
  Steps:
    1:
      Click Trigger:
        Script:
        - ^TAKE MONEY QTY:20
        - ^GIVE FEATHER QTY:10
        - CHAT 'Thanks! Here are your feathers.'  
        - NARRATE 'You bought 10 Feathers for 20 coins! Sweet!'
        - NARRATE 'Right click again to buy some more.'

        
'Magic Shop Dust':
  Type: Interact
  Requirements:
    Mode: All
    List:
    - FLAGGED 'MAGICSHOPITEM:DUST'
    - MONEY 50
  Steps:
    1:
      Click Trigger:
        Script:
        - ^TAKE MONEY QTY:50
        - ^GIVE GLOWSTONE_DUST QTY:10
        - CHAT "Thanks! Here's your dust."
        - NARRATE 'You bought 10 Glowstone Dust for 50 coins! Sweet!'
        - NARRATE 'Right click again to buy some more.'
```

## To Do
