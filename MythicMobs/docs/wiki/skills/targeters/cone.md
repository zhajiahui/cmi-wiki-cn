---
title: Cone
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Cone
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Cone {#cone}

## 说明 {#description}

选中施法者前方圆锥体内的随机点。注意：圆锥体固定在 y 轴上，无法向上或向下旋转

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| angle | a | 锥体的角度。 | 90 |
| range | r | 锥体的长度。 | 16 |
| points | p | 在锥体内部选择为目标的点数。 | angle*range*0.1 |
| slices | s | 定义沿锥体长度或范围将其划分为多少层或切片。切片越多，分辨率越精细。 | floor(`range`) |
| minpoints | mp | 每个切片生成的最少点数。 | 1 |
| rotation | rot | 锥体的旋转角度。 | 0 |
| yoffset | yo, y | 锥体的 y 轴偏移。 | 0 |
| exact | e | 是否使用精确方法将点均匀分布在锥体表面，而不是随机生成。 | false |

## 示例 {#examples}

```yaml
  Skills:
  - effect:particles @Cone{a=45;r=10;p=200}
```
