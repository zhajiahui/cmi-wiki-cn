---
title: Recoil
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Recoil
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Recoil {#recoil}

## 说明 {#description}

晃动目标的屏幕，模拟后坐力。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| recoil | r | 后坐力大小。 | 1 |
| pitch | p | 屏幕受后坐力影响的俯仰角（pitch）范围 | -10to10 |
| yaw | y | 屏幕受后坐力影响的偏航角（yaw）范围 | -0.25to0.25 |
| sneaking | sn | 玩家潜行时，pitch 和 yaw 的倍率 | 0.75 |
| sprinting | sp | 玩家冲刺时，pitch 和 yaw 的倍率 | 1.25 |

### Recoil 属性 {#recoil-attribute}

pitch 为负时向上后坐，为正时向下后坐。范围两端设为相同值，就会固定移动相同距离，例如 `pitch=-1to-1`。

## 示例 {#examples}

```yaml
  Skills:
  - recoil{r=1;pitch=-1to1} @self
```

## 别名 {#aliases}

- effect:recoil
- e:recoil
