---
title: "保护资源包"
source_url: "https://wiki.itemsadder.com/other/resourcepack-protection"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 保护资源包

#### 免责声明

资源包无法做到 100% 有效保护，因为游戏必须能够正确解压资源包，才能显示纹理。

这个功能是预防措施，防止小朋友或其他不怀好意的人偷取你的纹理。\
一些有经验的用户可能可以找到绕过这些保护方法的措施。

ItemsAdder 尽最大努力防止该情况，但仍请记住这并非完全有效。

其他插件也有相同限制，并非 ItemsAdder独有。

要借助 ItemsAdder 你可以防止你的资源包被解压、盗窃。你只需要在 `config.yml` 中启用该设置，并再次使用 `/iazip`。

如果使用[外部托管](../plugin-usage/plugin-configuration/resourcepack-hosting.md)（如 [Dropbox](../plugin-usage/plugin-configuration/resourcepack-hosting/dropbox.md)），记得重新上传资源包并更新 `config.yml`。

```yaml
  zip:
    protect-file-from-unzip:
      protection_1: true
      protection_2: true
      protection_3: true
```

#### `protection_1`

使用基础方法保护资源包。

#### `protection_2`

使用另一层保护来保护资源包，防止其他解压资源包的方法。

#### `protection_3`

目前未知。

## 展示

这个趣味演示展示了用户试图窃取数据时会看到的内容。实际显示效果正是如此：一组损坏的文件和文件夹。


## 保护 self-host 资源包免受 DDoS 攻击

仅在 ItemsAdder 4.0.8 中可用

此功能用于缓解熊孩子和恶意捣乱者试图拖慢服务器的问题。

```yaml
self-host:
  enabled: false
  server-ip: '127.0.0.1'
  pack-port: 8163
  append-port: true
  protection:
    block_non_game_requests: false
    rate_limit:
      enabled: true
      max_requests: 3
      period_seconds: 2
      cooldown:
        enabled: true
        duration_minutes: 30
        trigger_on_failed_times: 5
```

#### `protection`

本节包含用于防止滥用和未经授权请求的安全设置。

***

#### `block_non_game_requests`

**默认：**`false`\
阻止来自于浏览器或自动服务对资源包地址的访问（如用来 DDoS 你服务器的控制台指令）。

***

#### `rate_limit`

该设置帮助阻止可能为自动进行的频繁性请求，如 DDoS 攻击。

**`enabled`**

**默认：**`true`\
决定是否启用请求速率限制。

**`max_requests`**

**默认：**`3`\
在 `period_seconds` 时间范围内，触发限制前允许的最大请求数。

**`period_seconds`**

**默认：**`2`\
统计请求数的时间窗口（单位：秒）。如果客户端在此期间超过 `max_requests`，则计为一次**失败尝试**。

***

#### `cooldown`

该部分控制忽视多次未通过请求速率检查的客户端再次进行请求的时间。

**示例：**\
如果用户在 **2 秒内发送超过 3 次请求**，并且重复 **5 次**，之后的请求会被封禁 **30 分钟**。

**`enabled`**

**默认：**`true`\
决定是否暂时忽略超出请求限制的客户端。

**`duration_minutes`**

**默认：**`30`\
以分钟计，客户端超出 `trigger_on_failed_times` 限制后，忽略客户端请求的时间。

**`trigger_on_failed_times`**

**默认：**`5`\
客户端在短时间内超过请求限制多少次后，会触发冷却。
