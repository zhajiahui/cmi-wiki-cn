---
title: 自定义头颅（CustomHeads.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/CustomHeads.yml
---

# 自定义头颅（CustomHeads.yml）

文件：`plugins/CMI/Settings/CustomHeads.yml`

## `LootMobBonus` { #lootmobbonus }

```yaml title="CustomHeads.yml · LootMobBonus"
# 启用后，使用带抢夺附魔的工具时，提高生物头颅掉落概率
# 数值为百分比，按当前掉落概率计算额外增幅
# 例如基础概率 1%，抢夺 3 提供 30% 加成，最终为 1.3%，这是默认值
# 仅影响怪物头颅
# 可复制条目添加任意等级，例如
# Lvl33: 35.5
LootMobBonus:
  Enabled: true
  Lvl1: 5.0
  Lvl2: 15.0
  Lvl3: 30.0
```

## `useDefaultHeadLore` { #usedefaultheadlore }

```yaml title="CustomHeads.yml · useDefaultHeadLore"
# 是否使用默认头颅描述，用于未单独设置描述的头颅
useDefaultHeadLore: true
```

## `defaultHeadLore` { #defaultheadlore }

```yaml title="CustomHeads.yml · defaultHeadLore"
# 头颅未设置描述时使用的默认描述
defaultHeadLore:
- "&7击杀者：&6[playerName]"
```

## `PlayerHead` { #playerhead }

```yaml title="CustomHeads.yml · PlayerHead"
PlayerHead:
  # 是否使用玩家头颅描述
  UseLore: true
  # 玩家头颅掉落时使用的描述
  # 可用全局变量，便于标识死者与击杀者
  # 也支持占位符；需要玩家对象的占位符会以死者为解析对象
  Lore:
  - "&7击杀者：&6[playerName]"
```

## `HeadHandling` { #headhandling }

```yaml title="CustomHeads.yml · HeadHandling"
HeadHandling:
  Maintain:
    # 头颅放置后再破坏时，是否保留自定义名称
    # 原版在放置头颅时会丢弃自定义信息，此项可帮助保留数据
    Name: false
    Lore: false
    Enchants: false
```

## `Player` { #player }

```yaml title="CustomHeads.yml · Player"
Player:
  Drop: false
  # 头颅掉落概率，范围为 0 到 100，可填 0.2 等小数
  # 100 表示每次玩家击杀其他玩家时都会掉头颅
  # 1 表示玩家被另一名玩家击杀时，有 1% 概率掉头颅
  Percentage: 1.0
  # 再次获得同一玩家头颅时，降低掉落概率的百分比，范围为 0 到 100
  # 每次服务器重启后重置
  LowerChanceAfterDrop: 50.0
  # 启用后，使用带抢夺附魔的工具时，提高玩家头颅掉落概率
  # 数值为百分比，按当前掉落概率计算额外增幅
  # 例如基础概率 1%，抢夺 3 提供 30% 加成，最终为 1.3%，这是默认值
  # 仅影响玩家头颅
  # 可复制条目添加任意等级，例如
  # Lvl33: 35.5
  LootBonus:
    Enabled: true
    Lvl1: 5.0
    Lvl2: 15.0
    Lvl3: 30.0
  # 允许掉落玩家头颅的世界，留空包含全部世界
  Worlds: []
```

## `Mob` { #mob }

```yaml title="CustomHeads.yml · Mob"
Mob:
  # 允许生物按指定概率掉落自定义头颅
  # 按实体类型的详细设置见 CustomHeads.yml
  Drop: false
  # 允许掉落生物头颅的世界，留空包含全部世界
  Worlds: []
```

## `EntityHeads` { #entityheads }

