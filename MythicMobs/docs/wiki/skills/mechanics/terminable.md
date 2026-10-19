---
title: Terminable
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/terminable
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Terminable {#terminable}

## 说明 {#description}

创建[光环](aura.md)，每个游戏刻检查一组条件；条件满足时，立即取消 onStart 技能的执行。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| terminateconditions | conditions, cond, c | 要检查的条件 |  |
| deep |  | 可终止光环的条件满足后，是否同时停止执行调用该光环的[元技能](../metaskills.md) | false |
| onterminate | ox | onStart 终止后执行的[元技能](../metaskills.md) |  |

> 该机制继承了[光环](aura.md)机制的所有属性

### Deep 属性 {#deep-attribute}

deep 属性较为特殊：启用后，终止光环不仅影响 onStart 元技能，还会影响它最初调用的元技能。例如：

```yaml
ExampleSkill:
  Skills:
  - terminable{deep=true;...}
  - skill:test1
  - delay 100
  - mechanic2

SecondarySkill:
  Skills:
  - mechanic1
  - delay 200
  - mechanic3
```

然后，如果可终止光环满足其条件，则`ExampleSkill`和随后调用的`SecondarySkill`元技能将被停止：因此，例如，如果可终止光环在10游戏刻后停止执行，`mechanic2`或`mechanic3`都不会被触发

## 示例 {#examples}

```yaml
  Skills:
  - terminable{
    auraName=exampleAura;
    d=2000;
    conditions=[
      - health{h=<50} true
    ];
    onStart=[
    - state{s=charged_attack}
    - delay 20
    - skill{s=ChargedAttackDamage}
    ];
    onTerminate=[
    - state{s=charged_attack;remove=true}
    - state{s=stunned}
    ]} @self
```

## 别名 {#aliases}

- stoppable
- cancelable
- exit
- terminatable
