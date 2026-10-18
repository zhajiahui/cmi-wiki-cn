---
title: Mythic 技能过场动画（Mythic Skill Cinematic）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/cinematic/mythicskill_cinematic
source_version: 0.8.0
---

# Mythic 技能过场动画（Mythic Skill Cinematic）

`Mythic Skill Cinematic`过场动画条目会在过场动画期间触发技能。

**注意**

技能本身需要使用`group=self`将组定义为自己

### 示例： {#example}

```text
- effect:particlesphere{particle=flame;amount=200;radius=2;group=self} @self
```

## 用途示例 {#how-could-this-be-used}

这可用于在过场动画中制作精美的粒子效果动画。

## 字段 {#fields}

## 条件（Criteria）

继承 · 列表

此条目触发前，玩家必须满足的事实条件列表。

## 片段（Segments）

必填 · 列表 · 片段

片段是过场动画中的一个时间区间，可在此期间执行动作或显示信息。

**说明**

同一条目中的片段无法重叠。需要重叠片段时，请新建条目。

---

原文：[Mythic Skill Cinematic](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/cinematic/mythicskill_cinematic) · 文档版本：0.8.0
