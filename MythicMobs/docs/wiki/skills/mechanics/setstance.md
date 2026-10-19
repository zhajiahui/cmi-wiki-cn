---
title: Setstance
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setstance
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setstance {#setstance}

## 说明 {#description}

将目标 Mythic 生物的 stance 属性设为给定字符串。目标不是 Mythic 生物时不执行操作。

配合[姿态条件](../conditions/stance.md)，可为生物设置使用不同能力的姿态或阶段。姿态条件采用宽松匹配，例如当前姿态为 angry fiery explosive 时，检查 fiery 也会返回   true  。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| stance | s | 姿态的字符串名称 | default |

## 示例 {#examples}

此技能将施法者的阶段改为 bowphase。

```yaml
StanceChangeSkill:
  Skills:
  - setstance{stance=bowphase} @self
```

只有施法者的姿态为 bowphase 时，此技能才可使用。

```yaml
AnotherSkill:
  Conditions:
  - stance bowphase
  Skills:
  - ...some bow skills
```

## 别名 {#aliases}

- stance
