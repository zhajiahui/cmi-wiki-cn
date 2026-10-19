# Attribute Modifier

## Description {#description}

Adds an attribute modifier to the attributable target.
Not supposed to be used on players.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| attribute | attr | The [attribute](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/Attribute.html) | GENERIC_LUCK |
| operation | op | The [operation](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/attribute/AttributeModifier.Operation.html) to perform | ADD_NUMBER |
| name | modifierName | The name of the modifier | <caster.uuid> |
| amount | amt, a | The modifier of the attribute | 0 |
| duration | dur | The duration of the attribute | 0 |

## Examples {#examples}

```yaml
ExampleMob:
  Type: ZOMBIE
  Skills:
  - attributeModifier{attribute=GENERIC_LUCK;a=2;dur=1200;op=ADD_NUMBER} @trigger ~onDeath
```
