---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 0.9.0-beta-177
---

# config.yml

文件：`config.yml`。版本：`0.9.0-beta-177`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `enabled` { #enabled }

```yaml title="config.yml · enabled"
# 是否启用网页面板和 WebSocket。
enabled: true
```

## `panel` { #panel }

```yaml title="config.yml · panel"
panel:
  enabled: true
  # 网页面板使用的端口，请确保该端口已开放。
  port: 28080
```

## `websocket` { #websocket }

```yaml title="config.yml · websocket"
websocket:
  # WebSocket 服务使用的端口，请确保该端口已开放。
  port: 29092
  # 连接时使用的身份验证方式。不清楚用途时请保持默认。
  # 可用值：none（不建议）、session
  auth: session
```

## `hostname` { #hostname }

```yaml title="config.yml · hostname"
# 服务器的主机地址，请改为你的服务器 IP。
hostname: "HOST"
```
