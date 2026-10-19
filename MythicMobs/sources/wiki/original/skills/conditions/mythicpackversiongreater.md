# Mythic Pack Version Greater

## Description {#description}

Check if a [Pack](https://wiki.mythiccraft.io/mythicmobs/Packs) with the specified id is present on the server with a version that is either greater or equal the specified one.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| packid | pack, id, p | The Pack id to check for |  |
| packversion | packV, version, v | The version to check for |  |

## Examples {#examples}

```yaml
  Conditions:
  - packversiongreater{p="ThePackId";v="1.2.3"} true
```

## Aliases {#aliases}

- packversiongreater
- packversionisgreater
