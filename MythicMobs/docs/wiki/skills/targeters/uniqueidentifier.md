---
title: Unique Identifier
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/UniqueIdentifier
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Unique Identifier {#unique-identifier}

## 说明 {#description}

按 UUID 选中特定实体，支持占位符。uuid 选项也支持用逗号分隔多个 UUID，同时选中多个实体。无效的 UUID 会被静默跳过。此目标选择器不受目标过滤器限制，可以选中任何实体

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| uuid | u | 实体的 uuid，可以是以逗号分隔的 uuid 列表。 | 0 |

## 示例 {#examples}

下面的生物会记住生成后第一个攻击它的实体的 uuid，此后每隔 10 秒点燃该实体一次

```yaml
VengefulMob:
  Type: ZOMBIE
  Skills:
  - setvariable{var=caster.targetedentity;type=STRING;val=<trigger.uuid>} @self ~onDamaged =100% ?~isLiving
  - ignite @UniqueIdentifier{uuid=<caster.var.targetedentity>} ~onTimer:200 ?variableisset{var=caster.targetedentity}
```

也可以用逗号分隔，一次传入多个 UUID，在一次技能中选中所有匹配的实体。下面的示例会按 UUID 点燃三个实体。

```yaml
IgniteMany:
  Skills:
  - ignite @UUID{u="9b7f8e2a-1c3d-4e5f-8a90-1234567890ab,3f2c1d0e-5a6b-7c8d-9e0f-abcdef012345,0a1b2c3d-4e5f-6789-0abc-def012345678"}
```

## 别名 {#aliases}

- uuid
