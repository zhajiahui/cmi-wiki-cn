---
title: Targetwithin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/targetwithin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Targetwithin {#targetwithin}

## 说明 {#description}

检查目标的 AI 攻击目标是否在指定距离内。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| distance | d | 要检查的距离。 | 0 |

## 示例 {#examples}

```yaml
  Conditions:
  - targetwithin{d=10} true
```

> 检查施法实体的原版目标是否在 10 格内。

---

```yaml
  TargetConditions:
  - targetwithin{d=10} true
```

> 检查继承目标的原版目标是否在施法者 10 格内……虽然技术上可行，但最好别这样使用！
