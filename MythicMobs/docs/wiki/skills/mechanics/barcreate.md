---
title: Barcreate
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/barcreate
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Barcreate {#barcreate}

## 说明 {#description}

为施法生物创建自定义 Boss 血条，不能用于玩家。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| name | n | Boss 血条名称。 | infobar |
| display | d, bartimerdisplay, bartimertext | 血条上显示的文字。 | <caster.name> |
| value | v | Boss 血条的填充程度，必须介于 0.0 和 1.0 之间。 | 1.0 |
| color | c, bartimercolor | Boss 血条的[颜色](../../mobs/bossbar.md#color)。 | RED |
| style | s, bartimerstyle | Boss 血条的[样式](../../mobs/bossbar.md#style)。 | SOLID |

## 示例 {#examples}

```yaml
  Skills:
  - barCreate{
    name="MyBossBar";
    display="<caster.name> - <caster.hp>";
    value=1.0;color=BLUE;
    style=SEGMENTED_6
    } @self ~onSpawn
```

## 别名 {#aliases}

- barAdd
- createBar
