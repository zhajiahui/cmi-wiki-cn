# Targeted Target

## Description {#description}

Targets the inherited targeted entities. Useful for [Targets Filtering](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#targets-filtering) by using [Targeter Options](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#targeter-options).

## Attributes {#attributes}

> *This targeter has no attributes*

## Examples {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @PIR{r=10}
```

##  {#section}

```yaml
ExampleSkill2:
  Skills:
  - lightning @TargetedTarget
```

## Aliases {#aliases}

- targeted
