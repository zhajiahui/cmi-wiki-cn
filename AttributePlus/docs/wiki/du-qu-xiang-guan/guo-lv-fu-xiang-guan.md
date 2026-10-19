---
title: "过滤符相关"
source_url: "https://ersha.gitbook.io/attributeplus-pro/du-qu-xiang-guan/guo-lv-fu-xiang-guan"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方持续更新 Wiki；2026-10-19 快照；未固定到随包 3.3.3.6"
---

# 过滤符相关

3.1.1 版本开始

| 过滤符 | 作用                    |
| --- | --------------------- |
| &-  | 该行描述将不会读取属性           |
| &\| | 只读取过滤符左遍内容            |
| §<  | 只读取过滤符左遍内容 (与 §\| 相同) |
| §>  | 只读取过滤符右遍内容            |

## 例子

"**&-**&#x7269;理伤害: 1000" 那么该行描述上的属性就 **不会读取**\
**"**&#x7269;理伤害+ 999 **&<**(战斗力999)" 那么该行描述只读取 **"物理伤害+ 999"** 内容\
\
请配合物品制造(**例如 MythicMobs 的物品库功能**)插件使用，在游戏内使用 **/lore add &-物理伤害: 100** 是无效的
