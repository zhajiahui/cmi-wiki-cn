---
title: 排错
source_url: https://wiki.mythiccraft.io/mythicmobs/Troubleshooting/Troubleshooting
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 排错 {#troubleshooting}

如果某项功能遇到问题，可以在下方查找。点击相应链接，即可查看逐步排查问题的指南。如果仍未解决，可前往我们的 [Discord](https://www.mythiccraft.io/discord) 寻求帮助

## 常规指南 {#general-guidelines}

#### 创造模式 {#creative-mode}

不要在创造模式下测试，无论出于什么原因。这样会使大多数功能出现问题。请改用生存模式测试。

#### 最大生命值 {#max-health}

默认情况下，Spigot 将生物的最大生命值限制为2048。你可以通过将 `maxHealth` 更改为更高的数字，在 `spigot.yml` 文件中更改此限制。

#### 控制台记录死亡信息 {#console-logs-deaths}

如果控制台出现 "Skeletal Knight was slain by PlayerName" 之类的消息，而你不想显示这些消息，可打开 `/spigot.yml`，将 `log-named-deaths` 设为   false  ，然后重启服务器。

## 特定功能 {#specific-features}

### MythicMobs {#mythicmobs}

- [随机生成](randomspawns.md)

### ModelEngine {#modelengine}

- [ModelEngine 模型消失](modelengine-model-vanishes.md)
