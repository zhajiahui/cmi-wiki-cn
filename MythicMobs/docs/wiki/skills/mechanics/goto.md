---
title: Goto
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/goto
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Goto {#goto}

## 说明 {#description}

使生物寻路到指定位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| speed | s | 移动速度修饰值。 | 1 |
| spreadH | sh | 相对于正在前往的目标，允许的水平散布量。 | 0 |
| spreadV | sv | 相对于正在前往的目标，允许的竖直散布量。 | 0 |

## 示例 {#examples}

```yml
  Skills:
  - goto{speed=1;sh=5;sv=5} @owner
  - goto{speed=1;sh=5;sv=5} @location{c=100,65,100}
```

## 别名 {#aliases}

- pathto
- navigateto