```yaml title="CustomHeads.yml · EntityHeads（1/6）"
# 各实体的自定义头颅
# 可添加任意数量的自定义头颅
# 格式为 [dropChance]:[texture]
# 此处概率仅针对这一种头颅
# 每种实体类型另有独立的全局掉落概率
# 强烈建议至少有一种头颅的概率为 100%，否则即使触发了实体的掉落，也可能没有头颅产出
# 可在网上查找自定义贴图
# 同一实体有多种可用头颅时，随机选择
# 自定义头颅格式：[chance]:[HeadName]:c-[options]:lore{"[lore]"}:[texture]
# 详细说明和示例见 www.zrips.net/cmi/extra/custom-mob-heads/
# 可省略贴图字符串开头的 eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUv；缺失时会自动补上
EntityHeads:
  allay:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YmVlYTg0NWNjMGI1OGZmNzYzZGVjZmZlMTFjZDFjODQ1YzVkMDljM2IwNGZlODBiMDY2M2RhNWM3YzY5OWViMyJ9fX0=="
  armadillo:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OTE2NGVkMGUwZWY2OWIwY2U3ODE1ZTQzMDBiNDQxM2E0ODI4ZmNiMDA5MjkxODU0MzU0NWE0MThhNDhlMGMzYyJ9fX0="
  axolotl:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZThhOGEyZDdjY2YwYzM3NDZlMjNhYjU0OTEwNzBlMDkyM2YwNWIyMzVmOWEyZjVkNTNkMzg0MzUzODUzYmRkYyJ9fX0="
  bat:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NGNmMWIzYjNmNTM5ZDJmNjNjMTcyZTk0Y2FjZmFhMzkxZThiMzg1Y2RkNjMzZjNiOTkxYzc0ZTQ0YjI4In19fQ=="
  bee:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OTlkYzNmMDBlY2FiMjI0OWJiNmExNmM4YzUxMTVjZWI5ZjIzMjA1YTBkNTVjYzBlOWJhYmQyNTYyZjc5NTljNCJ9fX0=="
    - "100:默认:ZTZiNzRlMDUyYjc0Mjg4Nzk5YmE2ZDlmMzVjNWQwMjIxY2Y4YjA0MzMxNTQ3ZWMyZjY4ZDczNTk3YWUyYzliIn19fQ=="
    - "100:默认:YmIxNzc3NDY2MjUxMmQ3ODdlZjc3YjFhNDZhMDRlMmM2ZmQ2Nzc5NGJmN2Y3Nzk1NjZlYjIxYzgxNDNhYWQ5ZSJ9fX0="
    - "100:默认:OTQ3MzIyZjgzMWUzYzE2OGNmYmQzZTI4ZmU5MjUxNDRiMjYxZTc5ZWIzOWM3NzEzNDlmYWM1NWE4MTI2NDczIn19fQ=="
  blaze:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Yjc4ZWYyZTRjZjJjNDFhMmQxNGJmZGU5Y2FmZjEwMjE5ZjViMWJmNWIzNWE0OWViNTFjNjQ2Nzg4MmNiNWYwIn19fQ=="
  bogged:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTNiOTAwM2JhMmQwNTU2MmM3NTExOWI4YTYyMTg1YzY3MTMwZTkyODJmN2FjYmFjNGJjMjgyNGMyMWViOTVkOSJ9fX0="
  breeze:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTI3NTcyOGFmN2U2YTI5Yzg4MTI1YjY3NWEzOWQ4OGFlOTkxOWJiNjFmZGMyMDAzMzdmZWQ2YWIwYzQ5ZDY1YyJ9fX0="
  camel:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NzRiOGEzMzNkZmE5MmU3ZTVhOTVhZDRhZTJkODRiMWJhZmEzM2RjMjhjMDU0OTI1Mjc3ZjYwZTc5ZGFmYzhjNCJ9fX0="
  camel_husk:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:M2JkN2E5MmE2ZjY3Yjc1MDBkMTZjNGUxMmYyODA1OGVjMjg1OTMxMTU1NmJhMDNiZTJkMWY1ODExNzBmMmRiNiJ9fX0="
  cat:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NTg4MDNmMDI3MGY4Y2RmNGUwZmU5NzMyZDQ5NjdjY2NjMGEyZjRmY2QxMThjZDE1MDAwOTc5YjE4ODg1MTQ0ZiJ9fX0="
    - "100:默认:N2M5Yjc0MDllN2I1MzgzYzE5YjM2MmIyYTBjYjQzZDUwOTNiMTNlMmIyMzRlOGExODkxNTYzZTU1ZWFlOWQ2OCJ9fX0="
  cave_spider:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NDE2NDVkZmQ3N2QwOTkyMzEwN2IzNDk2ZTk0ZWViNWMzMDMyOWY5N2VmYzk2ZWQ3NmUyMjZlOTgyMjQifX19"
  chicken:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MTYzODQ2OWE1OTljZWVmNzIwNzUzNzYwMzI0OGE5YWIxMWZmNTkxZmQzNzhiZWE0NzM1YjM0NmE3ZmFlODkzIn19fQ=="
  cod:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NmY5OWI1ODBkNDVhNzg0ZTdhOTY0ZTdkM2IxZjk3Y2VjZTc0OTExMTczYmQyMWMxZDdjNTZhY2RjMzg1ZWQ1In19fQ=="
  copper_golem:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OTllMjRlOTRkYmU0MmUyMzBkODMyOTNhNzdkNjFmZjcxMDFhOGM2OGFiNjhiYmM2YTkzZjk2MzBmYjJmZGI0In19fQ=="
    - "100:默认:Y2MyYWFiOGEwZmVjM2NjMDZhNGQ0NzQ4MGUwMjRmODhmMmIwN2JjOTZlZTA5ZTUzMzFlNWY0ZGI2YjI3Mzg4NSJ9fX0="
    - "100:默认:OTgyZDVjOTQ0ZjgwNzk1ZDYxM2MyMjQwNWMwMjdlZGJkMmE1NTQ0ODgyYWNiYWI5NzRhMDJmNTQ3YzE1NDY4ZCJ9fX0="
  cow:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NWQ2YzZlZGE5NDJmN2Y1ZjcxYzMxNjFjNzMwNmY0YWVkMzA3ZDgyODk1ZjlkMmIwN2FiNDUyNTcxOGVkYzUifX19"
    - "100:默认:YzVhOWNkNThkNGM2N2JjY2M4ZmIxZjVmNzU2YTJkMzgxYzlmZmFjMjkyNGI3ZjRjYjcxYWE5ZmExM2ZiNWMifX19"
```

