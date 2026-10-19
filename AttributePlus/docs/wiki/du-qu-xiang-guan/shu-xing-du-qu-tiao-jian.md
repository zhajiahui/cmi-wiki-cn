---
title: "属性内嵌条件格式"
source_url: "https://ersha.gitbook.io/attributeplus-pro/du-qu-xiang-guan/shu-xing-du-qu-tiao-jian"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方持续更新 Wiki；2026-10-19 快照；未固定到随包 3.3.3.6"
---

# 属性内嵌条件格式

新版特色 / 3.1.9 版本起

## 内嵌**读取条件**

自带的属性读取格式有一个额外的 **读取条件** 当 **满足该条件时属性才会被读取**\
你也可以为你服务器开发更多不同的**内嵌条件 (**[**开发文档**](../kai-fa-wen-dang/descriptionlinecondition.md)**)**\
\
**格式为** "<属性内容> **/** **<条件>**"\
条件必须写在 / 右边,否则不生效<br>

| 类型       | 说明             |
| -------- | -------------- |
| Lv.<值>   | 使用者等级必须满足才会读取  |
| Gm.<权限名> | 使用者必须拥有该权限才会读取 |

具体用法，你只需要在物品属性Lore上加 **对应类型的读取条件** 即可，例如 **"物理伤害: 1000 / Lv.1000"** 那么装备使用者等级必须大于等于 1000 该属性条目才会生效

![](../assets/739acad053635d32.png)

![](../assets/954ae1e0c420a2f7.png)

![](../assets/cbaed888cc63ad50.png)
