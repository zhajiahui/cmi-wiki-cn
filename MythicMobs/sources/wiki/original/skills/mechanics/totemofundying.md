# Totem Of Undying

## Description {#description}

Plays the effect of a totem resurrecting a player with options to specify CustomModelData to use from resource packs.

> You can't disable the sound that plays

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| model | m | The CustomModelData to use for the shown totem |  |

## Examples {#examples}

```yaml
PlayTotemEffect:
  Skills:
  - totemofundying{model=2} @PIR{r=5}
```

## Aliases {#aliases}

- totemresurrection
- effect:totemresurrection
- e:totemresurrection
- totemresurrectioneffect
- totemofundying
- e:totemofundying
- totemeffect
