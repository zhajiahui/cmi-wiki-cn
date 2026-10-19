# Onspawnorload

## Description {#description}

Executes the skill when either [~onSpawn](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSpawn) or [~onLoad](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onLoad) would trigger.

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob spawns or when the mob is loaded after a server restart
    - message{m=SPAWNED! Or was i loaded?} @World ~onSpawnOrLoad
```
