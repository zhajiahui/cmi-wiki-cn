---
title: Not Living Near Origin
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/NotLivingNearOrigin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Not Living Near Origin {#not-living-near-origin}

## 说明 {#description}

以原点附近半径范围内的所有非生物实体为目标

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 目标选择器的半径。 | 5 |

## 示例 {#examples}

此机制结束时，会在全局聊天中显示其周围半径 10 格内所有非活体实体的 UUID

```yaml
ExampleSkill:
  Skills:
  - projectile{...;
    onEnd=[
      - command{c="say <target.uuid>"} @NotLivingNearOrigin{r=10}
    ]}
```

## 别名 {#aliases}

- nonLivingNearOrigin
- NLNO
