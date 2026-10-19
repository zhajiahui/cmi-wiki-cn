# Onchangeworld

## Description {#description}

Executes the skill when the caster changes world.

## Examples {#examples}

```yaml
WorldJumper:
  Type: WITHER_SKELETON
  Skills:
  - command{c=say The End!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_the_end}
  - command{c=say The Nether!} @self ~onChangeWorld ?varEquals{var=skill.world;value=world_nether}
```

## Aliases {#aliases}

- onChange_World
- onWorld_Change
- onWorldChange
