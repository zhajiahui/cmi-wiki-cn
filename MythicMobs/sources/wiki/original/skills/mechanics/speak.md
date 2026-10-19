# Speak

## Description {#description}

Makes the caster speak using chat and speech bubbles. Supports
Holograms.  
You can force a new line in the hologram by using `\n`

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| offset | o, yo, yoffset | The y offset for the hologram. | 1 |
| radius | r | The radius of entities which will see the chat message | 12 |
| maxlinelength | ll, mll, ml, linelength | The maximum length of the hologram | 22 |
| lineprefix | lp | The prefix for the hologram. | &f |
| message | m, msg | The message to be displayed (affects both hologram and chat) |  |
| chatprefix | cp | The prefix for the chat message | <caster.name>&f<&co> |
| duration | d, ticks, time, t | The amount of time the hologram will be displayed for. | MESSAGE LENGTH * 4 |
| sendchatmessage | chatmessage, chat | Whether the message shows up in chat | true |
| audience |  | The [Audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the mechanic | tracked |

> This mechanic inherits every attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) mechanic
>
> > - The `auraname` attribute is **set** at `#speaking`
> > - The `charges` attribute is **set** at `1`
> > - The `maxStacks` attribute is **set** at `1`
> > - The `mergeSameCaster` attribute is **set** at `false`
> > - The `overwriteCaster` attribute is **set** at `true`
> > - The `refreshDuration` attribute is **set** at `false`

## Examples {#examples}

```yaml
  Skills:
  - speak{
    offset=0.6f;
    radius=30;
    maxlinelength=22;
    lineprefix="&5";
    message=" I just spawned!";
    chatprefix=<caster.name>&f<&co>;
    duration=200} @self ~onSpawn
```

## Aliases {#aliases}

- speech
