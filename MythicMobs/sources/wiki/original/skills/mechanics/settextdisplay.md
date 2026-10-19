# Set Text Display

## Description {#description}

Sets the text component of target Text Display entity

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| text | t | The text to use. If not set, the mechanic will remove the text from the entity instead |  |

## Examples {#examples}

```yaml
ExampleTextDisplayEntity:
  Type: TEXT_DISPLAY
  DisplayOptions:
    Text: I am but a humble example, nothing to see here
  Skills:
  - settextdisplay{text="MUHAHAHA! YOU FELL FOR MY TRICKERY!";delay=100} @self ~onSpawn
```

## Aliases {#aliases}

- setText
