# 🎒 Inventory {#🎒-inventory}

## Close Inventory {#close-inventory}

Use this mechanic to close the current player's inventory. This can be used inside any MMO plugin UI: MMOItems crafting stations, MMOProfiles profile selection, MMOCore skill tree UIs, etc...

```yml
script_close_inventory:
  mechanics:
    - 'close_inventory{}'
```

## Go Back {#go-back}

Use this to have the player navigate to the last page visited. For instance, this can be used to go back from the *Class Confirmation UI* to the *Class Selection UI* in MMOCore for instance.

```yml
script_ui_go_back:
  mechanics:
    - 'go_back{}'
```
