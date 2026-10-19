---
title: Setmaxhealth
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setmaxhealth
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setmaxhealth {#setmaxhealth}

## 说明 {#description}

设置目标实体的最大生命值。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 设置最大生命值时使用的数值 | 1.0 |
| mode | m | 最大生命值的设置方式。`STATIC` 直接将最大生命值设为 amount 的值；`SCALE` 设置新的最大生命值，同时相应缩放实体当前的生命值 | STATIC |

## 示例 {#examples}

本例将实体的新最大生命值设为 5。如果新上限低于当前生命值，当前生命值会降至新上限。

```yaml
  Skills:
  - setmaxhealth{amount=5;mode=STATIC} @self ~onInteract
  - ...
```

##  {#section}

本例将生物最大生命值改为 5，并按比例调整剩余生命值。原本为 15/20 时，交互后会变为 3/5，而非 5/5。

```yaml
  Skills:
  - setmaxhealth{amount=5;mode=SCALE} @self ~onInteract
  - ...
```

## 别名 {#aliases}

- setmaxhp
