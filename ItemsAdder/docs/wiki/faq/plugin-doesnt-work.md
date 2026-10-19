---
title: "插件不起作用"
source_url: "https://wiki.itemsadder.com/faq/plugin-doesnt-work"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 插件不起作用

**在寻求支持之前，请仔细阅读此页面。**

大多数情况下，通过阅读此页面可以轻松解决问题。

## 重新阅读安装教程

尝试在纯净服务器上重新按照安装教程操作。

[first-install.md](../plugin-usage/first-install.md)

## 移除最近安装的插件

尝试移除新插件、从服务器备份恢复，或将更新后的插件/服务器版本降级，再检查问题是否仍然存在。

## 更新所有依赖

更新所有依赖，过时的 JAR 有时会导致问题。

## 按照资源包排错教程检查

[identify-why-textures-are-not-shown.md](identify-why-textures-are-not-shown.md)

## 在 Discord 上询问

其他人可能也遇到了相同问题。也可以尝试使用搜索按钮。

## **如果仍有问题，请报告漏洞** <a href="#if-you-still-have-problems-please-read-this-and-then-contact-me" id="if-you-still-have-problems-please-read-this-and-then-contact-me"></a>

提交报告前先使用搜索按钮，其他人可能已经报告过此问题。

#### 无效的支持请求会被忽略

报告问题时，请务必：

* 按照教程完成每一个步骤，并确保阅读整个 Wiki。
* 在**纯净**服务器上测试插件（只安装 **ItemsAdder**），因为可能有其他插件造成干扰。
* 使用插件、依赖和服务器的最新版本。

如果问题仍然存在，且你认为这是漏洞，请在报告问题时向我提供以下信息：

* 你执行了哪些具体操作来触发此问题
* 服务器版本：使用 `/version` 命令，将显示的完整文本发给我（在控制台中执行以便复制粘贴）
* 插件版本
* 告诉我你是否编辑过 ItemsAdder 的 `.yml` 文件
* 告诉我你是否编辑过资源包
* 将 ItemsAdder 的 `.yml` 文件打包为 zip 发给我
* 说明插件是否在控制台或聊天中显示错误
* 完整的服务器日志（不要只截取你看到的 **ItemsAdder** 错误的一小部分，否则我无法判断问题）

