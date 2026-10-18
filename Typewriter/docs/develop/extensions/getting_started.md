---
title: 创建扩展（Creating an Extension）
source: https://docs.typewritermc.com/develop/extensions/getting_started
source_version: 0.8.0
---

# 创建扩展（Creating an Extension）

## 介绍 {#introduction}

Typewriter是一个支持扩展开发的动态平台，扩展是增强整体功能的模块化组件。
扩展是独立的，易于共享，并顺利集成到Typewriter系统中。
它们允许你创建自定义条目并将其显示在网页面板中。
本指南旨在指导你完成创建扩展的过程。

## 前置条件 {#prerequisites}

- Java 开发工具包 (JDK) 21 或更高版本。
- 集成开发环境 (IDE)，例如 IntelliJ IDEA 或 Eclipse。
- 对Gradle和SpigotAPI 的基本了解。

## 创建 Gradle 项目 {#setting-up-a-gradle-project}

首先为你的Typewriter扩展建立一个Gradle项目。以下是Gradle项目的全面设置：

**正式版**

将以下内容添加到你的`settings.gradle.kts`文件中：

settings.gradle.kts

```kotlin
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
        maven("https://maven.typewritermc.com/releases")
    }
}
```

将以下内容添加到你的`build.gradle.kts`文件中：

build.gradle.kts

```kotlin
plugins {
    kotlin("jvm") version "2.0.21"
    id("com.typewritermc.module-plugin") version "<module plugin version>"
}

// Replace with your own information
group = "me.yourusername"
version = "0.0.1"

typewriter {
    namespace = "<a name for the company which all your extensions are published under>"

    extension {
        name = "<Name of the extension>"
        shortDescription = "<Short description of the extension>"
        description = "<Long description of the extension>"
        engineVersion = "<latest typewriter version>"

        paper {
            // Optional - If you want to make sure a plugin is required to be installed to use this extension
            dependency("<plugin name>")
        }
    }
}

kotlin {
    jvmToolchain(21)
}
```

**测试版**

将以下内容添加到你的`settings.gradle.kts`文件中：

settings.gradle.kts

```kotlin
pluginManagement {
    repositories {
        mavenCentral()
        gradlePluginPortal()
        maven("https://maven.typewritermc.com/beta")
    }
}
```

将以下内容添加到你的`build.gradle.kts`文件中：

build.gradle.kts

```kotlin
plugins {
    kotlin("jvm") version "2.0.21"
    id("com.typewritermc.module-plugin") version "<module plugin version>"
}

typewriter {
    namespace = "<a name for the company which all your extensions are published under>"

    extension {
        name = "<Name of the extension>"
        shortDescription = "<Short description of the extension>"
        description = "<Long description of the extension>"
        engineVersion = "<latest typewriter version>"
        channel = com.typewritermc.moduleplugin.ReleaseChannel.BETA

        paper {
            // Optional - If you want to make sure a plugin is required to be installed to use this extension
            dependency("<plugin name>")
        }
    }
}

kotlin {
    jvmToolchain(21)
}
```

**替换你的信息**

确保将`me.yourusername`等占位符替换为你的项目详细信息。

## 构建扩展 {#building-the-extension}

创建扩展类后，构建扩展。这可以通过运行`build`Gradle任务来完成。
这将在`build/libs`目录中生成一个 JAR 文件。
该 JAR 文件可以用作Typewriter中的扩展。
将 JAR 文件放置在`plugins/Typewriter/extensions`目录中。
Typewriter将自动加载扩展并运行它。

**重载扩展**

你可以重新启动Minecraft服务器或使用`/typewriter reload`重新加载Typewriter来重新加载扩展。

如果出现任何问题，请检查控制台是否有错误并确保扩展配置正确。
如果你需要帮助，请加入[Discord 服务器](https://discord.gg/HtbKyuDDBw)并寻求帮助。

## 下一步 {#whats-next}

创建扩展后，你可以开始向其添加功能。
查看[创建条目](entries.md)指南，了解如何向扩展添加条目。

---

原文：[Creating an Extension](https://docs.typewritermc.com/develop/extensions/getting_started) · 文档版本：0.8.0
