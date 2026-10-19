# Follow Path

## Description {#description}

Crates an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) that causes the holding mob to follow a path.  
This mechanic is also an [aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| path | p | A list of either coordinates in the format `(x,y,z)` or [targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters) |  |
| onGoalSkill | onGoal, og, then | The [metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) to execute when the last point is reached |  |
| tolerance |  | The minimum distance the mob must be from each point in order to having "reached" it | 2 |
| speed | s | The speed multiplier of the movement | 1 |
| duration | ticks, t, d, time, t | The maximum duration of the mechanic. Unless set, it's the maximum possible value for an integer |  |
| timeoutdistance | td, maxdistance, md | If set, if the distance between the mob and the next point is greater than this value, it will be immediately teleported to the next point |  |
| timeouttime | tt | If set, if the mob has not reached the next point in less than this allotted time, it will be teleported to the next point |  |

> This mechanic inherits every attribute of the [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) mechanic
>
> > - The `auraname` attribute is **set** at `#pathing`
> > - The `duration` attribute is **defaulted** at `2147483647`
> > - The `charges` attribute is **set** at `1`
> > - The `maxStacks` attribute is **set** at `1`
> > - The `mergeAll` attribute is **set** at `true`

## Examples {#examples}

```yaml
  Skills:
  - followPath{
    speed=2;
    tolerance=2;
    path=(200,5,520),(200,5,500),@forward{a=5};
    onGoal=[
      - message{m="I DID IT"} @world
    ]} @self ~onInteract
```

## Aliases {#aliases}

- path
