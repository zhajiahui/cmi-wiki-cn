# Mythic Pack Version

## Description {#description}

Check if a [Pack](https://wiki.mythiccraft.io/mythicmobs/Packs) with the specified id is present on the server with the specified version.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| packid | pack, id, p | The Pack id to check for |  |
| packversion | packV, version, v | The version to check for |  |

## Examples {#examples}

```yaml
  Conditions:
  - packversion{p="ThePackId",v="1.2.3"} true
```

## Aliases {#aliases}

- packversion
- packversionis
