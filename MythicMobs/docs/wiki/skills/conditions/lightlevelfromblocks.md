---
title: Lightlevelfromblocks
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lightlevelfromblocks
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lightlevelfromblocks {#lightlevelfromblocks}

## 说明 {#description}

测试目标位置发光块发出的亮度水平

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| level | l | 要匹配的亮度范围。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - lightlevelfromblocks{l=10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=>10} true
```

```yaml
  Conditions:
  - lightlevelfromblocks{l=1to10} true
```

## 别名 {#aliases}

- blocklightlevel
