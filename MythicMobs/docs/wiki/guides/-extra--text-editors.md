---
title: （补充）文本编辑器
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/%28Extra%29-Text-Editors
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# （补充）文本编辑器 {#extra-text-editors}

使用 MythicMobs 时，了解各项功能的工作方式只是其中一半，另一半是将它们写成配置。如果没有合适的文本编辑器，管理所需的各种文件和配置可能会很困难。好在有很多不错的选择！本指南只介绍 [Visual Studio Code](https://code.visualstudio.com/Download)，因为它支持 [MythicScribe 扩展](https://marketplace.visualstudio.com/items?itemName=Lxlp.mythicscribe)，但任何文本编辑器都可以使用！

## [VSCode 扩展](https://marketplace.visualstudio.com/items?itemName=Lxlp.mythicscribe) {#vscode-extension}

## 创建工作区 {#creating-a-workspace}

VSCode 最实用的功能之一是创建“工作区”，它可以持续保留打开的所有文件，并为项目使用自定义设置。创建工作区时，可以先右键点击要使用的文件夹。对于 Mythicmobs，根据你的使用方式和目的，可以选择根文件夹或某个[包](../packs.md)的文件夹。

- 右键点击文件夹并选择 "Open with Code"，即可选中该文件夹。  
![选择文件夹](https://i.imgur.com/pOPO9cI.png)
- 打开后，前往 `File > Save Workspace As...`，选择有效路径，用于创建新的工作区文件。  
![创建工作区](https://imgur.com/2CWpJnK.png)
- 之后双击生成的工作区文件，即可再次打开该工作区。  
![工作区文件](https://imgur.com/Ja7mZcg.png)

这样就完成了！你已经创建了一个工作区，可以更方便地跟踪更改和编辑内容！

## 自定义工作区 {#customizing-the-workspace}

创建工作区后，可以设置仅适用于该工作区的选项，避免影响其他工作区。打开工作区后，前往 `File > Preferences > Settings > Workspace` 即可进行设置！
![工作区设置](https://imgur.com/OpWkcEG.png)

## 工作区工具 {#workspace-utilities}

##### 编辑文件 {#editing-files}

- 你可以直接在 VSCode 的资源管理器中创建、编辑和重命名文件或文件夹：右键点击相应文件夹或文件，选择所需操作即可。

##### 固定标签页 {#pinning-tabs}

- 右键点击重要的标签页并选择 `Pin`，可以将其固定。固定后的标签页会保持打开；使用任何“全部关闭”选项也不会关闭它们，而且它们会固定在标签页列表的开头。

##### 拆分视图 {#split-view}

- 如果需要同时编辑技能文件和生物文件，可以将其中一个拆分显示，以便同时查看。点击相应的已打开标签页，选择 "Split X"，其中 X 是所需的方向（上、下、左、右）。

##### 批量修改 {#bulk-changes}

- 如果想重命名元技能或生物，可以：
  - 使用右侧的搜索和替换功能（放大镜图标），在整个工作区的所有文件中进行修改。
  - 使用 `Change All Occurrences` 按钮（选中要修改的词后右键点击），修改当前文件中该词的所有出现位置。
- 如果需要同时编辑多行，可以按住鼠标中键并拖过相应行，为每行创建一个光标，然后同时编辑这些行。
