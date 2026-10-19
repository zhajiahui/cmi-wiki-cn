---
title: Currencytake
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/currencytake
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Currencytake {#currencytake}

## 说明 {#description}

从玩家那里拿钱。   该机制需要安装 Vault 插件和经济插件才能工作。它还需要在 [config.yml](../../configuration.md) 中启用 Vault

```yaml
        Vault:
          Enabled: true
```

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 从玩家处扣除的货币数量。 | 0.0 |

## 示例 {#examples}

该技能会夺走20范围内所有玩家的20金钱。

```yaml
  Skills:
  - currencytake{amount=20} @pir{r=20} ~onSpawn
```

## 别名 {#aliases}

- takeCurrency
