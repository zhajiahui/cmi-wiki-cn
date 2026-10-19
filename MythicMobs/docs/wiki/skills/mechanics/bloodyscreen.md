---
title: Bloody Screen
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BloodyScreen
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Bloody Screen {#bloody-screen}

## 说明 {#description}

显示接近世界边界时的画面效果，玩家必须开启精美画质才能看到。

注意：带有此效果的玩家无法在技能中使用 "onUse" 触发器。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d | 效果生效的时间，单位为刻。 | 20 |
| cancel | c | 为 true 时，停止所有现有的 redscreen 效果。 | false |

## 示例 {#examples}

```yaml
BloodyEffect:
  Skills:
  - effect:bloodyScreen{d=25} @PIR{r=15} ~onTimer:20
```

## 别名 {#aliases}

- effect:bloodyScreen
- e:bloodyScreen
- redScreen
- effect:redScreen
- e:redScreen
