## Citizens 2.0.x Permissions

This page may be outdated: double check the plugin.yml at <https://github.com/CitizensDev/Citizens2/blob/master/main/src/main/resources/plugin.yml> for up-to-date permissions

Default on all permissions is OP

- citizens.admin.*
  - citizens.admin This allows players to edit 'server' owned NPCs
  - citizens.admin.avoid-limits Allows user to create any number of NPCs
- citizens.help /citizens help
- citizens.npc.*:
  - citizens.npc.age /npc age
  - citizens.npc.position.assume /npc age
  - citizens.npc.behaviour /npc behaviour
  - citizens.npc.create /npc create
  - citizens.npc.create.[mobtype or *] /npc create [mobtype]
  - citizens.npc.controllable /npc controllable
  - citizens.npc.copy /npc copy
  - citizens.npc.despawn /npc despawn
  - citizens.npc.edit.*
    - citizens.npc.edit.equip /npc equip
    - citizens.npc.edit.path /npc path
  - citizens.npc.help /npc help
  - citizens.npc.limit.# Limit this player to creating # number of NPCs (works with 1-100
  - citizens.npc.list /npc list
  - citizens.npc.lookclose /npc lookclose
  - citizens.npc.moveto /npc moveto
  - citizens.npc.owner /npc owner
  - citizens.npc.path /npc path
  - citizens.npc.power /npc power
  - citizens.npc.profession /npc profession
  - citizens.npc.remove /npc remove
  - citizens.npc.remove.all /npc removeall
  - citizens.npc.rename /npc rename
  - citizens.npc.select /npc select
  - citizens.npc.spawn /npc spawn
  - citizens.npc.speed /npc speed
  - citizens.npc.talk  Hear NPCs by click or walking near with talk-close
  - citizens.npc.text /npc text
  - citizens.npc.trait.*
    - citizens.npc.trait /trait
    - citizens.npc.trait-configure
    - citizens.npc.trait-configure.*
    - citizens.npc.tp /npc tp
    - citizens.npc.tphere /npc tphere

## Character Permissions

See the appropriate [Characters](https://wiki.citizensnpcs.co/Characters "Characters") page for character-specific permission nodes.

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · Permissions  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
