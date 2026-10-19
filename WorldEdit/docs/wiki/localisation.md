---
title: 本地化
source_url: https://worldedit.enginehub.org/en/latest/localisation/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 本地化 { #localisation }

WorldEdit 内置本地化支持，翻译由社区通过 Crowdin 提供，并随 WorldEdit 发布版一并打包，因此安装后即可使用所有语言。它会根据每名玩家 Minecraft 客户端所设语言显示文本，让玩家看到自己选择的语言。

因此，多语言服务器中的每名玩家都可使用偏好的语言，而非被迫使用服务器统一指定的语言。

## 参与翻译 { #how-to-contribute }

如果 WorldEdit 的部分内容尚未翻译为你的语言，通常是因为还没有人提交相应译文。

我们使用 Crowdin 接收翻译，项目页面[在这里](https://crowdin.com/project/worldedit-core)。每次发布新版 WorldEdit 时，都会从网站导入新翻译。

欢迎为 Crowdin 项目贡献译文，更完整的翻译能使所有人受益。

!!! note "注意"

    撰写本文时，由于命令库的限制，部分命令说明文本尚无法翻译。限制解决后，我们会将这些文本加入翻译系统。

## 自定义翻译 { #custom-translations }

WorldEdit 支持从其目录下的 `lang` 文件夹加载用户提供的翻译。

语言加载采用按字符串生效的优先级系统，尽量利用所有可用的本地化信息。因此，一部分译文可来自 WorldEdit 目录，另一部分来自 JAR。即使用户只提供了一个字符串的译文，其余缺失条目仍会从内置翻译补齐。本地副本只需包含明确要覆盖的字符串，无需随每次 WorldEdit 更新维护整个翻译文件。

字符串按以下顺序查找：

1. 游戏目录中 WorldEdit 文件夹内的 `lang/[language-code]/strings.json`。

2. 游戏目录中 WorldEdit 文件夹内 `lang/i18n.zip` 中的 `[language-code]/strings.json`。

3. WorldEdit JAR 内 `lang/i18n.zip` 中的 `[language-code]/strings.json`。

4. WorldEdit JAR 内的 `lang/strings.json`，仅用于默认语言。

如果因任何原因找不到当前语言的某个字符串，会改用更宽泛的语言重复查找，例如用 `fr` 代替 `fr-CA`，最后回退到默认语言 `en`。

根据这一优先级机制，建议用户目录中*只*放入确实要修改的字符串，以便后续更新 WorldEdit 时自动获得其他翻译改进。

!!! note "注意"

    此系统主要用于补齐服务器常用语言的缺失译文，而不是完整自定义消息。虽然可以借此修改消息，但仍有部分限制，例如不能改变颜色。

文件结构可参考 WorldEdit JAR 内的 `lang/i18n.zip`。自定义翻译无论放在 ZIP 内还是 `lang` 文件夹中，都遵循同一结构。

### ZIP 方式 { #zip-method }

在游戏目录中放置 `WorldEdit/lang/i18n.zip` 后，WorldEdit 会从中加载翻译，优先级高于 JAR 内的译文。

### 独立文件方式 { #file-method }

也可不用 ZIP，直接将语言文件存入文件夹。例如澳大利亚英语放在 `lang/en-AU`，希腊语放在 `lang/el`。基础译文 `en` 不使用独立目录，而是放在 `lang/strings.json`；因为它不来自 Crowdin，而是由我们在编写插件时直接编写。
