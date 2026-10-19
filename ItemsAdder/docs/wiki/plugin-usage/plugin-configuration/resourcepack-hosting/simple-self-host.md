---
title: "简易自托管"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/resourcepack-hosting/simple-self-host"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 简易自托管

此功能需要 ItemsAdder 4.0.17 或更高版本

这是应用资源包的新方法。它即插即用，无需设置或端口转发。

只需禁用所有其他托管方法，在 `config.yml` 中启用 `simple_self_host`，然后使用 `/iazip` 生成资源包。

如果愿意，可以在 `server_address` 字段中指定服务器地址 + 端口，不过通常没有必要。

```yaml
hosting:
  simple_self_host:
    enabled: true
    server_address: auto
    optimization:
      block_non_game_requests: true
      max_downloads_per_ip: 5
      max_speed_in_megabyte_ps: 30
```
