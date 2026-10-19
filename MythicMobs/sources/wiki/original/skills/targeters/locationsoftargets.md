# Locations Of Targets

## Description {#description}

Targets the location of the inherited targets

## Attributes {#attributes}

> *This targeter has no attributes*

## Examples {#examples}

```yaml
ExampleSkill1:
  Skills:
  - skills{s=ExampleSkill2} @EIR{r=10}

ExampleSkill2:
  Skills:
  - lightning @LocationsOfTargets
```

## Aliases {#aliases}

- locationOfTarget
- LOT
