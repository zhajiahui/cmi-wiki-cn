---
title: Play Animation
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayAnimation
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Play Animation {#play-animation}

## 说明 {#description}

强制实体播放动画

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| animation | a, effect, e | 要播放的动画。 | 1 |
| audience |  | 效果的[可见对象]。 | world |

### Animation 属性 {#animation-attribute}

| ID | 动画 |
| --- | --- |
| 0 | 挥动主手臂。 |
| 1 | 受到伤害。 |
| 2 | 离开床。 |
| 3 | 挥动副手臂。 |
| 4 | 暴击效果。 |
| 5 | 魔法暴击效果。 |

## 示例 {#examples}

导致施法者摆动手臂。

```yaml
SwingSkill:
  Skills:
  - playanimation{a=0;audience=World} @Self
```

## 别名 {#aliases}

- effect:playanimation
- e:playanimation
- playarmanimation
