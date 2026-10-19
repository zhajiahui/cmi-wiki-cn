---
title: "Google Drive"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/resourcepack-hosting/google-drive"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# Google Drive

**不推荐。**

由于 Minecraft 的漏洞，此方法在某些电脑上的 1.17 之前版本中存在问题。更多信息见：[https://bugs.mojang.com/browse/MC-143768](https://bugs.mojang.com/browse/MC-143768)

Mojang 已修复此问题，因此此方法在 Minecraft 1.17.1 及较新的版本中应该可以正常使用。

### 步骤 1

右键点击资源包 zip 文件，选择“Get link”（获取链接）。

![](../../../assets/5838cbb8c7382f85ecb9.png)

### 步骤 2

重要：将权限设为“Anyone with the link”（知道链接的任何人）。

![](../../../assets/62d08118d5dea9101431.png)

点击“复制链接”

![](../../../assets/cd8fa229b0c5966e656c.png)

### 步骤 3

访问这个网站：[http://a.devs.beer/gdrive-direct](http://a.devs.beer/gdrive-direct)

粘贴链接并点击“获取直接链接”

<img src="../../../assets/eff4cc9224ab19996325.png" alt="" data-size="original">

### 步骤 4

网站会自动将生成的链接添加到你的剪贴板中。

![](../../../assets/c7e6522ef2a6b46fe845.png)

你现在可以将链接粘贴到 **ItemsAdder** 配置文件 `config.yml` 中，然后使用 `/iareload` 命令。

```yaml
external-host:
  enabled: true
  url: 'http://drive.google.com/uc?export=view&id=10g3whim95Hab40KZNjUkwY9FUuqKMGh5'
```

### 完成！

你现在可以看到资源包已被游戏正确加载。

## 常见问题

### 长时间停留在“正在请求... 100%”

### ![](../../../assets/8fade41c8fca2512f272.png)

这是正常现象。因为 Google Drive 在授权下载资源包之前会进行一些操作。

这种情况只会在玩家第一次下载资源包时发生，通常需要 5 到 10 秒。

### 资源包完全无法加载

由于 Minecraft 的漏洞，此方法在某些电脑上的 1.17 之前版本中存在问题。更多信息见：[https://bugs.mojang.com/browse/MC-143768](https://bugs.mojang.com/browse/MC-143768)

此方法在 Minecraft 1.17.1+ 上 100% 可用。

## 如有需要，继续安装

[first-install.md](../../first-install.md)
