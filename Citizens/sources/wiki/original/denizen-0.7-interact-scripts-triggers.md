For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

Denizen Triggers trigger from interaction with Denizens. They are defined in the Steps: node of an Interact Script.

## Trigger Types

### Right Click

- **Click Trigger**s activate when the Denizen is right-clicked.

```
Click Trigger:
  Script:
  - CHAT "Teehee, that tickles!"
  - EMOTE "giggles"
```

### Attack / Left Click

- **Damage Trigger**s activate when the Denizen is left-clicked. If the Denizen has Damage Triggers disabled, this will count as a Click Trigger.

```
Damage Trigger:
  Script:
  - CHAT "OUCH, You'll pay for that!"
  - STRIKE <PLAYER>
```

### Proximity

- **Proximity Trigger**s activate when a player walks close to the Denizen.

```
Proximity Trigger:
  Script:
  - CHAT 'Eek! get away, you smell bad, <PLAYER>.'
```

### Chat

- **Chat Trigger**s activate when players chat with Denizens. Players' chat within the configurable range will be directed to the Denizen instead of global chat. Chat also follows the configuration setting. a single chat trigger entry can handle multiple words, see below:

```
Chat Trigger:
  '1':
    Trigger: The word needed to /Trigger/ is inside slashes, this whole sentence will appear to be said by the player
    Script:
    - CHAT "Good to know!"
  '2':
    Trigger: A chat trigger can also catch on any word not otherwise caught using /*/. 
    Script:
    - CHAT "I don't know what you mean, <PLAYER>!"
```

### Locations

- **Location Trigger**s activate when players walk near a [Location Bookmark](https://wiki.citizensnpcs.co/index.php?title=Location_Bookmark&action=edit&redlink=1 "Location Bookmark (page does not exist)"). Like chat triggers, multiple locations can be defined in one Location Trigger. They are similar in format to Chat Triggers in the fact that there can be multiple Locations per trigger entry.

```
Location Trigger:
  '1':
    Trigger: TreasureRoom
    Script:
    - TELEPORT BOOKMARK:Jail
  '2':
    Trigger: BedRoom
    Script:
    - NARRATE 'You enter the bedroom of the dead man, looking for clues'
```

### Player Death

- **Playerdeath triggers** activate when a Player dies. This trigger is disabled by default. The Trigger: node can be used to define the radius within which the player must die for the Denizen to see it. If the Trigger: is set to -1 the Denizen will attempt to handle any player deaths on the current world.

```
  Playerdeath Trigger:
    Radius: 50
    Script:
    - SHOUT "HA HA! <PLAYER> died!"
```

For a full list of Commands, see [Commands](https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts/Commands "Denizen/0.7/Interact Scripts/Commands")
