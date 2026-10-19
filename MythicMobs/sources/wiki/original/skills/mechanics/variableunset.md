# Variableunset

## Description {#description}

Unsets a [variable](https://wiki.mythiccraft.io/mythicmobs/skills/variables).

## Attributes {#attributes}

> This mechanic inherits every *inheritable* attribute of the [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable) mechanic

## Examples {#examples}

This will unset the testing caster scope variable from the caster.

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=caster.testing} @self
```

This will unset the testing caster scope variable from the caster as well.

```yaml
RemoveVariable:
  Skills:
  - variableUnset{var=testing;scope=caster} @self
```

## Aliases {#aliases}

- unsetvariable
- unsetvar
- varunset
