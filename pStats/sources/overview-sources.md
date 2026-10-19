---
title: "pStats 官方资料摘录"
source_kind: plugin-overview
translation_review: reviewed
---

# pStats 官方资料摘录

核对日期：2026-10-19。随包形态为配置目录，没有独立 pStats JAR 的版本记录，组件版本未标明。

## 随包原始注释

一手来源为随包 pStats 配置中的原始注释。用途和网址原文如下：

> pStats collects some data for plugin authors like how many servers are using their plugins.

> Check out https://pstats.devs.beer/ to learn more :)

对应中文：为插件作者收集使用数据，例如有多少服务器使用其插件。此处只保留注释明确说明的统计用途，不补写具体采集字段。

## 注释指向的项目站点

来源：[pStats](https://pstats.devs.beer/)。核对时页面标题为 `pStats`，页面描述为：

> Statistiche aggregate pStats

该意大利语描述意为“pStats 汇总统计”。站点返回前端应用页面，本次未核实独立配置手册、管理命令、权限列表或完整采集字段。没有将同名的其他统计网站作为来源。

## 随包形态与依赖记录

随包清单列有 pStats 配置目录，未列出独立 pStats JAR；其他随包插件的 `depend` 与 `softdepend` 中均未出现 pStats。资料没有标明具体调用方或 SDK 版本，因此没有补写。
