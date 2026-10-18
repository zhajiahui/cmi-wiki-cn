---
title: 解锁技能
source: https://docs.phoenixdevt.fr/mmocore/skills/unlocking
source_snapshot: '2026-10-19'
---

# 解锁技能 {#🔐-unlocking-skills}

每个技能都可以锁定、解锁但不可用、或可用。锁定技能意味着在玩家的技能UI 中看不到它，并且玩家不知道它的存在。当技能解锁时，它对玩家UI 可见，但只有在玩家满足与技能关联的等级要求时才能绑定到插槽。技能可以通过 [触发](../misc/triggers.md)（推荐）或 [命令](../general/commands.md)来解锁或锁定。

如果解锁了一个尚未在职业文件夹中填写信息的技能，该技能会直接视为可用，等级为 1，且无法继续升级。

---

原文：[🔐 Unlocking Skills](https://docs.phoenixdevt.fr/mmocore/skills/unlocking) · 原文归档：2026-10-19
