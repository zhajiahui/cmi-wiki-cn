---
title: "属性类型"
source_url: "https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben/shu-xing-lei-xing"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方持续更新 Wiki；2026-10-19 快照；未固定到随包 3.3.3.6"
---

# 属性类型

## 介绍

AttributePlus 属性由 `ATTACK DEFENSE RUNTIME UPDATE OTHER` 五个类型组成

使用属性脚本编写时，需要编写不同方法名内的逻辑作为属性执行逻辑

|         |                                                   |
| ------- | ------------------------------------------------- |
| ATTACK  | function runAttack(attr, attacker, entity, ha...) |
| DEFENSE | function runDefense(attr, entity, killer, handle) |
| KILLER  | function runKiller(attr, killer, entity, handle)  |
| UPDATE  | function run(attr, entity, handle)                |
| RUNTIME | function run(attr, entity, handle)                |
| OTHER   | 无需编写                                              |

可以查看 [脚本教学](shou-ba-shou-jiao-ni-xie-shu-xing-jiao-ben.md) 页面内的属性示例

**KILLER** 类型 **JavaScript** 自定义属性脚本示例：传送门
