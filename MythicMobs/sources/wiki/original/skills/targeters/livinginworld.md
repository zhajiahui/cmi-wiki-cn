# Living In World

## Description {#description}

Targets all living entities in the caster's world

## Attributes {#attributes}

> *This targeter has no attributes*

## Examples {#examples}

```yaml
EntityCount:
  Skills:
  - setvariable{var=skill.count;val=<skill.targets>} @LivingInWorld
  - message{m="There are <skill.var.count> entities loaded in the current world"} @self
```

## Aliases {#aliases}

- EIW
- allinworld
- livingentitiesinworld
- entitiesinworld
