# Hide

## Description {#description}

Hides the caster from the targeted players for a set duration.

> The hidden entity can then be shown via the used of the [showentity](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/showentity) mechanic.

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| auraname | buffname, debuffname | The name of the aura | #hiding |
| ignoreAuraOptions | iao, permanent, perma | This will make the mechanic ignore any [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura)-related option and the `duration` attribute | false |

> This mechanic inherits every attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) mechanic
>
> > - The `auraname` attribute is **defaulted** at `#hiding`
> > - The `charges` attribute is **set** at `1`
> > - The `maxStacks` attribute is **set** at `1`
> > - The `mergeAll` attribute is **set** at `true`

## Examples {#examples}

```yml
DUMMY:
  Type: ZOMBIE
  Skills:
  - hide{d=100} @Server ~onInteract
```

##  {#section}

```yml
CUSTOM_ITEM:
  Id: STICK
  Skills:
  - hide{d=100} @Server ~onUse #User is now invisible from all online players, no armor is shown
```

## Aliases {#aliases}

- hideFromPlayers
- hideFromPlayer