```yaml title="CustomHeads.yml · EntityHeads（2/6）"
EntityHeads:
  creaking:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZGUzNzNmYTUzNGM3YzNmOTM0MGQzM2MzMmMyMTM0MDJhMmNmODkxN2U3NTBlYjhiYzg3MTBmY2QzZWU5YTE1ZCJ9fX0="
  creeper:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZjQyNTQ4MzhjMzNlYTIyN2ZmY2EyMjNkZGRhYWJmZTBiMDIxNWY3MGRhNjQ5ZTk0NDQ3N2Y0NDM3MGNhNjk1MiJ9fX0="
    - "100:默认:YTNmMTcyZDI5Y2Y5NGJjODk1NjA4YjdhNWRjMmFmMGRlNDljNzg4ZDViZWNiMTYwNWYxZjUzNDg4YTAxNzBiOCJ9fX0="
    - "100:闪电苦力怕:c-powered:ZjJjZWIzOWRkNGRlMjRhN2FkZmUyOTFhM2EwY2ZjN2NmNGY2NDVkZTU5YjYwM2ZjZmUwNmM2YjVhMDZlMjYifX19"
  dolphin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OGU5Njg4Yjk1MGQ4ODBiNTViN2FhMmNmY2Q3NmU1YTBmYTk0YWFjNmQxNmY3OGU4MzNmNzQ0M2VhMjlmZWQzIn19fQ=="
  donkey:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZGZiNmMzYzA1MmNmNzg3ZDIzNmEyOTE1ZjgwNzJiNzdjNTQ3NDk3NzE1ZDFkMmY4Y2JjOWQyNDFkODhhIn19fQ=="
  drowned:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NTZkYWY1MGVhZjc2YzNhNmQ1YWQzOWM5NjZmMjk4NzdiOTFkOTUwZGQxZTM3MTIyZTljODE5NTg1Yzg5ZDkyZSJ9fX0="
    - "100:默认:YzNmN2NjZjYxZGJjM2Y5ZmU5YTYzMzNjZGUwYzBlMTQzOTllYjJlZWE3MWQzNGNmMjIzYjNhY2UyMjA1MSJ9fX0="
    - "100:默认:MWY4YmFhNDhiOGY1MTE5OTBlNDdkYjk2ODMyNGMxNTJiZDExNjc3MzFkZGYwMzQ1MzAwNDQ3MzVhNmJkMmVkNCJ9fX0="
    - "100:默认:YzFhNzMyNTI0MDFhNmU5NDZmNjFkYmFjMGUwMjdkMTgzZTBhY2U1ODc1MmZhMTVhNjRkMjQ0OWZjZjUwODdiNyJ9fX0="
    - "100:默认:ZmIxNTMxYzA0ZTI1ZDdmYTY0NTc2OTgyNjg0OTFjYjg5NmQzMzAyZDI2ODg0ZmNmZGYxYTBiMmY5MmQ3N2M4ZiJ9fX0="
    - "100:默认:Yzg0ZGY3OWM0OTEwNGIxOThjZGFkNmQ5OWZkMGQwYmNmMTUzMWM5MmQ0YWI2MjY5ZTQwYjdkM2NiYmI4ZTk4YyJ9fX0="
  elder_guardian:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MWM3OTc0ODJhMTRiZmNiODc3MjU3Y2IyY2ZmMWI2ZTZhOGI4NDEzMzM2ZmZiNGMyOWE2MTM5Mjc4YjQzNmIifX19"
  ender_dragon:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZmZjZGFlNTg2YjUyNDAzYjkyYjE4NTdlZTQzMzFiYWM2MzZhZjA4YmFiOTJiYTU3NTBhNTRhODMzMzFhNjM1MyJ9fX0="
  enderman:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:N2E1OWJiMGE3YTMyOTY1YjNkOTBkOGVhZmE4OTlkMTgzNWY0MjQ1MDllYWRkNGU2YjcwOWFkYTUwYjljZiJ9fX0="
  endermite:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODRhYWZmYTRjMDllMmVhZmI4NWQzNTIyMTIyZGIwYWE0NTg3NGJlYTRlM2Y1ZTc1NjZiNGQxNjZjN2RmOCJ9fX0="
  evoker:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTAwZDNmZmYxNmMyZGNhNTliOWM1OGYwOTY1MjVjODY5NzExNjZkYmFlMTMzYjFiMDUwZTVlZTcxNjQ0MyJ9fX0="
  fox:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MjRhMDM0NzQzNjQzNGViMTNkNTM3YjllYjZiNDViNmVmNGM1YTc4Zjg2ZTkxODYzZWY2MWQyYjhhNTNiODIifX19"
    - "100:默认:YjZmZWI3NjFiMmY1OWZhYmU1Y2MzY2M4MmE5MzRiNTM0ZWE5OWVkYjkxMzJjY2RhOWY0ODRiZDU5ODZkNyJ9fX0="
    - "100:默认:MTZkYjdkNTA3Mzg5YTE0YmJlYzM5ZGU2OTIyMTY1YjMyZDQzNjU3YmNiNmFhZjRiNTE4MjgyNWIyMmI0In19fQ=="
  frog:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZDBlZGNiODk4MzU2ZmQ0MDBjMjA1YzYxMzRlMDk4NjEwYmFmYmJjNTA0MTc3MjlhMTU1Y2U3N2Q3YmNhOThkNCJ9fX0="
  ghast:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OGI2YTcyMTM4ZDY5ZmJiZDJmZWEzZmEyNTFjYWJkODcxNTJlNGYxYzk3ZTVmOTg2YmY2ODU1NzFkYjNjYzAifX19"
  giant:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZWM0NTViMzgzNjhkYWU3MzBlZjE0ODNjMWRmMjVjZDg3YjQxYmVlNDQxZWYzYWIxZjNjNjBmMjFiZmUwZTUxMSJ9fX0="
  glow_squid:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MmVjZDBiNWViNmIzODRkYjA3NmQ4NDQ2MDY1MjAyOTU5ZGRkZmYwMTYxZTBkNzIzYjNkZjBjYzU4NmQxNmJiZCJ9fX0="
  goat:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:M2E0OTg2ZmRmMDRjYzg2ZDhhZmYyMDM3YTZiNGRmNTczY2RjMWU3MDhkMDU3OTBjNzY3MjhmYWVmNzk2ZjMzYSJ9fX0="
  guardian:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZGZiNjc1Y2I1YTdlM2ZkMjVlMjlkYTgyNThmMjRmYzAyMGIzZmE5NTAzNjJiOGJjOGViMjUyZTU2ZTc0In19fQ=="
```

