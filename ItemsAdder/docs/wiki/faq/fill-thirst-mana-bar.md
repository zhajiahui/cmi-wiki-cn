---
title: "口渴/魔力条"
source_url: "https://wiki.itemsadder.com/faq/fill-thirst-mana-bar"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 口渴/魔力条

## 填充它们

要填充口渴条，使用 `/iaplayerstat write LoneDev thirst float 10`

![](../assets/28de373ab36ec4dd889b.png)

要填充魔力条，使用 `/iaplayerstat write LoneDev mana float 5`

![](../assets/5cc4d25770c093964c53.png)

## 禁用口渴

* 打开 `contents/iasurvival/configs/thirst/hud_thirst.yml`
* 设置 `enabled: false`
* 使用 `/iareload` 命令

## 禁用魔力

* 打开 `contents/iaalchemy/configs/huds/huds.yml`
* 设置 `enabled: false`
* 使用 `/iareload` 命令
