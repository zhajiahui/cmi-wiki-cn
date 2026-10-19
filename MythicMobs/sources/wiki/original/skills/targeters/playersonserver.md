# Players On Server

## Description {#description}

Targets all players in the server

## Attributes {#attributes}

> *This targeter has no attributes*

## Examples {#examples}

```yaml
PlayerCount_ServerWide:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @PlayersOnServer{targetself=true}
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```

## Aliases {#aliases}

- server
- everyone
