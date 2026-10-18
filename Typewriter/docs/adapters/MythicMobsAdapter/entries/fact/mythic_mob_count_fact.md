---
title: 生物数量事实（Mob Count Fact）
source: https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/fact/mythic_mob_count_fact
source_version: 0.8.0
---

# 生物数量事实（Mob Count Fact）

一个[事实](../../../../docs/creating-stories/facts.md)代表世界上有多少个特定的MythicMobs生物。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

当 Boss 存在时，这一事实可用于更改 NPC 或生物发出的对话。如果一个或多个生物存在/不存在，它也可以与“生成生物”操作结合使用来生成特定的生物。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 生物名称（Mob Name）

必填

要计数的生物的ID

---

原文：[Mob Count Fact](https://docs.typewritermc.com/adapters/MythicMobsAdapter/entries/fact/mythic_mob_count_fact) · 文档版本：0.8.0
