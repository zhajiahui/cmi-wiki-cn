Data storage in Citizens2 is handled in one of two ways: [YAML flatfile](#Saves.yml) or a NBT file.

## saves.yml

*saves.yml* is used by default to store all data on created NPCs.

### Structure

Mouseover to view info:

```
# Citizens NPC Storage
npc:
  '0':
   name: My_First_NPC
   traits:
     age:
       age: 0
       locked: true
     spawned: true
     type: PLAYER
     owner: Steve
     lookclose: true
     location:
       world: world
       x: '92.65002360423462'
       y: '3.0'
       z: '-264.5621058817138'
       yaw: '87.90003967285156'
       pitch: '21.14999008178711'
     text:
       talk-close: true
       random-talker: true
       0: Hello, there. I'm My_First_NPC.
     waypoints:
       linear:
         points:
           '0':
             location:
               world: MyWorld
               x: 60
               y: 64
               z: 80
               pitch: 90
               yaw: 0
             delay: 0
           '1':
             location:
               world: MyWorld
               x: 65
               y: 64
               z: 82
               pitch: 45
               yaw: 0
             delay: 0
       provider: linear
```

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · Data Storage |
