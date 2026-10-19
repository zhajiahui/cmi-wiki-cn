---
title: Hasaurastacks
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/hasaurastacks
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Hasaurastacks {#hasaurastacks}

## 说明 {#description}

测试目标是否具有给定的光环堆叠范围

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | 要检查的光环名称。 |  |
| stacks | s | 要检查的层数或层数范围。 | 1 |

## 示例 {#examples}

```yaml
  Conditions:
  - hasaurastacks{n=firedebuff;s=>3} true
```

## 别名 {#aliases}

- hasbuffstacks
- hasdebuffstacks
- aurastacks
- buffstacks
- debuffstacks
