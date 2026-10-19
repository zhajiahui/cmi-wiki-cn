---
title: Teleportin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleportin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Teleportin {#teleportin}

## 说明 {#description}

相对施法者的偏航方向传送目标。direction 属性格式必须为 direction=x,y,z。

`x` 向前或向后，`y` 向上或向下，`z` 向左或向右

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| vector | direction,dir,d,v | 生物传送的方向 |  |
| yaw | y | yaw 修正值 | 0 |
| targetasorigin | tao | 使用目标的位置作为原点，而不是施法者的位置 | false |

## 示例 {#examples}

将触发技能的玩家传送到施法者的右侧。

```yaml
  Skills:
  - teleportin{vector=0,0,1} @trigger ~onInteract
```

## 别名 {#aliases}

- tpin
- tpdir
- tpi
