# Damage Cause

## Description {#description}

Checks the cause of the damage the entity took, if the skilltree originated from a [onDamaged Trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged) or an [onDamaged Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/ondamaged).  
A list of valid damage causes can be found in the [Spigot DamageCause javadoc](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| damagecause | cause, c | The damage cause to match | ENTITY_ATTACK |

## Examples {#examples}

```yaml
  Conditions:
  - damagecause{cause=ENTITY_ATTACK} true
```
