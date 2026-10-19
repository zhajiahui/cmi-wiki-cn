---
title: Switch
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Switch
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Switch {#switch}

## 说明 {#description}

switch 根据一组 case 值逐项匹配条件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| uniqueresult | unique, first | 满足条件后，是否停止执行其他技能 | true |
| condition |  | 要检查的条件 |  |
| cases |  | 要逐项判断的分支列表 |  |

## 示例 {#examples}

```yml
MyCoolMob:
  Type: ZOMBIE
  Skills:
    - switch{condition=entitytype{t=<case>};cases=
        case SKELETON=[
          - message{m="A SKELETON JUST HIT ME"} @Server
          ]
        case HUSK=[
          - message{m="A HUSK JUST HIT ME!"} @Server
          ]
        case PIG=[
          - message{m="NOOO A PIG"} @Server
          ]
        case DEFAULT=[
          - message{m="SOMEONE or SOMETHING HIT ME OUT OF NOWHEREE!!"} @Server
          ]
      } @trigger ~onDamaged
```
