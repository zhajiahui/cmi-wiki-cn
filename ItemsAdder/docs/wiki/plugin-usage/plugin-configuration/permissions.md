---
title: "权限"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/permissions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 权限

## 权限

你**必须**使用支持 `.*` 权限写法的权限管理插件，例如 [LuckPerms](https://luckperms.net/download)。\
Bukkit 默认不支持这种符号！

| 功能                              | 权限                     |
| --- | --- |
| 允许使用配方，[更多信息](../../adding-content/items/item-properties/permission.md#recipes-permissions)。 | <p><code>ia.user.recipe.PERMISSION</code><br><br>（若要授予全部合成权限，只需使用 <code>ia.user.recipe.\*</code>）</p> |
| 在 `/ia` 界面中查看物品，[更多信息](../../adding-content/items/item-properties/permission.md)。 | <p><code>ia.user.ia.seeitem.PERMISSION</code><br><br>（若要授予全部 /ia 权限，只需使用 <code>ia.user.ia.seeitem.\*</code>）</p> |
| 在 `/ia` GUI 中搜索.   | `ia.user.ia.search`            |
| 在界面中查看类别。 | 使用类别权限，请查看 [/ia GUI](recipes-menu.md) 页面。 |
| 不带参数使用 `/e` 时显示 `/e` 书籍。 | `ia.user.image.gui` |
| 根据搜索词显示包含表情符号的 Tab 补全列表。 | `ia.user.image.hints` |
| 在**聊天**中使用**表情符号**.       | `ia.user.image.chat`           |
| 在**命令**中使用**表情符号**.   | `ia.user.image.command`        |
| 在**告示牌**中使用**表情符号**.      | `ia.user.image.sign`           |
| 在**书**中使用**表情符号**.      | `ia.user.image.book`           |
| 在**铁砧**重命名中使用**表情符号**.                                                                | `ia.user.image.anvil`          |
| 使用**表情**。 | <p><code>ia.user.image.use.\<permission\></code><br>示例： <code>ia.user.image.use.heart</code></p> |
| 在**聊天**中使用**文字效果**. | `ia.user.text_effect.chat`     |
| 在**告示牌**中使用**文字效果**.| `ia.user.text_effect.sign`     |
| 在**书**中使用**文字效果**.| `ia.user.text_effect.book`     |
| 在**铁砧**重命名中使用**文字效果**.                                                          | `ia.user.text_effect.anvil`    |
| 使用**文本效果**。 | <p><code>ia.user.text_effect.use.\<effect\>_</code></p><p>_示例（_<a href="../../adding-content/text-effects-1.17+.md">_完整列表见此_</a>_）：_</p><ul><li><code>_ia.user.text_effect.use.r</code></li><li><code>ia.user.text\_effect.use.rw</code></li></ul> |
| 使用表情动作命令（[玩家表情动作](../../adding-content/player-emotes.md)）。 | `ia.user.iaemote` |
| 使用某个表情动作（[玩家表情动作](../../adding-content/player-emotes.md)）。 | <p><code>ia.user.iaemote.use.\<emote\></code><br></p><p>示例：</p><ul><li><code>ia.user.iaemote.use.yes</code></li><li><code>ia.user.iaemote.use.\*</code></li></ul> |
| 查看 HUD         | `ia.user.hud.show.<name>`      |
| 查看所有 HUD       | `ia.user.hud.show.*`           |
| 阻止玩家的 HUD 值根据事件增加或减少.                                  | `ia.user.hud.bypass.triggers.*`|
| 阻止玩家的 HUD 值根据命令增加或减少.                             | `ia.user.hud.bypass.commands.*`|
| 阻止玩家的 HUD 值根据 API 增加或减少.                                  | `ia.user.hud.bypass.api.*`     |
| 绕过拒绝资源包时的踢出处理 | `ia.resourcepack.bypasskick` |
| 允许玩家放置的方块掉落战利品                                                              | `ia.admin.bypassblockplaceloot`|
| 破坏自定义方块 | <p><code>ia.user.block.break.\<suffix\></code></p><p><br>示例：</p><p><code>permission_suffix_</code>_ -\> _<code>_break_</code>_ : _<code>_iasurvival.ruby_block</code></p><p>权限：<code>ia.user.block.break.iasurvival.ruby_block_</code><br><br>_注意：需要在[方块属性](../../adding-content/blocks.md)中设置 _<code>_permissions_suffix</code>。</p> |
| 放置自定义方块 | <p><code>ia.user.block.place.\<suffix\></code></p><p><br>示例：</p><p><code>permission_suffix_</code>_ -\> _<code>_break_</code>_ : _<code>_iasurvival.ruby_block</code></p><p>权限：<code>ia.user.block.place.iasurvival.ruby_block_</code><br><br>_注意：需要在[方块属性](../../adding-content/blocks.md)中设置 _<code>_permissions_suffix</code>。</p> |
| 破坏家具 | <p><code>ia.user.furniture.break.\<suffix\></code></p><p><br>示例：</p><p><code>permission_suffix_</code>_ -\> _<code>_break_</code>_ : _<code>_example.red_chair</code></p><p>权限：<code>ia.user.furniture.break.example.red_chair_</code><br><br>_注意：需要在[家具属性](../../adding-content/furnitures.md)中设置 _<code>_permissions_suffix</code>。<br></p> |
| 放置家具 | <p><code>ia.user.furniture.place.\<suffix\></code></p><p><br>示例：</p><p><code>permission_suffix_</code>_ -\> _<code>_break_</code>_ : _<code>_example.red_chair</code></p><p>权限：<code>ia.user.furniture.place.example.red_chair_</code><br><br>_注意：需要在[家具属性](../../adding-content/furnitures.md)中设置 _<code>_permissions_suffix</code>。</p> |

## WorldGuard 标志

[worldguard-flags.md](../../compatibility-with-other-plugins/compatible/worldguard-flags.md)

## 权限设置示例

| 权限                    | 操作                                                             |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ia.user.ia`            | 打开 `/ia` 菜单|
| `ia.user.ia.seeitem.*`  | 查看 `/ia` 菜单中的所有物品|
| `ia.user.iarecipe`      | 使用 `/iarecipe` 命令|
| `ia.user.recipe.*`      | 使用所有配方|
| `ia.menu.seecategory.*` | <p>查看 <code>/ia</code> 菜单中的所有类别.<br><mark style="color:red;">注意:</mark> <br><mark style="background-color:red;">这可能会根据你下载的物品包而改变. 类别权限通常以</mark> <code>ia.menu.seecategory.</code> <mark style="background-color:red;">开头，但有些开发者可能会更改它.</mark></p> |
| `ia.user.image.gui`     | 使用 `/e` 命令查看表情符号书|
| `ia.user.image.hints`   | 使用 `/e` 和 TAB 完成时建议表情符号|
| `ia.user.image.chat`    | 在聊天中替换表情符号文本 `:smile:` 等|
| `ia.user.image.command` | 在命令中替换表情符号文本 `:smile:` 等|
| `ia.user.image.sign`    | 在标牌中替换表情符号文本 `:smile:` 等|
| `ia.user.image.book`    | 在书籍中替换表情符号文本 `:smile:` 等|
| `ia.user.image.use.*`   | 访问所有表情符号|

## 我在哪里可以获得类别权限？

**ItemsAdder 默认类别**

打开 `categories.yml` 文件以读取查看类别的所有权限.\
默认的 ItemsAdder 包类别文件位于每个 `namespace` 文件夹内.\
例如: `contents/iasurvival/configs/categories.yml`

例如，如果你想让玩家查看默认 ItemsAdder 的所有类别，你只需授予 `ia.menu.*` 权限.

**附加包类别**

如果正在安装[附加包](https://addons.plugin.ga/itemsadder/)，可以在 `contents/<ADDON NAME>/configs` 中查找 `categories.yml` 文件。作者通常将类别放在其中，因此也能找到对应的**权限**。

### **创建我的类别**

要创建你的类别，请阅读教程

[ia.md](recipes-menu.md)
