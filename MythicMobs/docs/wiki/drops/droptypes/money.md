---
title: 金钱
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/Money
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 金钱 {#money}

## 说明 {#description}

掉落时，如果触发者是玩家，就会获得 `Vault` 插件提供的货币。奖励消息中可以使用 `<drop.amount>` [占位符](../../skills/placeholders.md#misc-placeholders)获取发放的金额。这条消息可以在 `config-general.yml` 文件中配置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| sendmessage | sm | 是否向玩家发送预先配置的消息 | true |

## 示例 {#examples}

```yaml
  Drops:
  - money 20
```

## 别名 {#aliases}

- vault
- currency
