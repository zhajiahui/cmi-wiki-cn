---
title: Currencygive
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/currencygive
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Currencygive {#currencygive}

## 说明 {#description}

给玩家钱。   该机制需要安装 Vault 插件和经济插件才能工作，并且必须在 MythicMobs `config-general.yml` 文件中启用 Vault

```yaml
    Vault:
      Enabled: true
```

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| amount | a | 货币数量。 | 0.0 |

## 示例 {#examples}

```yaml
  Skills:
  - currencygive{amount=20} @pir{r=20} ~onSpawn 0.2
```

执行时，生成生物周围 20 格内的每个玩家，都有 20% 的概率获得 20 金钱。

## 别名 {#aliases}

- giveCurrency
