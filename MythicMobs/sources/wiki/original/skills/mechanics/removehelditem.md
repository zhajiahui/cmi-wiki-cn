# Removehelditem

## Description {#description}

Removes the given amount from the casting player's held item.

> **This is a no-target mechanic, and the affected player will always be the caster**

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| amount | a | The amount to remove | 1 |

## Examples {#examples}

As a skill that only targets the casting player, a mob may need to use a [sudoskill](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sudoskill) to remove the player's item:

```yaml
munchy:
  Type: PIG
  Skills:
  - SudoSkill{s=removeApple} @trigger ~onInteract
```

This will cause a player to cast the `removeApple` meta-skill when right-clicking the mob:

```yaml
removeApple:
  Conditions:
  - holding{m=APPLE} true
  Skills:
  - removeHeldItem{amount=1}
```

This example checks for if the player (now the caster) is holding an apple, and if so, remove 1 from their hand.

## Aliases {#aliases}

- consumeHeldItem
- takeHeldItem
