---
title: 安装指南
source: https://docs.phoenixdevt.fr/mmoprofiles/install
source_snapshot: '2026-10-19'
---

# 安装指南 {#🔌-installation-guide}

## 安装 {#installation}

安装后即可使用默认配置。已有玩家首次在安装插件后登录时，会看到一份保留其原有数据的档案。此功能可在插件主配置文件中关闭。

## 禁用Spigot玩家数据保存 {#disable-spigot-player-data-saving}

在 `spigot.yml` 中启用此项，可以减少 MMOProfiles 使用时的重复数据。它会让 Spigot **停止向世界数据文件夹保存玩家数据**，因为 MMOProfiles 已负责保存这些数据。此选项仍有风险，修改时需要留意！

```yml
players:
  disable-saving: true
```

如果接受丢弃原有玩家数据，可以在启用此项后直接清空 `/world/playerdata`。如果保留 `playerdata` 文件夹，MMOProfiles 会在玩家首次加入时将这些数据迁入新档案。

## Multiverse-Core用户注意事项 {#note-for-multiverse-core-users}

使用 Multiverse-Core 时，还需要关闭 `Multiverse/config.yml` 中的此项。该选项会在玩家首次加入时执行传送，覆盖 MMOProfiles 的传送，干扰档案选择。

```yml
firstspawnoverride: 'false'
```

---

原文：[🔌 Installation Guide](https://docs.phoenixdevt.fr/mmoprofiles/install) · 原文归档：2026-10-19
