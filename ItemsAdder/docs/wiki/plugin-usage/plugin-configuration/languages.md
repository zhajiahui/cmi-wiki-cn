---
title: "语言"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/languages"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 语言

### 当前可用语言

```
Messages GUIs: 
    Czech cz
    German de
    English en
    Spanish es
    French fr
    Italian it
    Japanese jp
    Korean ko
    Dutch nl
    Portuguese pt
    Polish pl
    Russian ru
    Turkish tr
    Thai th
    Chinese zh_cn
Dictionaries (items): 
    English en
    Spanish es
    French fr
    Hebrew he
    Italian it
    Portuguese pt
    Russian ru
    Thai th
    Turkish tr
    Chinese zh_cn
```

## 命令和消息

只需打开 `lang` 文件夹，复制一份 `en.yml`，然后翻译，并将 `config.yml` 中的 `lang` 设置改为你的文件名。

```yaml
config_files:
  lang: 'en'
  dictionaries-lang: 'en'
```

## 物品等内容

所有翻译均取决于客户端语言。

你可以方便地覆盖 Minecraft 的默认翻译文件。

支持以下内容：

* 物品名称
* 物品描述
* 实体名称
* 聊天消息

ItemsAdder 字典和 Minecraft 语言文件的主要区别，在于它们如何适应玩家设置。Minecraft 语言文件会根据每位玩家选择的语言动态调整。相比之下，ItemsAdder 字典是静态的，即所有玩家看到的文本语言都相同，由 `config.yml` 文件定义（例如 `en`）。

#### `languages`

languages 属性用于列出你想更改文本的所有语言。\
通常应只设置玩家群体使用的语言，不过我选择设为 ALL，这样无论玩家选择哪种客户端语言，都能看到自定义文本。

#### `entries`

这是翻译文本的列表。完整列表见[此处](https://github.com/InventivetalentDev/minecraft-assets/blob/1.21.4/assets/minecraft/lang/en_us.json)。

### 示例：自定义物品名称翻译

```yaml
info:
  namespace: ia_various_configs
minecraft_lang_overwrite:
  my_translations_all:
    entries:
      "my_custom_items.my_sword.name": "My Sword"
    languages:
      - ALL
  my_translations_french:
    entries:
      "my_custom_items.my_sword.name": "Mon épée"
    languages:
      - fr_fr
  my_translations_italian:
    entries:
      "my_custom_items.my_sword.name": "La Mia Spada"
    languages:
      - it_it
```

```yaml
info:
  namespace: special_items
items:
  my_sword:
    name: <lang:my_custom_items.my_sword.name>
    permission: my_sword
    resource:
      material: DIAMOND_SWORD
      generate: true
      textures:
      - item/my_sword.png
    durability:
      max_custom_durability: 1324
```

使用特殊属性 `<lang:NAME>` 指定翻译条目（使用 [Minimessage](../beginners/text-formatting.md)）。

### 示例：自定义 Esc 菜单的返回按钮文字

本例中，我会更改 ESC 菜单的 Return to game（回到游戏）文字。

```yaml
info:
  namespace: ia_various_configs
minecraft_lang_overwrite:
  esc_menu_texts:
    entries:
      "menu.returnToGame": "Return to &aSurvival &fGamemode"
    languages:
      - ALL
```

## ItemsAdder 字典

这是翻译物品的旧方法。所有翻译都不取决于客户端语言。

<details>

<summary>点击展开</summary>

支持以下内容：

* 物品名称
* 物品描述
* `/ia` 菜单类别名称

#### 为新物品创建自己的翻译

要为自己的物品创建翻译，只需在 `ItemsAdder/contents/` 内的新文件夹中创建文件（每种语言一个文件），例如 `ItemsAdder/contents/myitems/configs/dictionaries/`。

如下所示：

```yaml
info:
  namespace: special_items_lang
  dictionary-lang: "fr"
dictionary:
  display-name-my_sword: épée de saleté
  display-name-my_item: j'aime la baguette
```

这是我的物品文件的内容：

```yaml
info:
  namespace: special_items
items:
  my_sword:
    name: display-name-my_sword
    permission: my_sword
    resource:
      material: DIAMOND_SWORD
      generate: true
      textures:
      - item/my_sword.png
    durability:
      max_custom_durability: 1324
```

<div class="admonition info" markdown="1">
如你所见，我将 `name` 设为 `display-name-my_sword`，这会让 IA 用字典中的文本替换该文字，因此剑的名称将是 `épée de saleté`。
</div>

</details>

## 最后说明

你可以**跳过翻译**部分，直接这样设置，**但**这样在**将来**需要时就**不方便翻译**物品。

```yaml
info:
  namespace: special_items
items:
  my_sword:
    display_name: "épée de saleté"
    permission: my_sword
    resource:
      material: DIAMOND_SWORD
      generate: true
      textures:
      - item/my_sword.png
    durability:
      max_custom_durability: 1324
```
