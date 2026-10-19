---
title: Disguise Modify
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/DisguiseModify
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Disguise Modify {#disguise-modify}

## 说明 {#description}

修改目标实体*已经*应用的伪装。   与[伪装](disguise.md)机制一样，必须安装[LibsDisguises](https://www.spigotmc.org/resources/libs-disguises-free.81/)。 [在这里](../../mobs/disguises.md)你可以找到我们关于此事的文档。该机制中的伪装语法与`/modifydisguise`命令中使用的语法完全等同。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| disguise | d, type | 要修改的伪装选项。 | player Ashijin |

## 示例 {#examples}

将伪装主手显示的物品设为 air。

```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand air"} @self 
```

##  {#section}

这会将伪装主手上显示的物品设置为真实物品

```yaml
  Skills:
  - disguisemodify{d="setItemInMainHand %held-item%"} @self
```

## 别名 {#aliases}

- modifydisguise
