# Spawn Reason

## Description {#description}

Checks against the spawn reason of the target(s)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| reason | r | The reason to check for. Can be any of the [Bukkit](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/event/entity/CreatureSpawnEvent.SpawnReason.html) ones |  |

## Examples {#examples}

In this example, the skill will apply a glow effect to the target entity if it has been spawned because of a raid

```yaml
ExampleSkill:
  TargetConditions:
  - spawnReason{reason=RAID} true
  Skills:
  - potion{t=GLOWING;d=100;l=0}
```
