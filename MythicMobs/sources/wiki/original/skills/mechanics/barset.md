# Barset

## Description {#description}

Modifies a custom boss bar on the casting mob (cannot be player).

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| name | n | The name of the bossbar to modify/set | infobar |
| display | d, bartimerdisplay, bartimertext | The text displayed on the bar | <caster.name> |
| value | v | How filled the bossbar is. Must be between 0.0 and 1.0. | 1.0 |
| color | c, bartimercolor | The [Color](https://wiki.mythiccraft.io/mythicmobs/Mobs/BossBar#color) of the bossbar | RED |
| style | s, bartimerstyle | The [Style](https://wiki.mythiccraft.io/mythicmobs/Mobs/BossBar#style) of the bossbar | SOLID |

## Examples {#examples}

```yaml
  Skills:
  - barSet{
    name="MyBossBar";
    display="<caster.name> - <caster.hp>";
    value=1.0;
    color=RED;
    style=SEGMENTED_6
    } @self ~onDamaged
```
