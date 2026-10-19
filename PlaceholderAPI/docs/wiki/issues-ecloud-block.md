---
title: eCloud 连接被阻止
source_url: https://wiki.placeholderapi.com/issues/ecloud-block/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="ecloud-connection-blocked"></a>
# eCloud 连接被阻止

如果无法通过 PlaceholderAPI 下载占位符扩展，服务器可能无法连接到 PlaceholderAPI Expansion Cloud（eCloud）。这通常是服务器托管商、防火墙或互联网服务提供商（ISP）的网络限制造成的。

<a id="symptoms"></a>
## 问题表现

常见表现包括：

- 游戏内的消息引导你访问此页面。
- `/papi ecloud download/update <expansion>` 执行失败（超时、报错、连接被拒绝或类似情况）。

<a id="why-it-happens"></a>
## 问题原因

下载命令需要服务器通过 HTTPS 向 PlaceholderAPI 的 eCloud API 发起出站连接。以下因素可能阻止连接：

- 服务器托管商的防火墙或安全策略
- 服务器所在机器的本地防火墙
- 网络防火墙（数据中心、路由器）
- DNS 过滤或 ISP 封锁

<a id="domains-placeholderapi-uses"></a>
## PlaceholderAPI 使用的域名

请允许通过 HTTPS（TCP 443）向以下域名发起出站连接：

- PlaceholderAPI **< 2.12.0** 使用 `api.extendedclip.com`
- PlaceholderAPI **>= 2.12.0** 使用 `*.placeholderapi.com`

<a id="fix-options"></a>
## 解决方法

<a id="1-ask-your-host-to-unblock-the-ecloud"></a>
### 1) 请服务器托管商解除对 eCloud 的限制

如果使用共享主机或托管服务，你可能无法自行更改防火墙规则。请联系服务器托管商，要求允许向上述域名发送出站 HTTPS 请求。

<a id="2-check-firewalls-filters-you-control"></a>
### 2) 检查由你管理的防火墙和过滤规则

如果服务器由你自行管理，请检查所有出站过滤规则：

- 操作系统防火墙规则（Windows 防火墙 / `ufw` / `iptables`）
- 路由器或数据中心的防火墙规则
- DNS 过滤

<a id="3-manually-install-expansions-works-even-if-the-ecloud-is-blocked"></a>
### 3) 手动安装占位符扩展（即使 eCloud 被阻止也适用）

如果无法解除连接限制，可以手动下载占位符扩展：

1. 访问 <https://ecloud.placeholderapi.com/>
2. 打开所需占位符扩展的页面。
3. 下载 `.jar` 文件。
4. 将其放入服务器的 `plugins/PlaceholderAPI/expansions/` 文件夹。
5. 执行 [`/papi reload`](users-commands.md#papi-reload)（或重启服务器）。

<a id="quick-connectivity-checks-optional"></a>
## 快速检查连通性（可选）

如果可以访问运行服务器的机器，可在终端或命令提示符中执行以下检查，帮助确认连接是否被阻止。

```
curl -I https://ecloud.placeholderapi.com/api/v3/
curl -I https://api.extendedclip.com/v2/
```

如果这些命令在服务器上执行失败，但在你自己的电脑或网络中可以正常执行，那么很可能是服务器托管商或数据中心网络阻止了出站连接。

<a id="still-stuck"></a>
## 问题仍未解决？

如需帮助，请加入 [Discord 服务器](https://discord.gg/helpchat)，并提供以下信息：

- 已尝试的处理方法
- 尝试下载时控制台输出的完整错误信息
- `/papi dump` 提供的链接
