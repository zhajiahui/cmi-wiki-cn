---
title: "CMI"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/cmi"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# CMI
## Rank 功能

1. 打开 CMI 文件夹中的 `Settings/Chat.yml` ，设置 `GeneralFormat` （我使用了 `%vault_prefix%` 占位符，而非 CMI 的 `{prefix}`）为如下内容：

```yaml
GeneralFormat: '%vault_prefix% &f{displayName}&7: &r{message}'
```

2\. 下载 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) 与 [Vault](https://github.com/MilkBowl/Vault/releases/latest)。\
3\. 安装它们并重启服务器\
4\. 输入指令 `/papi ecloud download Vault`。\
5\. 最后，输入指令 `/papi reload`。

ItemsAdder 现在应该正常与 CMI 的聊天功能工作。
