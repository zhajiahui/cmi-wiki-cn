---
title: Chain
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/chain
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Chain {#chain}

## 说明 {#description}

连锁允许你制作在目标之间反弹的技能，例如“连锁闪电”类型的技能。

BounceConditions 在技能的每次“反弹”后进行评估。举个例子，如果有人在墙的另一边，但你站在门口，那么它可能会从你那里弹到他们那里，因为它会绕着墙弹跳

每次施法只会对同一实体跳转一次。每次跳转时，当前实体成为技能原点，onBounce 的继承目标则是下一次跳转的实体，因此可用 fromOrigin 制作效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onBounce | ob, m, meta, onbounceskill, ontick, ontickskill, ot, s, skill | 在目标之间跳转的技能。 |  |
| bounces | b | 连锁跳转的次数。 | 2 |
| delay | d, bd, bouncedelay, i, interval | 两次跳转之间的延迟。 | 1 |
| radius | r, bounceradius, bouncerange, range | 技能跳转到新目标的最大距离。 | 5 |
| hitSelf | hs | 连锁是否影响施法者。 | false |
| hitTarget | ht | 连锁是否先从施法者传递至第一个目标。 | true |
| hitPlayers | hp | 连锁是否跳转至玩家。 | true |
| hitNonPlayers | hnp | 连锁是否跳转至非玩家实体。 | false |
| bounceConditions | conditions, cond, c | 应用于跳转目标的条件。 |  |

## 示例 {#examples}

```yaml
Skills:
- chain{
    bounces=5;
    bounceRadius=10;
    bounceDelay=1;
    hitSelf=false;
    hitPlayers=true; 
    hitNonPlayers=true;
    hitTarget=true;
    onBounce=[
      - effect:particleline{p=flame;fromOrigin=true}
    ];
    bounceConditions=[
      - inlineofsight
      - hasaura{aura=damageResist} false
    ];
  } @target ~onTimer:20
```
