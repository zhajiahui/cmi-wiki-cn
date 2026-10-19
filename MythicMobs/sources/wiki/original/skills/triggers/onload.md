# On Load

## Description {#description}

Executes the skill when the mob is loaded after a server restart.

## Examples {#examples}

```yml
EXAMPLE_MOB:
  Type: VILLAGER
  Skills:
    # sends a message to all the players in the world
    # when the mob is loaded after a server restart
    - message{m=LOADED} @World ~onLoad
```
