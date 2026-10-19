---
title: Forward
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Forward {#forward}

## 说明 {#description}

瞄准施法者前方的位置

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| forward | f, amount, a | 目标点应距离多远。 | 5 |
| rotate | rot | 目标位置绕施法者的旋转角度。 | 0 |
| useeyelocation | uel | 是否使用眼睛位置作为目标选择器的基准。 | false |
| lockpitch |  | 是否按施法者俯仰角为 0 的情况选择目标位置。 | false |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - effect:particles @Forward{f=3;uel=true;rot=10}
```
