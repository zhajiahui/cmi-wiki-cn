---
title: "自动补全"
source_url: "https://wiki.itemsadder.com/adding-content/scripting/java/autocompletion"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 自动补全

需要 ItemsAdder 4.0.13 或更高版本。

仅兼容 `.java` 脚本类型。

#### 步骤 1

在命名空间文件夹中新建名为 `build.gradle.kts` 的文件。\
例如 `ItemsAdder/contents/test/build.gradle.kts`。

可以添加仓库和依赖，但如果脚本在运行时使用这些依赖，服务器中也必须具备它们。

此处添加 Paper 和 ItemsAdder API，是为了让 Java 自动补全正常工作。

```gradle
plugins {
    java
}

sourceSets {
    main {
        java {
            setSrcDirs(listOf("."))
        }
    }
}

repositories {
    mavenCentral()
    maven("https://repo.papermc.io/repository/maven-public/")
}

dependencies {
    compileOnly("io.papermc.paper:paper-api:1.21.4-R0.1-SNAPSHOT")
    compileOnly("beer.devs:itemsadder-api:4.0.17")
}
```

将 Paper 版本替换为与服务器匹配的版本。

#### 步骤 2

安装 [VSCode](https://code.visualstudio.com/)。

安装以下扩展：

* [Extension Pack for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)
* [Gradle for Java](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-gradle)

#### 步骤 3

新建文件 `.vscode/settings.json`（不要遗漏开头的点！）。

```json
{
  "java.autobuild.enabled": false
}
```

#### 步骤 4

在 VSCode 中打开命名空间文件夹，例如：

`ItemsAdder/contents/test`

VSCode 应当检测到 `build.gradle.kts`，并启用 Java 自动补全。
