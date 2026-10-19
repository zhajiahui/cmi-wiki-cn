---
title: Fieldofview
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/fieldofview
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fieldofview {#fieldofview}

## 说明 {#description}

测试目标是否位于施法者所观察的给定角度内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| angle | a | 要检查的视野角度。 | 90 |
| rotation | r | 旋转要检查的视野。 | 0 |

## 示例 {#examples}

```yaml
  TargetConditions:
  - fieldofview{angle=90} false
```

此条件将过滤掉施法者 90 度视野内的所有目标。

##  {#section}

```yaml
  TargetConditions:
  - fieldofview{angle=90} true
```

此条件将允许仅定位施法者视野90度范围内的实体。

## 别名 {#aliases}

- infieldofview
- fov
