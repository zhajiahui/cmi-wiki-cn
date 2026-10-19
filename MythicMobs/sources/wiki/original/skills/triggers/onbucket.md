# On Bucket

## Description {#description}

Executes the skill when the cow is milked or when an entity is stored in a bucket (axolotl and the other bucketable ones).

> The associated [@trigger](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Trigger) is the caster itself

## Examples {#examples}

```yaml
ANormalCow:
  Type: Cow
  Skills:
  - skill{s=[
    - message{m="HOW DARE YOU?!?"} @trigger
    - sound{s=entity.creeper.primed}
    - explosion{yield=5;delay=30}
    ];cd=2} @self ~onBucket
```

## Aliases {#aliases}

- onUseBucket
- onFillBucket
- onBucketFill
- onMilk
- onMilked
