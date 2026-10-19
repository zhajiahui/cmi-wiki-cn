---
title: Open Trades
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OpenTrades
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Open Trades {#open-trades}

## 说明 {#description}

向目标玩家开放施法村民的交易

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| realTrade | real | 是否打开实际村民的交易而不是交易副本，以免影响施法村民。 | true |

## 示例 {#examples}

```yaml
  Skills:
  - opentrades @PIR{r=10;limit=1;sort=NEAREST}
```

## 别名 {#aliases}

- opentrade
- trade
