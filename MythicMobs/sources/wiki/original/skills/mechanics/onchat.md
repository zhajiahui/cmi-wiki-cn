# On Chat

## Description {#description}

Applies an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) on the target player that triggers a [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) when they type a chat message

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.input>` |

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| onChatSkill | onchat, oc, then | The [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) to execute when the player chats |  |

> This mechanic inherits every attribute of the [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) mechanic

## onChatSkill Attribute {#onchatskill-attribute}

When the metaskill is execute, a new [skill-scoped variable](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables) containing what has been said in chat is set, called `input`.  
Its value can then be fetched via the `<skill.var.input>` placeholder.

## Examples {#examples}

The `ExampleSkill` metaskill will create an aura on every player in a 20 blocks radius. If those players were to chat during its 10 seconds duration, a message would be sent to them and they would be set on fire.

```yaml
ExampleSkill:
  Skills:
  - onChat{onChat=ExampleSkill2;d=200} @PIR{r=20}

ExampleSkill2:
  Skills:
  - message{m="SILENCE!"} @trigger
  - ignite @trigger
```

This below example uses the [StringEquals](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/stringequals) condition to check what the player typed! The message mechanic will only appear if the player typed `QueenOfAnts is a noob`.

```yaml
YourMob:
  Type: ZOMBIE
  Skills:
  - onChat{onChat=ChatSkill;d=1000} @trigger ~onInteract

ChatSkill:
  Conditions:
  - stringequals{val1="<skill.var.input>";val2="QueenOfAnts is a noob"} true
  Skills:
  - message{m=She is indeed!} @trigger
```

## Aliases {#aliases}

- chatprompt
