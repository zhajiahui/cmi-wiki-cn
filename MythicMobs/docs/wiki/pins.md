---
title: 标记点
source_url: https://wiki.mythiccraft.io/mythicmobs/Pins
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 标记点 {#pins}

每个 [pack](packs.md) 现在都允许一个 `pins.yml` 文件。该文件可以包含 mm 以特殊方式处理的位置列表：它们将被视为“pin”，使它们能够更轻松地定位或检查。

## 命令 {#commands}

| 命令 | 权限 | 说明 |
| --- | --- | --- |
| `/mm pins create [pack] [name]` | mythicmobs.command.pins | 将当前位置保存为 `[pack]` 包中名为 `[name]` 的定位点。 |
| `/mm pins list` | mythicmobs.command.pins.list | 列出所有有效的定位点。 |
| `/mm pins move [name]` | mythicmobs.command.pins | 将名为 `[name]` 的定位点移至当前位置。 |
| `/mm pins remove [pack] [name]` | mythicmobs.command.pins | 从 `[pack]` 包中移除名为 `[name]` 的定位点。 |
| `/mm pins toggleviewing` | mythicmobs.command.pins | 通过文本展示实体显示每个定位点的位置。 |
| `/mm pins wand [pack] [pinName]` | mythicmobs.command.pins | 手持定位点魔杖时，左键会创建多点定位标记并为其添加点；右键会移除多点定位标记中最近添加的点。 |

## 技能机制 {#mechanics}

- [MovePin](skills/mechanics/movepin.md)

## 目标选择器 {#targeters}

- [@Pin](skills/targeters/pin.md)
- [@BlocksInPinRegion](skills/targeters/blocksinpinregion.md)

## 条件 {#conditions}

- [DistanceFromPin](skills/conditions/distancefrompin.md)
- [inPinRegion](skills/conditions/inpinregion.md)
- [OriginDistanceFromPin](skills/conditions/origindistancefrompin.md)
