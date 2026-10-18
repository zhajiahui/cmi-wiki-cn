---
title: 自定义方块
source: https://docs.phoenixdevt.fr/mmoitems/features/custom-blocks
source_snapshot: '2026-10-19'
---

# 自定义方块 {#📦-custom-blocks}

使用MMOItems5+ 你可以实现具有自定义纹理的块。你甚至可以让它们生成并使用[世界生成模板](world-gen-templates.md)] 定义它们的稀有程度，使用玩家破坏它的工具进行配置，使用MMOItems掉落表决定它会掠夺什么，并将随机数量的 exp 绑定到它。

**[在此下载所需的资源包](https://www.dropbox.com/s/90w9pvdbfeyxu94/MICustomBlockPack.zip?dl=1)**

## 创建和编辑自定义块 {#creating-and-editing-a-custom-block}

你可以使用`/mi browse blocks`浏览当前的自定义块。当使用物品浏览器时，你可以使用GUI右下角的小物品指示器切换到块浏览器。就像使用物品浏览器一样，你可以右键单击自定义块来编辑它们。

这是来自`blocks.yml`的配置模板

```yml
'1':
  base:
    name: '&aMy First Custom Block'
    lore:
    - '&7Wow... It''s possible!'
    - '&7That''s awesome!'
    required-power: 2
    min-xp: 10
    max-xp: 20
    gen-template: basic-template
    material: STONE
    block-id: 1.0
```

`required-power`定义了工具必须具有的镐功率才能打破该块。如果设置为3，则玩家必须使用`Pickaxe Power`高于3的工具。当破坏自定义块时，MMOItems会滚动在`min-xp`和`max-xp`之间选择的随机数量的 exp，并像普通矿石一样在块上生成一个 exp 球。

`gen-template`是自定义块[生成模板](world-gen-templates.md)。它定义了该块可能产生的位置以及它的稀有程度。

## 如何升级到MMOItems5.5.5自定义块 {#how-to-upgrade-to-mmoitems-5-5-5-custom-blocks}

本节将介绍如何正确将自定义模块升级到MMOItems5.5.5。

**[在此下载新资源包](https://drive.google.com/uc?id=1FjV7y-2cn8qzSiktZ2CUXmkdjepXdj5N)**

### 物品型附加 {#item-type-addition}

你首先必须将新类型添加到item-types.yml。你可以将其粘贴到文件中的任何位置，也可以重新生成它。 **如果你不这样做，插件将不会启用并抛出 NullPointerException。**

```yml
BLOCK:
  display: STONE:0
  name: 'Block'
  unident-item:
    name: '&f#prefix#Unidentified Block'
    lore:
      - '&7This item is unidentified. I must'
      - '&7find a way to identify it!'
      - '{tier}'
      - '{tier}&8Item Info:'
      - '{range}&8- &7Lvl Range: &e#range#'
      - '{tier}&8- &7Item Tier: #prefix##tier#'
```

### 自定义块转换 {#custom-block-conversion}

*如果你当前正在使用自定义块，则以下注释适用，如果没有，你可以删除custom-blocks.yml。*

你的custom-blocks.yml文件应自动生成为物品/block.yml。一旦完成，就可以安全删除。

### 安装后注意事项 {#post-install-notes}

**自定义方块现在与普通 MMOItems 物品的行为相同。**可以通过 /mi browse 编辑，也可以交给玩家正常使用，因为它们现在按普通方块的方式放置。如果允许玩家使用自定义方块，务必在 config.yml 中将 `replace-mushroom-drops` 设为 true，否则可能被利用。

每次通过界面修改方块后，都必须重载插件：重启服务器或执行 /mi reload。

如果你对新更新有任何问题，请务必在 mmo 频道中的MythicMobsDiscord上询问。

---

原文：[📦 Custom Blocks](https://docs.phoenixdevt.fr/mmoitems/features/custom-blocks) · 原文归档：2026-10-19
