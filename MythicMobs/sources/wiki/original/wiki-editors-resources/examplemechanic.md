# Example Mechanic

## Description {#description}

The description of the mechanic: what it does, how it does it, and possible notes.

> **This is a [Paper-Only](https://papermc.io/downloads/all) mechanic!**

> **This is a [Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features) mechanic!**

> **This is a no-target mechanic, and the affected entity will always be the caster**

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.example1>` |
| `<skill.var.example2>` |

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| attribute1 | alias1, alias2 | The description of what the attributes does | default value |
| attribute2 | alias3 | The description of what the attributes does | default value |
| attribute3 |  | The description of what the attributes does | default value |
| attribute4 |  | The description of what the attributes does **<[Premium-Only](https://wiki.mythiccraft.io/mythicmobs/Premium-Features)>** | default value |

> This mechanic inherits every *inheritable* attribute of the [ExampleMechanic2](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ExampleMechanic2) mechanic
>
> > - The `attribute4` attribute is **defaulted** at `0`
> > - The `attribute5` attribute is **set** at `0` and cannot be modified

> *This mechanic has no attributes*

### Attribute1 Attribute {#attribute1-attribute}

A more in-depth explanation of what the attributes does, how it does it, what values are accepted and so on. Optional, only if necessary.

## Examples {#examples}

A description of the example below.

```yaml
  Skills:
  - examplemechanic{attribute1=value1} @targeter
```

##  {#section}

Another example:

```yaml
  Skills:
  - examplemechanic{attribute1=value1;attribute2=value2} @targeter
```

## Aliases {#aliases}

- mechanic_alias_1
- mechanic_alias_2
