# Owner

## Description {#description}

Targets the Owner of the casting mob.  
The Owner can be set via the [SetOwner](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/setowner) mechanic.

## Attributes {#attributes}

> *This targeter has no attributes*

## Examples {#examples}

This metaskill will send a message to the Owner of the casting mob

```yaml
ExampleSkill:
  Skills:
  - message{m="Hello there!"} @Owner
```