```yaml title="CustomHeads.yml · EntityHeads（3/6）"
EntityHeads:
  happy_ghast:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTFhMzZjYjkzZDAxNjc1YzQ2MjJkZDVjOGQ4NzIxMTA5MTFlYzEyYzM3MmU4OWFmYThiYTAzODYyODY3ZjZmYiJ9fX0="
    - "100:默认:ZWM3OWY5MDgyZjZhYmVlZDk3NTA3NDQ0M2JlOGM4YTc5ZWExMDYwZDYxMDk0ZmY3OWEwNDk4OTM0MDQzMDYyNCJ9fX0="
    - "100:默认:MjRiNWE0NzJkY2U5MzUwNWQ0YTQ0MDFhNzRjZTI5ZWNlZTg4ZTMyNjQyOGJjMTAzY2JhZDRkOTM5YWJlZDFiIn19fQ=="
  hoglin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OWJiOWJjMGYwMWRiZDc2MmEwOGQ5ZTc3YzA4MDY5ZWQ3Yzk1MzY0YWEzMGNhMTA3MjIwODU2MWI3MzBlOGQ3NSJ9fX0="
  horse:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NjE5MDI4OTgzMDg3MzBjNDc0NzI5OWNiNWE1ZGE5YzI1ODM4YjFkMDU5ZmU0NmZjMzY4OTZmZWU2NjI3MjkifX19"
  husk:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Nzc3MDY4MWQxYTI1NWZiNGY3NTQ3OTNhYTA1NWIyMjA0NDFjZGFiOWUxMTQxZGZhNTIzN2I0OTkzMWQ5YjkxYyJ9fX0="
  illusioner:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MmYyODgyZGQwOTcyM2U0N2MwYWI5NjYzZWFiMDgzZDZhNTk2OTI3MzcwNjExMGM4MjkxMGU2MWJmOGE4ZjA3ZSJ9fX0="
    - "100:默认:NTEyNTEyZTdkMDE2YTIzNDNhN2JmZjFhNGNkMTUzNTdhYjg1MTU3OWYxMzg5YmQ0ZTNhMjRjYmViODhiIn19fQ=="
  iron_golem:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODkwOTFkNzllYTBmNTllZjdlZjk0ZDdiYmE2ZTVmMTdmMmY3ZDQ1NzJjNDRmOTBmNzZjNDgxOWE3MTQifX19"
  llama:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NGQ2N2ZkNGJmZjI5MzI2OWNiOTA4OTc0ZGNhODNjMzM0ODVlNDM1ZWQ1YThlMWRiZDY1MjFjNjE2ODcxNDAifX19"
    - "100:默认:ODAyNzdlNmIzZDlmNzgxOWVmYzdkYTRiNDI3NDVmN2FiOWE2M2JhOGYzNmQ2Yjg0YTdhMjUwYzZkMWEzNThlYiJ9fX0="
    - "100:默认:YzJiMWVjZmY3N2ZmZTNiNTAzYzMwYTU0OGViMjNhMWEwOGZhMjZmZDY3Y2RmZjM4OTg1NWQ3NDkyMTM2OCJ9fX0="
    - "100:默认:Y2YyNGU1NmZkOWZmZDcxMzNkYTZkMWYzZTJmNDU1OTUyYjFkYTQ2MjY4NmY3NTNjNTk3ZWU4MjI5OWEifX19"
  magma_cube:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Mzg5NTdkNTAyM2M5MzdjNGM0MWFhMjQxMmQ0MzQxMGJkYTIzY2Y3OWE5ZjZhYjM2Yjc2ZmVmMmQ3YzQyOSJ9fX0="
  mannequin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads: []
  mooshroom:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZDBiYzYxYjk3NTdhN2I4M2UwM2NkMjUwN2EyMTU3OTEzYzJjZjAxNmU3YzA5NmE0ZDZjZjFmZTFiOGRiIn19fQ=="
  mule:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTA0ODZhNzQyZTdkZGEwYmFlNjFjZTJmNTVmYTEzNTI3ZjFjM2IzMzRjNTdjMDM0YmI0Y2YxMzJmYjVmNWYifX19"
  nautilus:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZmIxNjQ4NDgyNzMzYTdjM2JiODRiZTQ2OGQ1NzVlM2ZiZDNmZjE5MzI4MWIwNzI3ZWFkOGRlYWRlYTYwMjM3YSJ9fX0="
    - "100:默认:M2JiMzQwZGQzMzAyNjE1MzQ4ZGU1MTYyZmUxNjcwYjljNWM5YzYxNmNkOTJkMmRlOWQ4Mzk4Y2IzM2U4NDJhZSJ9fX0="
  ocelot:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YWI4ODFjMzliM2FmZGNjNzlmOTFmZTVkZTNjZGQwMTViYzMzNTM4NDNmNTkxZjRkMjNjZDMwMjdkZTRlNiJ9fX0="
    - "100:默认:NTY1N2NkNWMyOTg5ZmY5NzU3MGZlYzRkZGNkYzY5MjZhNjhhMzM5MzI1MGMxYmUxZjBiMTE0YTFkYjEifX19"
    - "100:默认:YTc1NWU3ZGYwNGQxOGIzMWQ2M2MxN2Y0YTdiNGM3MzkyNGJkNjI2NWRhNjllMTEzZWRkZDk3NTE2ZmM3In19fQ=="
    - "100:默认:ZjJhNjYyZjJhZTdkZWJlZTY1MjkyYzJiZjQyZmJiMDliOTdiMmZmYmRiMjcwNTIwYzJkYjk2ZTUxZDg5NDUifX19"
  panda:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZDE4OGM5ODBhYWNmYTk0Y2YzMzA4ODUxMmIxYjk1MTdiYTgyNmIxNTRkNGNhZmMyNjJhZmY2OTc3YmU4YSJ9fX0="
  parched:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MjRhZWNlZmY1ZjI2ZGQ4NDEzYzVjMDM1NDdjMjM0YWMwMzEwOGQxODdhZjBiOWNkODM0YThjZTEyNTk4NTkxYyJ9fX0="
  parrot:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Yjc4ZTFjNWY0OGE3ZTEyYjI2Mjg1MzU3MWVmMWY1OTdhOTJlZjU4ZGE4ZmFhZmUwN2JiN2MwZTY5ZTkzIn19fQ=="
    - "100:默认:ZGFjNjcwM2RlZDQ2ZDkzOWE2MjBmZTIyYzQzZTE4Njc0ZTEzZDIzYzk3NDRiZTAzNmIzNDgzYzFkMWNkZCJ9fX0="
    - "100:默认:M2Q2ZjRhMjFlMGQ2MmFmODI0Zjg3MDhhYzYzNDEwZjFhMDFiYmI0MWQ3ZjRhNzAyZDk0NjljNjExMzIyMiJ9fX0="
    - "100:默认:ZjBiZmE4NTBmNWRlNGIyOTgxY2NlNzhmNTJmYzJjYzdjZDdiNWM2MmNhZWZlZGRlYjljZjMxMWU4M2Q5MDk3In19fQ=="
    - "100:默认:ZjhhODJjOGI3NWRkMWMyY2U4MTMzYzBiYTkzOWI4YzUyZTQ3ZDNlYzM3NDk1MGY0N2RkZGJiZTM0NWUyMCJ9fX0="
    - "100:默认:YTRiYThkNjZmZWNiMTk5MmU5NGI4Njg3ZDZhYjRhNTMyMGFiNzU5NGFjMTk0YTI2MTVlZDRkZjgxOGVkYmMzIn19fQ=="
    - "100:默认:YWI5YTM2YzU1ODlmM2EyZTU5YzFjYWE5YjNiODhmYWRhNzY3MzJiZGI0YTc5MjYzODhhOGMwODhiYmJjYiJ9fX0="
    - "100:默认:YWNhNTgwYjA1MWM2M2JlMjlkYTU0NWE5YWE3ZmY3ZTEzNmRmNzdhODFjNjdkYzFlZTllNjE3MGMxNGZiMzEwIn19fQ=="
    - "100:默认:MmI5NGYyMzZjNGE2NDJlYjJiY2RjMzU4OWI5YzNjNGEwYjViZDVkZjljZDVkNjhmMzdmOGM4M2Y4ZTNmMSJ9fX0="
```

