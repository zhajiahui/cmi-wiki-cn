---
title: Phoenix 文档维护说明
source: https://docs.phoenixdevt.fr/README
source_snapshot: '2026-10-19'
---

# Phoenix 文档维护说明 {#phoenix-plugin-documentation}

插件文档是使用 [VitePress](https://vitepress.dev)实现的。这个基于Vue的精彩框架允许从 Markdown 文件生成静态网站。

该网站托管在 [PhoenixDevt 网站](index.md)上，并且每当更改推送到`main`分支时，都会使用 [TeamCity](https://teamcity.phoenixdevt.fr)持续部署。

## 发展 {#development}

安装依赖项

```sh
npm install
```

运行开发服务器

```sh
npm run docs:dev
```

## 建立网站 {#build-website}

静态站点将构建在`.vitepress/dist`文件夹中。可以使用以下命令构建它

```sh
npm run docs:build
```

构建网站将显示死链接和对non-existing图像的引用。这对于在将更改推送到`main`分支之前检查文档的有效性非常有用。  如果检测到此类错误，TeamCity将使构建失败。

## 文件系统和外壳 {#file-systems-casing}

在 Windows 计算机上工作时，请记住 Windows 文件系统不区分大小写，而大多数部署目标（基于 Linux）则区分大小写。构建网站的TeamCity代理在基于 Linux 的系统上运行，因此即使服务器在 Windows 上本地构建，也可能会出现文件名大小写问题。

对于文件名，请遵循`lowercase-kebab-case`约定，以避免文件名大小写问题。你可以使用 Python 脚本`scripts/check_file_casing.py`检查文件名中包含大写字符的文件。

---

原文：[Phoenix Plugin Documentation](https://docs.phoenixdevt.fr/README) · 原文归档：2026-10-19
