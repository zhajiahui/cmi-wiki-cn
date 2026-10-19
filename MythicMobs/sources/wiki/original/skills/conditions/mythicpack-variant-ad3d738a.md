# Mythicpack

## Description {#description}

Check if a [Pack](https://wiki.mythiccraft.io/mythicmobs/Packs) with the specified id is present on the server.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| packid | pack, id, p | The pack id to check for |  |

## Examples {#examples}

```yaml
  Conditions:
  - mythicpack{p="ThePackId"} true
```

## Aliases {#aliases}

- pack
- haspack
