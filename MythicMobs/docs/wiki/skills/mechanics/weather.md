---
title: Weather
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/weather
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Weather {#weather}

## 说明 {#description}

更改施法生物所在世界的天气。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | t | 天气类型，可为 "sunny"、"rainy" 或 "stormy" | sunny |
| duration | d | 强制维持该天气的时间，以刻为单位 | 500 |

#### 天气类型 {#weather-types}

| 类型 | 别名 |
| --- | --- |
| **Sunny** | sun, clear |
| **Rainy** | rain |
| **Stormy** | storm, thunder |

## 示例： {#examples}

当生物生成时，会引发持续 10 分钟的风暴。

```yaml
Skills:
  - weather{type=storm;duration=6000} ~onSpawn
```
