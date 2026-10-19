---
title: Totem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/totem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Totem {#totem}

## 说明 {#description}

图腾机制放置了一个看不见的“图腾”，类似于[弹射物](projectile.md)机制，只不过它不会移动。与弹射物非常相似，你可以使用onTick技能来创建效果来识别图腾的位置。

图腾会对进入指定半径的目标执行 onHit 技能，直到可用次数或持续时间耗尽。适合用粒子制作毒云、地雷等地面效果。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| Charges | ch, c | 图腾消失前可命中对象的次数 | 0 |
| YOffset | yo | 图腾生成位置相对于目标的高度 | 1 |
| stopatentity | se | 图腾命中实体后是否终止 | false |
| hugsurface | hs | 图腾是否贴合地面 | false |
| hugliquid | hugwater, huglava | 使用 hugSurface 时，液体是否也算作图腾可贴合的“表面” | false |
| heightfromsurface | hfs | HugSurface 设为 true 时，图腾高出所贴合表面的高度 | 0.5 |
| faceawayfromcaster | fafc | 初次放置图腾时是否背向施法者 | false |

> 继承[投射物](projectile.md)的属性

## 示例 {#examples}

```yaml
MyFirstTotem:
  Skills:
  - totem{ch=1;i=1;md=8;onTick=MFT_TICK} @self

MFT_TICK:
  Skills:
  - damage{a=3} @ENO{r=5}
```

## 别名 {#aliases}

- toteme
- t
