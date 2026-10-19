# Glow

## Description {#description}

Makes the target entity glow (like with the Glowing potion effect).

> Please note that this mechanic is not actually giving the *glowing* effect in any form: it will just *look* like it. If you want to check against the presence of this mechanic, you must check against the presence of the applied aura (an [hasaura](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasaura) condition can do the trick, for instance)

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| color | c | The [color](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Color.html) with which the entity will glow | white |
| audience |  | The [audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) of the glow effect | nearby |

## Aliases {#aliases}

- e:glow
- effect:glow