```yaml title="CustomHeads.yml · EntityHeads（4/6）"
EntityHeads:
  phantom:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YWQyZmE1NjE4NDQ3NzYyZTI2MTExZTA2MGRjNTkzZWE2MjJkNWRkZmMzODVkN2U0MjUzMmU0NjMyN2Y4MDdjMCJ9fX0="
    - "100:默认:NDExZDI1YmNkYWJhZmFkNWZkNmUwMTBjNWIxY2Y3YTAwYzljY2E0MGM1YTQ2NzQ3ZjcwNmRjOWNiM2EifX19"
  pig:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YzNhYmQ0NGFlNjdkOWM5MjU0ZDE3N2U5NjU4ZGE4NDg0MzM4OWQ1ZTFmZmQyYWYxZmI1MTIxN2M3NWMyOTgifX19"
    - "100:默认:NjIxNjY4ZWY3Y2I3OWRkOWMyMmNlM2QxZjNmNGNiNmUyNTU5ODkzYjZkZjRhNDY5NTE0ZTY2N2MxNmFhNCJ9fX0="
  piglin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:OWYxODEwN2QyNzVmMWNiM2E5Zjk3M2U1OTI4ZDU4NzlmYTQwMzI4ZmYzMjU4MDU0ZGI2ZGQzZTdjMGNhNjMzMCJ9fX0="
  piglin_brute:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:M2UzMDBlOTAyNzM0OWM0OTA3NDk3NDM4YmFjMjllM2E0Yzg3YTg0OGM1MGIzNGMyMTI0MjcyN2I1N2Y0ZTFjZiJ9fX0="
  pillager:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NGFlZTZiYjM3Y2JmYzkyYjBkODZkYjVhZGE0NzkwYzY0ZmY0NDY4ZDY4Yjg0OTQyZmRlMDQ0MDVlOGVmNTMzMyJ9fX0="
  polar_bear:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZDQ2ZDIzZjA0ODQ2MzY5ZmEyYTM3MDJjMTBmNzU5MTAxYWY3YmZlODQxOTk2NjQyOTUzM2NkODFhMTFkMmIifX19"
  pufferfish:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTk1NTkzODg5OTNmZTc4MmY2N2JkNThkOThjNGRmNTZiY2Q0MzBlZGNiMmY2NmVmNTc3N2E3M2MyN2RlMyJ9fX0="
  rabbit:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Yzk3N2EzMjY2YmYzYjllYWYxN2U1YTAyZWE1ZmJiNDY4MDExNTk4NjNkZDI4OGI5M2U2YzEyYzljYiJ9fX0="
    - "100:默认:NzJjNTgxMTZhMTQ3ZDFhOWEyNjI2OTIyNGE4YmUxODRmZThlNWYzZjNkZjliNjE3NTEzNjlhZDg3MzgyZWM5In19fQ=="
    - "100:默认:Y2I4Y2ZmNGIxNWI4Y2EzN2UyNTc1MGYzNDU3MThmMjg5Y2IyMmM1YjNhZDIyNjI3YTcxMjIzZmFjY2MifX19"
  ravager:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MWNiOWYxMzlmOTQ4OWQ4NmU0MTBhMDZkOGNiYzY3MGM4MDI4MTM3NTA4ZTNlNGJlZjYxMmZlMzJlZGQ2MDE5MyJ9fX0="
    - "100:默认:M2I2MjUwMWNkMWI4N2IzN2Y2MjgwMTgyMTBlYzU0MDBjYjY1YTRkMWFhYjc0ZTZhM2Y3ZjYyYWE4NWRiOTdlZSJ9fX0="
  salmon:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YWRmYzU3ZDA5MDU5ZTQ3OTlmYTkyYzE1ZTI4NTEyYmNmYWExMzE1NTc3ZmUzYTI3YWVkMzg5ZTRmNzUyMjg5YSJ9fX0="
  sheep:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:品红色绵羊:c-magenta:MTgzNjU2NWM3ODk3ZDQ5YTcxYmMxODk4NmQxZWE2NTYxMzIxYTBiYmY3MTFkNDFhNTZjZTNiYjJjMjE3ZTdhIn19fQ=="
    - "100:棕色绵羊:c-brown:YTU1YWQ2ZTVkYjU2OTJkODdmNTE1MTFmNGUwOWIzOWZmOWNjYjNkZTdiNDgxOWE3Mzc4ZmNlODU1M2I4In19fQ=="
    - "100:紫色绵羊:c-purple:YWU1Mjg2N2FmZWYzOGJiMTRhMjZkMTQyNmM4YzBmMTE2YWQzNDc2MWFjZDkyZTdhYWUyYzgxOWEwZDU1Yjg1In19fQ=="
    - "100:粉红色绵羊:c-pink:MmFjNzRhMmI5YjkxNDUyZTU2ZmExZGRhNWRiODEwNzc4NTZlNDlmMjdjNmUyZGUxZTg0MWU1Yzk1YTZmYzVhYiJ9fX0="
    - "100:绿色绵羊:c-green:YTAxNzIxNWM3ZjhkYjgyMDQwYWEyYzQ3Mjk4YjY2NTQxYzJlYjVmN2Y5MzA0MGE1ZDIzZDg4ZjA2ODdkNGIzNCJ9fX0="
    - "100:黄绿色绵羊:c-lime:OTJhMjQ0OGY1OGE0OTEzMzI0MzRlODVjNDVkNzg2ZDg3NDM5N2U4MzBhM2E3ODk0ZTZkOTI2OTljNDJiMzAifX19"
    - "100:青色绵羊:c-cyan:MWM4YTk3YTM4ODU2NTE0YTE2NDEzZTJjOTk1MjEyODlmNGM1MzYzZGM4MmZjOWIyODM0Y2ZlZGFjNzhiODkifX19"
    - "100:橙色绵羊:c-orange:ZjA5ODM5N2EyNzBiNGMzZDJiMWU1NzRiOGNmZDNjYzRlYTM0MDkwNjZjZWZlMzFlYTk5MzYzM2M5ZDU3NiJ9fX0="
    - "100:蓝色绵羊:c-blue:ZDllYzIyODE4ZDFmYmZjODE2N2ZiZTM2NzI4YjI4MjQwZTM0ZTE2NDY5YTI5MjlkMDNmZGY1MTFiZjJjYTEifX19"
    - "100:淡蓝色绵羊:c-light_blue:NDZmNmM3ZTdmZDUxNGNlMGFjYzY4NTkzMjI5ZTQwZmNjNDM1MmI4NDE2NDZlNGYwZWJjY2NiMGNlMjNkMTYifX19"
    - "100:黄色绵羊:c-yellow:MjZhNDExMmRmMWU0YmNlMmE1ZTI4NDE3ZjNhYWZmNzljZDY2ZTg4NWMzNzI0NTU0MTAyY2VmOGViOCJ9fX0="
    - "100:淡灰色绵羊:c-light_gray:Y2UxYWM2ODM5OTNiZTM1NTEyZTFiZTMxZDFmNGY5OGU1ODNlZGIxNjU4YTllMjExOTJjOWIyM2I1Y2NjZGMzIn19fQ=="
    - "100:红色绵羊:c-red:ODM5YWY0NzdlYjYyNzgxNWY3MjNhNTY2MjU1NmVjOWRmY2JhYjVkNDk0ZDMzOGJkMjE0MjMyZjIzZTQ0NiJ9fX0="
    - "100:黑色绵羊:c-black:MzI2NTIwODNmMjhlZDFiNjFmOWI5NjVkZjFhYmYwMTBmMjM0NjgxYzIxNDM1OTUxYzY3ZDg4MzY0NzQ5ODIyIn19fQ=="
    - "100:灰色绵羊:c-gray:NDI4N2ViNTAxMzkxZjI3NTM4OWYxNjZlYzlmZWJlYTc1ZWM0YWU5NTFiODhiMzhjYWU4N2RmN2UyNGY0YyJ9fX0="
    - "100:白色绵羊:c-white:ZjMxZjljY2M2YjNlMzJlY2YxM2I4YTExYWMyOWNkMzNkMThjOTVmYzczZGI4YTY2YzVkNjU3Y2NiOGJlNzAifX19"
  shulker:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MWU3MzgzMmUyNzJmODg0NGM0NzY4NDZiYzQyNGEzNDMyZmI2OThjNThlNmVmMmE5ODcxYzdkMjlhZWVhNyJ9fX0="
  silverfish:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZGE5MWRhYjgzOTFhZjVmZGE1NGFjZDJjMGIxOGZiZDgxOWI4NjVlMWE4ZjFkNjIzODEzZmE3NjFlOTI0NTQwIn19fQ=="
  skeleton:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MzAxMjY4ZTljNDkyZGExZjBkODgyNzFjYjQ5MmE0YjMwMjM5NWY1MTVhN2JiZjc3ZjRhMjBiOTVmYzAyZWIyIn19fQ=="
    - "100:默认:Yjk1MDc4ZDNiM2IxNzAxZDQ1NzI5ZDNhMTQyMjQ2N2IyOWRiYjJlMWE5MTI4MTMzYTJmMTYzZWJlODVkMmRiOSJ9fX0="
  skeleton_horse:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NDdlZmZjZTM1MTMyYzg2ZmY3MmJjYWU3N2RmYmIxZDIyNTg3ZTk0ZGYzY2JjMjU3MGVkMTdjZjg5NzNhIn19fQ=="
```

