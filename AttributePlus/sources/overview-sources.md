---
title: AttributePlus 概览来源
source_kind: plugin-overview
translation_review: reviewed
---

# AttributePlus 概览来源

核对日期：2026-10-19。概览对应随包版本 3.3.3.6；没有进行游戏内运行验证。

## 作者原帖

公开链接：[AttributePlus 3.3.3.6 作者原帖](https://www.mcbbs.co/thread-43-1-1.html)。已取得帖子正文，而非仅搜索摘要。原帖直接链接下方官方 GitBook。

原文摘录：

> 基于 Kotlin / Taboolib 开发的玩家属性插件，拥有 新机制、优先级、自定义属性 功能
>
> 从 3.0.9 版本起支持使用 JavaScript 自定义属性脚本

这些内容用于确认插件定位和脚本支持。原文本来就是中文，概览只调整语序，不另编教程。

## 官方首页

公开链接：[AttributePlus Pro](https://ersha.gitbook.io/attributeplus-pro)。

原文摘录：

> 插件软依赖 MythicMobs
>
> 插件硬依赖 PlaceholderAPI
>
> 插件拥有 40+ 种属性，多种条件判断，每种属性都可以设置 优先级、战斗力、部分属性还支持自定义公式
>
> 所有的属性均支持 小数点、负数、随机值
>
> 同时属性还可以作用到怪物上。

用于简介及 PlaceholderAPI、MythicMobs 的依赖核对。

## 官方命令页

公开链接：[插件相关](https://ersha.gitbook.io/attributeplus-pro/cha-jian-pei-zhi)，[同页 Markdown](https://ersha.gitbook.io/attributeplus-pro/cha-jian-pei-zhi.md)。

原文摘录：

> 建议在游戏内输入 `/ap` 命令，来查看命令详细介绍

| 原文命令 | 原文说明 |
| --- | --- |
| `ap stats` | 打开属性统计面板 |
| `ap update [player]` | 刷新玩家属性 |
| `ap source [player]` | 查看玩家属性来源 |
| `ap persistent [player] [...] ...` | 新增持久化属性源 (可给临时属性,永久属性) |
| `ap del-persistent [player] [source]` | 删除一个持久化属性源 |
| `ap reload` | 重载插件 |

此页没有列出确切的管理命令权限节点，因此概览没有补造节点。

## 随包描述信息

以下为该版本 JAR 描述信息的核对摘要：

```yaml
name: AttributePlus
version: 3.3.3.6
depend: [PlaceholderAPI]
softdepend: [MythicMobs, MythicLib, CMI, CMILib, CMIEInjector, SkillAPI, HolographicDisplays]
```

## 版本差异

官方 GitBook 首页写支持 1.8 ~ 1.21.11，作者原帖现写 1.8 至 26.2。概览未据此给出该 JAR 的确定兼容范围。GitBook 没有固定到 3.3.3.6 的独立标签。
