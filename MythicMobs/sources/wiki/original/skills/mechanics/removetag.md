# Removetag

## Description {#description}

Removes a scoreboard tag from the target.

This is used in conjunction with the **hastag condition** (see
[Conditions](https://wiki.mythiccraft.io/mythicmobs/conditions/start)). You can also use the vanilla command
`/scoreboard players tag <player name> remove [Tag Name]` to do
the same thing.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| tag | t | The string-name of the tag | default |

## Examples {#examples}

This skill would give the casting mob the tag "Test".

```yaml
UntagSkill:
  Skills:
  - removetag{t=Test} @self
```

## Aliases {#aliases}

- removescoreboardtag
- tagremove