```yaml title="CustomHeads.yml · EntityHeads（5/6）"
EntityHeads:
  slime:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MTZhZDIwZmMyZDU3OWJlMjUwZDNkYjY1OWM4MzJkYTJiNDc4YTczYTY5OGI3ZWExMGQxOGM5MTYyZTRkOWI1In19fQ=="
  sniffer:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODdhZDkyMGE2NmUzOGNjMzQyNmE1YmZmMDg0NjY3ZTg3NzIxMTY5MTVlMjk4MDk4NTY3YzEzOWYyMjJlMmM0MiJ9fX0="
  snow_golem:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MWZkZmQxZjc1MzhjMDQwMjU4YmU3YTkxNDQ2ZGE4OWVkODQ1Y2M1ZWY3MjhlYjVlNjkwNTQzMzc4ZmNmNCJ9fX0="
  spider:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Y2Q1NDE1NDFkYWFmZjUwODk2Y2QyNThiZGJkZDRjZjgwYzNiYTgxNjczNTcyNjA3OGJmZTM5MzkyN2U1N2YxIn19fQ=="
  squid:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MDE0MzNiZTI0MjM2NmFmMTI2ZGE0MzRiODczNWRmMWViNWIzY2IyY2VkZTM5MTQ1OTc0ZTljNDgzNjA3YmFjIn19fQ=="
  stray:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NzhkZGY3NmU1NTVkZDVjNGFhOGEwYTVmYzU4NDUyMGNkNjNkNDg5YzI1M2RlOTY5ZjdmMjJmODVhOWEyZDU2In19fQ=="
  strider:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MThhOWFkZjc4MGVjN2RkNDYyNWM5YzA3NzkwNTJlNmExNWE0NTE4NjY2MjM1MTFlNGM4MmU5NjU1NzE0YjNjMSJ9fX0="
  tadpole:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YjIzZWJmMjZiN2E0NDFlMTBhODZmYjVjMmE1ZjNiNTE5MjU4YTVjNWRkZGQ2YTFhNzU1NDlmNTE3MzMyODE1YiJ9fX0="
  trader_llama:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODQyNDc4MGIzYzVjNTM1MWNmNDlmYjViZjQxZmNiMjg5NDkxZGY2YzQzMDY4M2M4NGQ3ODQ2MTg4ZGI0Zjg0ZCJ9fX0="
    - "100:默认:YmU0ZDhhMGJjMTVmMjM5OTIxZWZkOGJlMzQ4MGJhNzdhOThlZTdkOWNlMDA3MjhjMGQ3MzNmMGEyZDYxNGQxNiJ9fX0="
    - "100:默认:NzA4N2E1NTZkNGZmYTk1ZWNkMjg0NGYzNTBkYzQzZTI1NGU1ZDUzNWZhNTk2ZjU0MGQ3ZTc3ZmE2N2RmNDY5NiJ9fX0="
  tropical_fish:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MzZkMTQ5ZTRkNDk5OTI5NjcyZTI3Njg5NDllNjQ3Nzk1OWMyMWU2NTI1NDYxM2IzMjdiNTM4ZGYxZTRkZiJ9fX0="
  turtle:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MGE0MDUwZTdhYWNjNDUzOTIwMjY1OGZkYzMzOWRkMTgyZDdlMzIyZjlmYmNjNGQ1Zjk5YjU3MThhIn19fQ=="
  vex:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NWU3MzMwYzdkNWNkOGEwYTU1YWI5ZTk1MzIxNTM1YWM3YWUzMGZlODM3YzM3ZWE5ZTUzYmVhN2JhMmRlODZiIn19fQ=="
  villager:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODIyZDhlNzUxYzhmMmZkNGM4OTQyYzQ0YmRiMmY1Y2E0ZDhhZThlNTc1ZWQzZWIzNGMxOGE4NmU5M2IifX19"
  vindicator:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZGFlZWQ5ZDhlZDE3NjllNzdlM2NmZTExZGMxNzk2NjhlZDBkYjFkZTZjZTI5ZjFjOGUwZDVmZTVlNjU3M2I2MCJ9fX0="
  wandering_trader:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NWYxMzc5YTgyMjkwZDdhYmUxZWZhYWJiYzcwNzEwZmYyZWMwMmRkMzRhZGUzODZiYzAwYzkzMGM0NjFjZjkzMiJ9fX0="
  warden:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NmNmMzY3NGIyZGRjMGVmN2MzOWUzYjljNmI1ODY3N2RlNWNmMzc3ZDJlYjA3M2YyZjNmZTUwOTE5YjFjYTRjOSJ9fX0="
  witch:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ODllOGI1ZjE1YTliMjlhMWUzODljOTUyMThmZDM3OTVmMzI4NzJlNWFlZTk0NjRhNzY0OTVjNTI3ZDIyNDUifX19"
  wither:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:YTQzNTE2NGMwNWNlYTI5OWEzZjAxNmJiYmVkMDU3MDZlYmI3MjBkYWM5MTJjZTQzNTFjMjI5NjYyNmFlY2Q5YSJ9fX0="
    - "100:默认:M2U0ZjQ5NTM1YTI3NmFhY2M0ZGM4NDEzM2JmZTgxYmU1ZjJhNDc5OWE0YzA0ZDlhNGRkYjcyZDgxOWVjMmIyYiJ9fX0="
    - "100:默认:Y2RmNzRlMzIzZWQ0MTQzNjk2NWY1YzU3ZGRmMjgxNWQ1MzMyZmU5OTllNjhmYmI5ZDZjZjVjOGJkNDEzOWYifX19"
    - "100:默认:OTY0ZTFjM2UzMTVjOGQ4ZmZmYzM3OTg1YjY2ODFjNWJkMTZhNmY5N2ZmZDA3MTk5ZThhMDVlZmJlZjEwMzc5MyJ9fX0="
    - "100:默认:ZGRhZmIyM2VmYzU3ZjI1MTg3OGU1MzI4ZDExY2IwZWVmODdiNzljODdiMjU0YTdlYzcyMjk2ZjkzNjNlZjdjIn19fQ=="
```

