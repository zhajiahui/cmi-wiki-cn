# Fake Lightning

## Description {#description}

Will strike a “fake” lightning bolt at the specified target.

The effect purely cosmetic and it plays the lightning sound effect, but will not cause any kind of damage to the target.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| localized | l | Whether the lightning should only be seen/heard by players in radius | false |
| localizedradius | lr, r | The radius of the localized effect Only works if localized is set to true! | 128 |

## Examples {#examples}

```yaml
SuperLightningSkill:
  Skills:
  - fakelightning @target
  - fakelightning @self
  - fakelightning{repeat=20;repeatInterval=1} @PIR{r=100}
```

## Aliases {#aliases}

- effect:lightning
- e:lightning
