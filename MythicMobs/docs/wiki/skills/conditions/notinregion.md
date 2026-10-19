---
title: Notinregion
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/notinregion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Notinregion {#notinregion}

## 说明 {#description}

检查目标位置是否**不在**给定的 WorldGuard 区域内

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| region | r, name, n | 区域名称。 |  |

## 示例 {#examples}

```yaml
  Conditions:
  - notinregion{r=BossZone} true
```
