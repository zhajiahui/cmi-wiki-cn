---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 5.5.0-SNAPSHOT-d89a5de
---

# config.yml

文件：`config.yml`。版本：`5.5.0-SNAPSHOT-d89a5de`。

主配置。

## `global` { #global }

```yaml title="config.yml · global"
global:
  # 自动版本更新器的设置。
  auto updater:
    notify: true
    download: false
    
    # 下载新更新前的等待时间，单位：秒。
    delay: 43200 # 12 小时
 
  metrics: true

  # 向拥有 protocol.info 权限的玩家显示某些警告。
  chat warnings: true
  
  # 自动编译结构修改器。
  background compiler: true
  
  # 对指定的 Minecraft 版本禁用版本检查。请先备份世界！
  ignore version check: 

  # 是否启用 filter 命令。
  debug: false
  
  # 是否为每条警告输出堆栈跟踪。
  detailed error: false
  
  # filter 命令使用的引擎。
  script engine: JavaScript
  
  suppressed reports:
```
