---
title: Lunarphase
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/lunarphase
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Lunarphase {#lunarphase}

## 说明 {#description}

检查当前月相

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| phases | p, phase | 要检查的一个或多个月相，可以是列表。 | 0 |

### Phase 属性 {#phase-attribute}

注意，**必须**使用月相编号。下图可以帮助你对应月相及编号。

| 阶段名称 | 阶段编号 |
| --- | --- |
| 满月 | 0 |
| 亏凸月 | 1 |
| 下弦月 | 2 |
| 残月 | 3 |
| 新月 | 4 |
| 蛾眉月 | 5 |
| 上弦月 | 6 |
| 盈凸月 | 7 |

## 示例 {#examples}

```yaml
  Conditions:
  - lunarphase{p=0} true
```

```yaml
  Conditions:
  - lunarphase{p=0,2,4,6} true
```
