---
title: general.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: general.yml
source_version: 0.98.13-x6
---

# general.yml

文件：`general.yml`。版本：`0.98.13-x6`。

随包配置。

## `Language` { #language }

```yaml title="general.yml · Language"
# 完整的配置说明见《CrackShot 完全指南》（英文）：
# https://github.com/Shampaggon/CrackShot/wiki/The-Complete-Guide-to-CrackShot

# 提示和命令帮助使用的语言：zh_CN（简体中文）或 en_US（英文）。
Language: zh_CN
```

## `Disabled_Worlds` { #disabled_worlds }

```yaml title="general.yml · Disabled_Worlds"
# 在这些世界里完全停用 CrackShot。写法示例：
#
# Disabled_Worlds:
#     - world_nether
#     - world_the_end
#     - 世界文件夹的名字
#
# "Disabled_Worlds: []" 表示列表为空。要填世界时，先把它改成 "Disabled_Worlds:" 再逐行列出。
# 不要用 Tab 缩进，空格的数量也要对齐。
Disabled_Worlds: []
```

## `Inventory_Control` { #inventory_control }

```yaml title="general.yml · Inventory_Control"
# 限制玩家快捷栏里能同时带几把某一类武器。超过数量时，这类武器不能使用。写法示例：
#
# Inventory_Control:
#     Group_Primary:
#         Limit: 2
#     Group_BlaBlaBla:
#         Limit: 2
#     名字随便起:
#         Limit: 2
#
# 分组数量不限。提示和声音可以不写。
# 在武器配置的 Item_Information 模块里，用 Inventory_Control 节点指定武器属于哪个分组。
# 下面这个例子用在默认武器 Bazooka 上。
Inventory_Control:
    Group_Bazookas:
        Limit: 1
        Message_Exceeded: "&e[背包限制] &b快捷栏里最多只能带一把火箭筒。"
        Sounds_Exceeded: LAVA_POP-1-1-0
```

## `Merged_Reload` { #merged_reload }

```yaml title="general.yml · Merged_Reload"
# "合并换弹"指的是给叠在同一格里的多把武器一起换弹。
# 把 Disable 设为 true 可以禁止玩家这样做。
# 提示和声音可以不写。
Merged_Reload:
    Disable: false
    Message_Denied: "&e叠放了多把武器的格子不能换弹。"
    Sounds_Denied: VILLAGER_NO-1-1-0
```
