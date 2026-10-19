---
title: 主机密钥
source_url: https://worldguard.enginehub.org/en/latest/host-keys/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 主机密钥 { #host-keys }

过去，Minecraft 的登录代码曾多次出现问题，使玩家可以冒用任意玩家身份登录服务器，包括管理员和管理人员。2010 年至 2013 年间，这类漏洞公开过五次，经常导致数以千计的服务器遭到入侵。

WorldGuard 加入主机密钥功能，是为了在防止身份冒用方面多设一道屏障。客户端登录服务器时必须发送一项 Mojang 不掌握的额外信息。即使攻击者突破 Minecraft 的登录系统，冒充管理人员加入，因为其客户端缺少这项信息，服务器仍能识别出冒用行为。

!!! note "注意"

    如今，这类安全漏洞已经较少出现。

## 工作原理 { #how-it-works }

玩家使用某个地址（如 `play.example.com`）连接服务器时，Minecraft 会告知服务器所用地址。管理人员可以通过一个特殊的秘密地址 `secretmod.play.example.com` 连接，服务器便能检查该地址是否以 `secretmod` 开头。

主机密钥功能允许你为特定玩家配置被接受的连接地址。名单中的玩家使用错误地址连接时，会立即被踢出。

## 配置 { #configuration }

在[配置](config.md)中设置：

```text
host-keys:
    your_username: bagels.play.example.com
    moderator1_name: manoverboard.play.example.com
```

!!! tip "提示"

    主机密钥支持 UUID。建议使用玩家的 UUID，而非用户名进行关联，以免玩家改名后受影响。

### DNS 配置 { #dns-configuration }

要使其生效，必须让 `bagels.play.example.com` 和 `manoverboard.play.example.com` 指向服务器。但**不要**为实际使用的这些域名单独添加具体记录，否则攻击者很容易发现秘密域名。

推荐配置“泛域名”。例如 `*.play.example.com` 表示*任意*前缀都可以使用，如 `aa.play.example.com`、`ab.play.example.com`、`ac.play.example.com` 等。

!!! tip "提示"

    如果没有域名，或无法设置泛域名，可以使用 [sslip.io](https://sslip.io/)。

## 其他方式 { #alternatives }

除了主机密钥，也可以使用需要输入密码的某种登录命令，不过 WorldGuard 本身不提供此功能。
