---
title: 处于过场动画中事实（In Cinematic Fact）
source: https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/in_cinematic_fact
source_version: 0.8.0
---

# 处于过场动画中事实（In Cinematic Fact）

“In Cinematic Fact”是一个事实，如果玩家有活动的过场动画，则返回 1，否则返回 0。

如果没有引用过场动画，它将根据是否有任何过场动画处于活动状态进行过滤。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

可根据这个事实，限制条目仅在玩家没有正在播放的过场动画时执行。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 启动过场动画

必填

未设置时，它将根据是否有任何动画处于活动状态进行过滤。

---

原文：[In Cinematic Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/in_cinematic_fact) · 文档版本：0.8.0
