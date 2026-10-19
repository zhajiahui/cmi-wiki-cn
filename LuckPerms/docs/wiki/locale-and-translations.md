---
title: "语言与翻译"
source_url: https://luckperms.net/wiki/Locale-and-Translations
source_kind: official-wiki
translation_review: reviewed
source_version: "fc2919c3d5e6bfba82af31f9930273b00f08ddbf"
---

<a id="overview"></a>
### 概述

LuckPerms 的所有游戏内消息都可以通过翻译系统自定义和翻译。

*英语*的基础翻译文件见：[`luckperms_en.properties`](https://github.com/LuckPerms/LuckPerms/blob/master/common/src/main/resources/luckperms_en.properties)

<a id="contributing"></a>
## 参与翻译

其他语言的翻译工作在我们的 [Crowdin 项目](https://crowdin.com/project/luckperms)上进行。

衷心感谢大家的帮助！:heart:

<a id="using-official-community-provided-translations"></a>
## 使用社区提供的“官方”翻译

要查看已安装或可用的翻译列表，执行 `/lp translations`。

要安装社区提供的最新翻译，执行 **`/lp translations install`**。（可以反复执行此命令，以重新安装并获取更新）

如果有相应翻译，玩家收到的消息会使用其 Minecraft 客户端设置中选择的语言。如果没有该语言的翻译，则使用内置的英语消息。

<a id="using-custom-translations"></a>
## 使用自定义翻译

可以按以下步骤将翻译加载到插件中：

* 创建 `/plugins/LuckPerms/translations/` 文件夹
* 导出修改后的 `.properties` 文件，并将其重命名为 `<locale id>.properties`。
  * 支持的语言区域 ID 列表见[此处](https://www.localeplanet.com/java/)
  * 例如，要加载*西班牙语*翻译，使用 `es.properties`；要加载*葡萄牙语（巴西）* 翻译，使用 `pt_BR.properties`
* 重启服务器
