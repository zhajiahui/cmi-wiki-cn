# Trigger Item Type

## Description {#description}

Checks against the item material type that triggered the skill. Only works with specific [Triggers](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| types | type, t, material, mat, m, items, item, i | A list of [materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) to check against | DIRT |

## Examples {#examples}

```yaml
  Conditions:
  - triggeritemtype{mat=STONE,DIRT,STONE_SWORD} true
```

## Aliases {#aliases}

- triggeringItemType
