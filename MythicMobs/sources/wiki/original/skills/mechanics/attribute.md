# Attribute

## Description {#description}

Sets the base value of the targeted entity's [attribute](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html).
Not supposed to be used on players.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| attribute | attr | The [attribute](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html) to set | GENERIC_LUCK |
| amount | amt, a | The amount of the attribute | 0 |
| duration | dur | The duration of the attribute | 0 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attribute{attribute=GENERIC_LUCK;a=2;duration=1200} @trigger ~onDeath
```

## Aliases {#aliases}

- setattribute
