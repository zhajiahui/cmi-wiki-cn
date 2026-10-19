---
title: Fake Lightning
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FakeLightning
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fake Lightning {#fake-lightning}

## 说明 {#description}

会向指定目标发出“假”闪电。

该效果纯粹是装饰性的，它会播放闪电音效，但不会对目标造成任何类型的伤害。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| localized | l | 是否仅让指定半径内的玩家看到或听到闪电。 | false |
| localizedradius | lr, r | 局部效果的半径，仅在 localized 设为 true 时生效！ | 128 |

## 示例 {#examples}

```yaml
SuperLightningSkill:
  Skills:
  - fakelightning @target
  - fakelightning @self
  - fakelightning{repeat=20;repeatInterval=1} @PIR{r=100}
```

## 别名 {#aliases}

- effect:lightning
- e:lightning
