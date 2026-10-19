---
title: "自定义图表"
source_url: "https://bstats.org/docs/custom-charts"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方服务文档 2026-10-19 快照"
---

<a id="custom-charts"></a>

# 自定义图表

bStats 提供几种图表类型，可以接入你的 Metrics 实例。

<a id="basics"></a>

## 基础

添加自定义图表有两步：在插件代码中提供数据，并在网站上注册图表。

1. 进入插件页面，点击 **Edit（编辑）**。
2. 添加新图表，填入代码中使用的图表 ID。

<a id="pie-charts"></a>

## 饼图

适合配置选项等分类数据。简单饼图每台服务器记录一个值，高级饼图允许每台服务器提供多个值。

### Simple pie（简单饼图）

### Advanced pie（高级饼图）

<a id="drilldown-pie"></a>

## 下钻饼图

适合先把类别分组，再逐层查看细节。

点击扇区可查看详细信息。

<a id="drilldown-pie-1"></a>

### Drilldown pie（下钻饼图）

<a id="line-charts"></a>

## 折线图

用于跟踪随时间变化的趋势。单折线图适合玩家数、服务器数，或每个时间区间只有一个样本的指标。多折线图可以并排比较多个指标。

时间范围：1d、1w、1m、3m、1y、All。

### Single line chart（单折线图）

### Multi line chart（多折线图）

（注意：多折线图仍在开发中。）

<a id="bar-charts"></a>

## 柱状图

用于展示排名或选项使用情况。简单柱状图每个类别显示一个值，高级柱状图每个类别支持多根柱。

### Simple bar chart（简单柱状图）

### Advanced bar chart（高级柱状图）
