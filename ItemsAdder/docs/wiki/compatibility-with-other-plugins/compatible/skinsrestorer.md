---
title: "SkinsRestorer"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/skinsrestorer"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# SkinsRestorer

## [此处下载](https://www.spigotmc.org/resources/skinsrestorer.2124/)

## 如何修复加入时未能自动应用资源包

### 步骤 1

安装 [**ResourcepackBroadcast**](https://www.spigotmc.org/resources/resourcepackbroadcast.88318/)

### 步骤 2

设置 **ResourcepackBroadcast** 的 `config.yml` 以在资源包正确加载后运行 `sr applyskin`：

```yaml
success:
  enabled: true
  message:
    enabled: true
    text: "&e%player_name% loaded resourcepack"
  placeholder:
    enabled: true
    text: "%img_smile%"
  commands:
    apply_skin:
      enabled: true
      command: sr applyskin %player_name%
      as_console: true
```

### 步骤 3

打开 **SkinsRestorer** 的 `config.yml` 并设置 `DisableOnJoinSkins: false`

### 步骤 4

安装 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)（如果尚未安装）。\
先执行命令 `/papi ecloud download Player`，再执行 `/papi reload`。

### 完成
