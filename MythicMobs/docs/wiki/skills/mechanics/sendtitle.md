---
title: Send Title
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/SendTitle
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Send Title {#send-title}

## 说明 {#description}

向所有目标玩家显示“标题”和/或“副标题”消息。如果目标不是玩家，则不执行任何操作。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| title | t | 要发送的标题字符串，必须用双引号包裹 |  |
| subtitle | st | 要发送的副标题字符串，必须用双引号包裹 |  |
| duration | d | 标题显示的时长，以刻为单位 | 1 |
| fadeIn | fi | 标题的淡入时间，以刻为单位 | 1 |
| fadeOut | fo | 标题的淡出时间，以刻为单位 | 1 |

## 示例 {#examples}

```yaml
  Skills:
  - sendtitle{title="Beware!";subtitle="A dangerous spell is being cast!";d=20} @PlayersInRadius{r=10}
  - ...
```

## 别名 {#aliases}

- title
