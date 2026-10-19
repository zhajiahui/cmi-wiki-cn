NPCs can be given Waypoints to pathfind between.

Waypoints are created by a Waypoint Provider. You can change providers using the /waypoint provider [provider] command.

The current Providers are:

Linear (default) - Sends the NPC to each stored waypoint in sequence.

Wander - The NPC wanders around randomly.

Guided - The waypoints are split into destination waypoints and helper waypoints. Destination waypoints are chosen randomly and pathed to using the helper waypoints as a guide. Useful for say patrolling NPCs in a city where you want them to roughly stick to the roads.

## Waypoint triggers

For the linear and guided waypoint provider, triggers can be added to pause the NPC at certain waypoints, change their speed or say something at a waypoint. More information can be found by typing 'triggers' in the waypoint editor.

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · [API](https://wiki.citizensnpcs.co/API "API")  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · Waypoints  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
