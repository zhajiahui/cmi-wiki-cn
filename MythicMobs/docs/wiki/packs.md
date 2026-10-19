---
title: 内容包
source_url: https://wiki.mythiccraft.io/mythicmobs/Packs
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 内容包

MythicMobs 的内容包系统便于整理全部文件，也便于安装从 MCModels 等平台获取的内容包。

在 MythicMobs/Packs 下创建文件夹，命名为内容包名称。再像 MythicMobs 基础目录一样，在其中创建 Items、Mobs、Skills、RandomSpawns 等文件夹，放入任意数量的对应类型文件。之后即可将整个文件夹压缩为 ZIP 分发。

# 文件夹和文件 {#folders-and-files}

一个包可以包含许多文件夹和文件。以下是你可能使用的内容的列表（目前还不全面）

## 内容包信息 {#pack-info}

在制作包时，你可能希望在其中嵌入更多信息，例如作者是谁、包名称等。这可以通过在包的主目录中创建 `packinfo.yml` 文件来实现。

```yaml
Name: The name of the pack
Version: 0.1.0
Author: The name of the author
Icon:
  Material: The bukkit name of the item you want to use
  Model: The CustomModelData of the material
URL: The link to your site, if any
Description:
- This is a list
- of things that will appear
- as the pack's description
- &aYou can also use color codes!&r
```

玩家执行 `/mm menu` 打开 MythicMobs 菜单，进入任一分类后，将鼠标悬停在内容包图标上即可查看。如果内容包包含当前分类的内容，就会显示该图标。

## 依赖与覆盖 {#dependencies-and-overrides}

`packinfo.yml` 也可以根据其他已安装内容，禁止加载整个内容包或其中部分文件：

```yaml
PackDependencies:
- MythicCrucible
PackOverrides:
- TheRealPack
FileDependencies:
- enchantments/* MythicEnchants
- cosmetics/chat.yml MythicCosmetics
FileOverrides:
- items/armors_vanilla.yml MythicArmors
```

| 配置键 | 效果 |
| --- | --- |
| `PackDependencies` | 除非列出的每个条件都为 true，否则跳过此包。 |
| `PackOverrides` | 列出的任意条件为 true 时，跳过此包。 |
| `FileDependencies` | `<glob> <condition>`：除非条件为 true，否则跳过匹配的文件。 |
| `FileOverrides` | `<glob> <condition>`：条件为 true 时，跳过匹配的文件。 |

条件是插件的名称、另一个包的文件夹名称或`MythicMobsPremium`。条件可以与 `&&`、`||`、`!` 和括号组合：

```yaml
PackDependencies:
- ((MythicCrucible && MythicMobsPremium) || Nexo)
FileOverrides:
- armors/** (MythicArmors || TheRealArmors)
```

Glob 路径相对于内容包目录。`*` 只匹配单层目录，`**` 匹配任意深度，包含空格的路径必须加引号。无效条件会记录警告并被忽略。被跳过的内容包不会被 `mythicpack` 条件识别。

将其用于在安装完整包时应自行关闭的精简包，或者用于在存在时应使用MythicArmors和在不存在时应使用普通装甲的物品。

## Files 文件夹 {#files-folder}

此文件夹中的配置会**根据文件名解析**，与文件的*位置*无关。文件名应采用以下结构：

```yaml
filename.identifier.yml
```

并且，根据它们的标识符，它们将被解析为不同的文件类型

| 标识符 | 别名 | 文件解析类型 |
| --- | --- | --- |
| `mob` |  | 生物文件 |
| `skill` |  | 技能文件 |
| `item` |  | 物品文件 |
| `droptable` | `drop` | 掉落表文件 |
| `randomspawn` | `rspawn`, `spawn` | 随机生成文件 |
| `spawner` |  | 刷怪器文件 |
| `menu` |  | 自定义菜单文件 |
| `placeholder` |  | 自定义占位符文件 |
| `stat` |  | 属性文件 |
| `loretemplate` | `lore-template` | 物品描述模板文件 |
| `font` |  | 字体文件 |
| `worldgen` |  | 世界生成文件 |
| `equipmentset` | `equipment-set` | 装备套装文件 |
| `tooltip` |  | 提示框文件 |
| `augment` |  | Augment 文件 |

有些文件也只能通过其扩展名来识别

```yaml
filename.extension
```

| 扩展名 | 文件解析类型 |
| --- | --- |
| `schem` | 结构模板文件 |

```
📦ExamplePack
 ┣ 📂files
 ┃ ┣ 📂aRandomFolder
 ┃ ┃ ┣ 📂aNestedFolder
 ┃ ┃ ┃ ┗ 📜ThisIsADroptableFile.droptable.yml
 ┃ ┃ ┣ 📜ThisIsAMobFile.mob.yml
 ┃ ┃ ┗ 📜ThisIsAPlaceholderFile.placeholder.yml
 ┃ ┣ 📂anotherRandomFolder
 ┃ ┃ ┣ 📜ThisIsAMobFile.mob.yml
 ┃ ┃ ┣ 📜ThisIsASchematic.schem
 ┃ ┃ ┗ 📜ThisIsASkillFile.skill.yml
 ┃ ┗ 📜ThisIsAStatFile.stat.yml
 ┗ 📜packinfo.yml
```
