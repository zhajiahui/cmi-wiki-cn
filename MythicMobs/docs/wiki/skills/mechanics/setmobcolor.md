---
title: Setmobcolor
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmobcolor
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setmobcolor {#setmobcolor}

## 说明 {#description}

更改目标颜色，只能应用于可着色的生物，例如潜影贝或羊。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| color | c | 颜色名称 |  |

## 示例 {#examples}

当可着色生物生成时，将其颜色设置为蓝色。

```yaml
  Skills:
  - setcolor{color=blue} @self ~onSpawn
  - ...
```

## 别名 {#aliases}

- setcolor
