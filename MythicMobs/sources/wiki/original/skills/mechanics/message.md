# Message

## Description {#description}

Sends a chat message to the target, if the target is a player. [Color
codes](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#color-codes) and
[variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables) are useable in this mechanic.

- Allows hex colors in the format **`<#FFFFFF>`**
- Supports gradients in the format **`<gradient:#color1:#color2>text</gradient>`**
- Supports **`<rainbow>text</rainbow>`**
- Supports hover text in the format **`<hover:show_text:'hover text??'>hover over me!</hover>`**
- Supports clickable text in the format **`<click:run_command:/say hello>click me!</click>`**

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| message | msg,m | The message to send | None |
| audience |  | the [audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the message |  |

## Examples {#examples}

```yaml
   Skills:
   - message{m="<caster.name>&f<&co> Hahaha! You will all die!"} @PlayersInRadius{r=30}
```

## Aliases {#aliases}

- m
- msg
