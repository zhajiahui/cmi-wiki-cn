---
title: Living In Cone
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Living In Cone {#living-in-cone}

## 说明 {#description}

选中圆锥体内的所有活体实体，可指定圆锥的角度、长度及其相对于朝向的旋转角度

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| angle | a | 锥体的角度。 | 90 |
| range | r | 锥体的长度。 | 16 |
| rotation | rot | 锥体的旋转角度。 | 0 |
| usepitch | pitch, p | 生成锥体时是否也考虑施法者的俯仰角。 | false |
| yoffset | yo | 添加到所生成锥体位置的 y 轴偏移。 | 0 |
| livingonly | lo | 是否只选中活体实体 | true |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - ignite @LivingInCone{a=45;r=20}
```

## 别名 {#aliases}

- entitiesInCone
- livingEntitiesInCone
- LEIC
- EIC
