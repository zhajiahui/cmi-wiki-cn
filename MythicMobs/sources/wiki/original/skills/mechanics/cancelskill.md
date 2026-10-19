# Cancel Skill

## Description {#description}

Cancels the execution of the [Metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) when triggered

## Attributes {#attributes}

> *This mechanic has no attributes*

## Examples {#examples}

```yml
SomeSkill:
  Skills:
  - message{m="Hello"} @server
  - cancelSkill ?isMonster #cancels the rest of the skill from executing if the condition is met
  - message{m="It appears i am not a monster! Yay!"} @server
```

## Aliases {#aliases}

- cancel
- return
