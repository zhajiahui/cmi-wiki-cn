---
title: "默认配置文件（旧版文档）"
source_url: "https://dev.bukkit.org/projects/protocollib/pages/configuration"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "ProtocolLib d89a5deb3eb625b16846da57fbbb04bfdd0d031d；官方 Wiki 与发布页 2026-10-19 快照"
---

# 默认配置文件（旧版文档）

默认配置文件：

```
global:
  # Settings for the automatic version updater
  auto updater:
    notify: true
    download: false
    
    # Number of seconds to wait until a new update is downloaded
    delay: 43200 # 12 hours
    # Last update time
    last: 0
 
  metrics: true
  
  # Automatically compile structure modifiers 
  background compiler: true
  
  # Disable version checking for the given Minecraft version. Backup your world first!
  ignore version check: 
  
  # Override the starting injecting method
  injection method:
```