```yaml title="CustomHeads.yml · EntityHeads（6/6）"
EntityHeads:
  wither_skeleton:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:Nzk1M2I2YzY4NDQ4ZTdlNmI2YmY4ZmIyNzNkNzIwM2FjZDhlMWJlMTllODE0ODFlYWQ1MWY0NWRlNTlhOCJ9fX0="
    - "100:默认:ZjVlYzk2NDY0NWE4ZWZhYzc2YmUyZjE2MGQ3Yzk5NTYzNjJmMzJiNjUxNzM5MGM1OWMzMDg1MDM0ZjA1MGNmZiJ9fX0="
    - "100:默认:NDk2YmM4ZWJkNGUxM2Y0OTZkOGQ3NGM1NjVkZDU2ZTk5YTRhZjJlMmVhN2EyN2E5NmMxYWJkMjg0MTg0YiJ9fX0="
  wolf:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NjlkMWQzMTEzZWM0M2FjMjk2MWRkNTlmMjgxNzVmYjQ3MTg4NzNjNmM0NDhkZmNhODcyMjMxN2Q2NyJ9fX0="
    - "100:愤怒的狼:c-angry:ZTk1Y2JiNGY3NWVhODc2MTdmMmY3MTNjNmQ0OWRhYzMyMDliYTFiZDRiOTM2OTY1NGIxNDU5ZWExNTMxNyJ9fX0="
  zoglin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZTY3ZTE4NjAyZTAzMDM1YWQ2ODk2N2NlMDkwMjM1ZDg5OTY2NjNmYjllYTQ3NTc4ZDNhN2ViYmM0MmE1Y2NmOSJ9fX0="
  zombie:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:NTZmYzg1NGJiODRjZjRiNzY5NzI5Nzk3M2UwMmI3OWJjMTA2OTg0NjBiNTFhNjM5YzYwZTVlNDE3NzM0ZTExIn19fQ=="
    - "100:默认:MzExZGQ5MWVlNGQzMWRkZDU5MWQyODMyZWExZWMwODBmMmVkZWQzM2FiODllZTFkYjhiMDRiMjZhNjhhIn19fQ=="
  zombie_horse:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZDIyOTUwZjJkM2VmZGRiMThkZTg2ZjhmNTVhYzUxOGRjZTczZjEyYTZlMGY4NjM2ZDU1MWQ4ZWI0ODBjZWVjIn19fQ=="
  zombie_nautilus:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:ZmQ5YTkzMzM3NmRhNDRjMzM5MTMwN2NiOWY0Y2YwM2YxNmYzYTU0ZjQ5NWZkNWExMWJhZDhhMzczZjlkNTcyMCJ9fX0="
  zombie_villager:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:MzdlODM4Y2NjMjY3NzZhMjE3YzY3ODM4NmY2YTY1NzkxZmU4Y2RhYjhjZTljYTRhYzZiMjgzOTdhNGQ4MWMyMiJ9fX0="
    - "100:默认:Y2ZmMDQ4MmZkMzJmYWIyY2U5ZjVmYTJlMmQ5YjRkYzc1NjFkYTQyMjE1MmM5OWZjODA0YjkxMzljYWYyNTZiIn19fQ=="
    - "100:默认:OTYxZjE5ZmZkOGFlNDI1NzkyYzRiMTgxNzU2YWRmZjhkNDgxNzRhZWVmNThhMGYzMjdhMjhjNzQyYzcyNDQyIn19fQ=="
    - "100:默认:YTE2MTU1ZmNmMzY2Y2Y0ZTA2Y2U1ZGZmYzQ4Y2E1NGU4ZWE0OGRmZTUyNTM1OGI2MTJkYzQ0ZmQ0MzIifX19"
    - "100:默认:NDRmMDhlYmQ0ZTI1Y2RhM2FkZTQ1Yjg2MzM3OGFkMzc3ZjE4YzUxMGRiNGQyOGU4MmJiMjQ0NTE0MzliMzczNCJ9fX0="
    - "100:默认:NTI4YzJiYWQ1Mzg5Y2IzNTkyYjU2NWIzYzQ3ZWNjMTg5ZTA1NDJhODc4MzUwMjhkNjE0OGJiZTMzNDU2NDUifX19"
  zombified_piglin:
    DropChance: 1.0
    LowerWithEachDrop: 50.0
    Heads:
    - "100:默认:N2VhYmFlY2M1ZmFlNWE4YTQ5Yzg4NjNmZjQ4MzFhYWEyODQxOThmMWEyMzk4ODkwYzc2NWUwYThkZTE4ZGE4YyJ9fX0="
```
