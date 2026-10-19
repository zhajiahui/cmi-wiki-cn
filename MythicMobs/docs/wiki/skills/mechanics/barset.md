---
title: Barset
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barset
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Barset {#barset}

## 说明 {#description}

修改施法生物的自定义 Boss 血条，不能用于玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | 要修改或设置的 Boss 血条名称。 | infobar |
| display | d, bartimerdisplay, bartimertext | 血条上显示的文字。 | <caster.name> |
| value | v | Boss 血条的填充程度，必须介于 0.0 和 1.0 之间。 | 1.0 |
| color | c, bartimercolor | Boss 血条的[颜色](../../mobs/bossbar.md#color)。 | RED |
| style | s, bartimerstyle | Boss 血条的[样式](../../mobs/bossbar.md#style)。 | SOLID |

## 示例 {#examples}

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
