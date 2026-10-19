---
title: 礼包（Kits.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Kits/Kits.yml
---

# 礼包（Kits.yml）

文件：`plugins/CMI/Kits/Kits.yml`

## `Newbie` { #newbie }

```yaml title="Kits.yml · Newbie"
# 使用指定礼包需要 cmi.kit.[kitName] 权限
# 例如 cmi.kit.newbie 允许使用 newbie 礼包
# 可用自定义变量：{USERNAME} {DISPLAYNAME} {WORLDNAME} {KITNAME} {RANDOMPLAYER}
# 请在游戏内通过 /cmi kiteditor 编辑礼包，避免格式错误
# 命令支持特殊指令格式
Newbie:
  CommandName: Newbie
  Description:
  - "&e花费金钱和经验，换取一些物品"
  - "&e每 X 分钟可使用一次"
  Delay: 36000
  MoneyCost: 100
  ExpCost: 30
  Group: 'groupName'
  Items:
    '1':
      v: 2730
      type: STONE
      amount: 70
      meta:
        ==: ItemMeta
        meta-type: UNSPECIFIC
        display-name: "§3石头"
        lore:
        - "§2名字 §3{USERNAME}"
        - "§3显示名称 §2{DISPLAYNAME}"
        - "§2礼包 §3{KITNAME}"
        - "§3世界名称 §2{WORLDNAME}"
        enchants:
          ARROW_DAMAGE: 3
          THORNS: 5
    '3':
      v: 2730
      type: OAK_PLANKS
      amount: 30
  Commands:
  - "asConsole! msg! [playerName] &e你刚刚领取了 &6{KITNAME} &e礼包！"
  Conditions:
  - cmi.kit.get
  - cmi.command.fly
```

## `Advanced` { #advanced }

```yaml title="Kits.yml · Advanced"
Advanced:
  Delay: 36000
  Items:
    '1':
      v: 2730
      type: STONE
```

## `Ad2` { #ad2 }

```yaml title="Kits.yml · Ad2"
Ad2:
  CommandName: Ad
  Weight: 2
  Delay: 36060
  Group: resources
  Items:
    '1':
      v: 2730
      type: OAK_PLANKS
      amount: 10
```

## `Ad1` { #ad1 }

```yaml title="Kits.yml · Ad1"
Ad1:
  CommandName: Ad
  Weight: 1
  Delay: 36000
  Group: resources
  Items:
    '1':
      v: 2730
      type: STONE
      amount: 10
```

## `Ad3` { #ad3 }

```yaml title="Kits.yml · Ad3"
Ad3:
  Delay: 36001
  Group: resources
  Items:
    '1':
      v: 2730
      type: DIRT
      amount: 10
```
