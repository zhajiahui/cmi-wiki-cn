---
title: Servernmsversion
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/servernmsversion
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Servernmsversion {#servernmsversion}

## 说明 {#description}

检查服务器是否正在运行特定的 minecraft NMS 版本

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| version | sv, v | 要检查的版本。 | v1_19_R1_2 |

## 示例 {#examples}

```yaml
  Conditions:
  - nmsversion{v="v1_19_R1"}
```

## 别名 {#aliases}

- servernms
- nmsversion
