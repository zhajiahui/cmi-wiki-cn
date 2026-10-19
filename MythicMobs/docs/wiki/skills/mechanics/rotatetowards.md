---
title: Rotate Towards
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/RotateTowards
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Rotate Towards {#rotate-towards}

## 说明 {#description}

使施法者转向目标位置，每次变化不超过指定的最大偏航角或俯仰角增量。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| rotateyaw | yaw | 是否旋转 yaw（偏航角） | true |
| rotatepitch | pitch | 是否旋转 pitch（俯仰角） | false |
| useEyeLocation | uel | 是否以施法者眼睛的位置为基准，计算新的 yaw/pitch | false |
| maxyaw | my, y | yaw 的最大增量 | 0 |
| maxpitch | mp, p | pitch 的最大增量 | 0 |

## 示例 {#examples}

```yaml
SlowTurn:
  Skills:
  - rotatetowards{pitch=true;uel=true;maxyaw=1;maxpitch=0.5;repeat=199;repeatInterval=2} @Trigger ~onInteract
```

## 别名 {#aliases}

- rotateto
