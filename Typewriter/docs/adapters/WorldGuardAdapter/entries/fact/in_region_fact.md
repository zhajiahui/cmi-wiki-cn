---
title: 处于区域内事实（In Region Fact）
source: https://docs.typewritermc.com/adapters/WorldGuardAdapter/entries/fact/in_region_fact
source_version: 0.8.0
---

# 处于区域内事实（In Region Fact）

[事实](../../../../docs/creating-stories/facts.md)检查玩家是否位于特定区域。如果玩家不在该区域，则该值为`0`；如果玩家在该区域，则该值为`1`。

此事实仅供**读取**，无法写入，因此只适合用于条件判断。

## 用途示例 {#how-could-this-be-used}

这一事实可用于使任务仅在特定区域可用。

## 字段 {#fields}

## 备注（Comment）

继承 · 可选

用于跟踪该事实用途的注释。

## 组（Group）

必填

## 区域（Region）

必填

玩家必须所在的区域的名称。

---

原文：[In Region Fact](https://docs.typewritermc.com/adapters/WorldGuardAdapter/entries/fact/in_region_fact) · 文档版本：0.8.0
