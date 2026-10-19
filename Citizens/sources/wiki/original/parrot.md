| **External Character Type!** |
| --- |
| This page is about a type of NPC that is not developed supported by the Citizens development team. Don't ask for support from them, or on the forums/IRC, as we won't be able to help you. Instead, look at the BukkitDev link of the InfoBox to the right for information on how to get support for this character type. |

<table align="right" cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="30%">
<tbody><tr>
<td style="width: 30%; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:gray; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; align:center; font-weight: bold; border-bottom:1px solid #aaaaaa;"><center><span class="mw-default-size" typeof="mw:Error mw:File"><a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Special:Upload&amp;wpDestFile=Mimic.png" title="File:Mimic.png"><span class="mw-file-element mw-broken-media">File:Mimic.png</span></a></span><br/><br/><b>Mimic</b></center></div>
<div style="font-size:100%; padding:13px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="150"><b>Author</b>
</td>
<td><a href="https://wiki.citizensnpcs.co/User:Aufdemrand" title="User:Aufdemrand">aufdemrand</a>
</td></tr>
<tr>
<td><b>Version</b>
</td>
<td>0.6
</td></tr>
<tr>
<td><b>Citizens build</b>
</td>
<td>2.0 (#37)
</td></tr>
<tr>
<td><b>Development status</b>
</td>
<td>InDev
</td></tr>
<tr>
<td><b>Download</b>
</td>
<td><a class="external text" href="http://dev.bukkit.org/server-mods/parrot/files/2-parrot-beta-v0-4/" rel="nofollow">Link</a>
</td></tr>
<tr>
<td><b>BukkitDev</b>
</td>
<td><a class="external text" href="http://dev.bukkit.org/server-mods/parrot/" rel="nofollow">Link</a>
</td></tr>
<tr>
<td><b>Source</b>
</td>
<td><a class="external text" href="http://www.github.com/aufdemrand/Mimic" rel="nofollow">Link</a>
</td></tr>
<tr>
<td><b>Issues</b>
</td>
<td><a class="external text" href="http://www.github.com/aufdemrand/Mimic/Issues" rel="nofollow">Link</a>
</td></tr>
<tr>
<td colspan="2"><div style="border-top:1px solid #aaaaaa;"><b>Description:</b> A mimic NPC that can be used for fun or for clues.</div>
</td></tr>
<tr>
<td colspan="2"><div style="border-top:1px solid #aaaaaa;"><center><code><a href="https://wiki.citizensnpcs.co/Installing_Character_Types" title="Installing Character Types">Installing Character Types</a></code></center></div>
</td></tr></tbody></table>
</div>
</td></tr></tbody></table>

Mimics are an attempt to bring some RPG elements to Minecraft using Citizens2. Mimics can be just for fun, or be used with questing to hold clues. Enderdragon parrots, anybody? (Joking! Probably not a good idea!)

Mimics randomly store messages said in the local area and repeat them back. Mimics can also hold a clue, information that it keeps and blurts out with the normal chatter it has heard for a great element to any RPG puzzle.

## Features

Customizable 'Voice' Mimic types with adjustable text messages for timed text and onclick behavoir.
Comes standard with a Parrot, Slime Mimic, and Village Idiot. You can add your own!

## Planned Future Features

## Commands

## Permissions

## Settings (and defaults)

Below is the standard configuration with notes.

```
# Mimic Configuration

cooldown-in-seconds: 45       # Time between each message/etc update timer. 
                              #   (Recommended 30-90)
click-cooldown-in-seconds: 5
chatter-range: 25             # Distance from Mimic needed to be to hear it.
                              #   (Recommended 10-30)
# Note: Next two lines have not yet been implemented, but still need to be set.
text-style: Normal            # Available: Sentence Case, Lower Case, Upper Case, Normal
use-smart-wrap: True          # Wraps text spanning multiple lines smartly.


# TYPES/DIALOG Setup
# You can add as many items to the list as you'd like.
# You can use <text> to use the mimic's texts.
# Note: <text> also randomly shows the mimic's clue.

voice types:
  list:               # List each voice mimic type. Case sensitive!
    - Parrot
    - Village Idiot
    - Slime Mimic

  NPC defaults:       # You can specify mimic type defaults for each npc type
                      # EntityTypes specified here will automatically apply the mimic type set alongside.
    SLIME: Slime Mimic
    CHICKEN: Parrot
    VILLAGER: Village Idiot

  # And now in detail. Note: This part needs to be indented as it's still part
  # of the types: node.  This is where you define each type. This is case sensitive!
  # When adding new types, be sure to add them to the list: node above, as well.

  Parrot:
    on click:         # Texts on click
      - "It's a parrot."
      - "You pet the parrot. *BAAAWK!*"
    texts:            # Texts that trigger randomly.
      - "A parrot squacks, '<text>'"
      - "'<text>' ...is that a parrot?"
      - "You hear a parrot nearby, '*SQUAK*!'"
      - "You hear a parrot nearby, '<text>'"
      - "*BRR BRR BRR* ...is that a parrot?"
      - "*BAAAWK* *BAAAWK*"   

  Village Idiot:
    on click:
      - "Oh, it's just the Village Idiot... he's an idiot."
      - "You slug the Village idiot in the arm. *OUCH!*"
      - "The Village Idiot says to you, 'text'"
    texts:
      - "'Yarharrrharr!' ...what the heck was that?"
      - "The village idiot says, '<text>' ...does that even make sense?"
      - "'<text>' says the Village Idiot, in a drunken slur."

  Slime Mimic:
    click:
      - "It's a jelly-like block of slime. Yuck!"
      - "The slime is filled with all kinds of stuff. Who knows where it has been?"
    texts:
      - "'<text>' ...was that a slime mimic?"
      - "You hear a slime mimic nearby, '<text>'"
      - "*SQUISH* *SQUISH*"
```

Note: As Mimics are created and interacted with, another section will populate in the config.yml. This should be configured in-game with commands.
