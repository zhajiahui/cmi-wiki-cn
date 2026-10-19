For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

## Requirements

Requirements set criteria for your scripts to check against. They provide a powerful way to have a variety of interaction possibilities with Denizen NPCs. Imagine NPCs that will offer you some fish when hungry, or a shopkeeper that can sell you goods. These are two of many things made possible with the use of Requirements.

Note: Requirements from 0.6 are in-tact for 0.7, but will now be referred to as 'Legacy Requirements'. They will be slowly replaced with new commands that will override functionality. The new systems allows for improved tolerence better debugging, as well as make it easy for other plugin programmers to extend Denizen. Just a heads up. This page will keep you informed of any changes.

`[] indicates required field, () indicates an optional field, | indicates alternative usage.`

Click on any requirement to get more information and example usages.

### Player

|  |  |
| --- | --- |
| [DURABILITY](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [> or < or =] [# or %] |

|  |  |
| --- | --- |
| [HOLDING](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [ITEM_NAME or #:#] (Quantity) |

|  |  |
| --- | --- |
| [HUNGER](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Full or Hungry or Starving] |

|  |  |
| --- | --- |
| [ITEM](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [ITEM_NAME or #:#] (Quantity) |

|  |  |
| --- | --- |
| [LEVEL](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [# or higher]  OR  LEVEL  [At least this Level #]  [No more than this Level #] |

|  |  |
| --- | --- |
| [NAME](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Player Name]  (Player Name)  (Player Name) ... |

|  |  |
| --- | --- |
| [OWNER](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") |  |

|  |  |
| --- | --- |
| [POTIONEFFECT](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [POTION_TYPE] |

|  |  |
| --- | --- |
| [SNEAKING](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") |  |

|  |  |
| --- | --- |
| [WEARING](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [ITEM_NAME or #:#] |

### World

|  |  |
| --- | --- |
| [ISLIQUID](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [BOOKMARK:Block Bookmark] |

|  |  |
| --- | --- |
| [ISPOWERED](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [BOOKMARK:Block Bookmark] |

|  |  |
| --- | --- |
| [PRECIPITATING](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") |  |

|  |  |
| --- | --- |
| [STORMY](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") |  |

|  |  |
| --- | --- |
| [SUNNY](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") |  |

|  |  |
| --- | --- |
| [TIME](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Day or Night or Dusk or Dawn or TIME 0-23999] |

|  |  |
| --- | --- |
| [WORLD](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [World Name]  (World Name)  (World Name) ... |

### Script

|  |  |
| --- | --- |
| [ACTIVITY](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Name of Activity] |

|  |  |
| --- | --- |
| [FAILED](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | (# of times)  [Script Name] |

|  |  |
| --- | --- |
| [FINISHED](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | (# of times)  [Script Name] |

|  |  |
| --- | --- |
| [FLAGGED](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [FlagName:FlagValue or FlagName] (EXACTLY) (PLAYER or DENIZEN or GLOBAL) |

|  |  |
| --- | --- |
| [SCRIPT](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [FINISHED or FAILED or STEP] (STEP:#) (QTY:#) (EXACTLY) [SCRIPT:scriptname] |

### Permission/Economy

These requirements only work if you have Vault installed and a compatible permissions/economy plugin.

|  |  |
| --- | --- |
| [GROUP](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Group Name]  (Group Name)  (Group Name) ... |

|  |  |
| --- | --- |
| [MONEY](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [Quantity] |

|  |  |
| --- | --- |
| [PERMISSION](https://wiki.citizensnpcs.co/index.php?title=Interact_Script_Requirements&action=edit&redlink=1 "Interact Script Requirements (page does not exist)") | [permission.node] |

### Negative Requirements

Requirements can also be 'negative' requirements. In the Requirements List, just place a '-' in front of the requirement to inverse its logic. For example, 'HOLDING IRON_SWORD' would require the player to be holding an Iron Sword. '-HOLDING IRON_SWORD' would require the player to NOT be holding an Iron Sword. All requirements have a negative alternative, even ones whose function may overlap, such as '-WEATHER Precipitating' and 'WEATHER Sunny', which technically do the same thing. If anything, it can add to script readability. The negative requirement '-' should not be confused with the 'list item -' with a trailing space in front of each Requirement in the List, as that is standard YAML list format. See below:

```` ```
 Requirements:
   Mode: All
   List:
   - -TIME Night
   - -MONEY 1000000
   - -STORMY
``` ````

Negative requirements can completely change the original example around. In this 'revised' example, for this script to trigger, time needs to be day, the weather in the current world must NOT be storming, and the player have less than 1000000 units of currency on them.
