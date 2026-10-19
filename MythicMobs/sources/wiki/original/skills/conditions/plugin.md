# Plugin

## Description {#description}

Checks if the specified plugin is running on the server

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| plugin | pl, p | The plugin to check for | MythicMobs |

## Examples {#examples}

```yml
  Conditions:
  - plugin{p=ThePluginName} true
```

## Aliases {#aliases}

- pluginexists
- hasplugin
