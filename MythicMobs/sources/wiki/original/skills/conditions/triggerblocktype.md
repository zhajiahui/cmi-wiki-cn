# Trigger Block Type

## Description {#description}

Checks against the material type that triggered the skill. Only works with specific [Triggers](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, block, b | A list of [materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) to check against | DIRT |

## Examples {#examples}

```yaml
  Conditions:
  - triggerblocktype{mat=STONE,DIRT} true
```

## Aliases {#aliases}

- triggeringBlockType
