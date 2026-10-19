---
title: AttributePlus 插件简介
source_kind: plugin-overview
translation_review: reviewed
---

# AttributePlus

AttributePlus 是玩家属性插件，支持属性优先级、战斗力、条件判断和自定义属性。属性值可使用小数、负数和随机值，部分属性支持自定义公式；也可以用 JavaScript 编写属性脚本。属性还可以作用于怪物。以上功能见[作者原帖](https://www.mcbbs.co/thread-43-1-1.html)及[官方文档](https://ersha.gitbook.io/attributeplus-pro)。

本次随包版本为 **3.3.3.6**。官方 Pro 文档持续更新，未单独固定到这一版本。

## 依赖

随包版本声明的必需插件为 **PlaceholderAPI**，官方首页也明确将其列为硬依赖。

软依赖为 MythicMobs、MythicLib、CMI、CMILib、CMIEInjector、SkillAPI、HolographicDisplays。软依赖表示可选联动，不表示需要全部安装。

## 核心命令

以下内容依据[官方命令说明](https://ersha.gitbook.io/attributeplus-pro/cha-jian-pei-zhi)，保留原文的参数记号。官方建议在游戏中输入 `/ap` 查看详细帮助。

| 命令 | 用途 |
| --- | --- |
| `/ap` | 查看命令帮助 |
| `/ap stats` | 打开属性统计面板 |
| `/ap update [player]` | 刷新玩家属性 |
| `/ap source [player]` | 查看玩家属性来源 |
| `/ap persistent [player] [...] ...` | 添加持久化属性源，可设置临时或永久属性 |
| `/ap del-persistent [player] [source]` | 删除持久化属性源 |
| `/ap reload` | 重载插件 |

该官方页面未列出这些命令的确切权限节点，因此这里不补列权限。

## 官方资料

- [作者发布页](https://www.mcbbs.co/thread-43-1-1.html)
- [AttributePlus Pro 官方文档](https://ersha.gitbook.io/attributeplus-pro)
- [官方命令说明](https://ersha.gitbook.io/attributeplus-pro/cha-jian-pei-zhi)

[查看配置文件及中文说明](configuration/index.md)。
