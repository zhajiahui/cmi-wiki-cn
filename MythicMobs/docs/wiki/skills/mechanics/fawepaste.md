---
title: Fawepaste
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/fawepaste
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Fawepaste {#fawepaste}

## 说明 {#description}

使用 [FAWE](https://www.spigotmc.org/resources/fast-async-worldedit.13932/) 插件粘贴结构文件。

在 MythicMob 目录中创建 `Schematics` 文件夹，放入要使用的结构文件。如果 mm 的 `Schematics` 目录中找不到指定文件，还会检查 FAWE 和 WE 的目录。

> **这是[仅限高级版](../../premium-features.md) 机制！**

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| schematic | s | 要加载的结构模板。 |  |
| pasteID | pid, id | 粘贴操作的 ID，可通过 [undoPaste](undopaste.md) 机制撤销这次粘贴。 |  |
| pasteAir | air, a | 是否粘贴空气？ | false |
| xOffset | x, xo | 粘贴结构模板时相对于目标的 X 轴偏移。 | 0 |
| yOffset | y, yo | 粘贴结构模板时相对于目标的 Y 轴偏移。 | 0 |
| zOffset | z, zo | 粘贴结构模板时相对于目标的 Z 轴偏移。 | 0 |
| rotation | rot, r | 粘贴结构模板时的旋转角度，单位为度。 | 0 |
| center | c | 是否将结构模板居中。 | true |
| chestDropTable | chests,cdt | 使用哪些 MythicMob 掉落表填充结构模板中的箱子。 |  |
| trapchestDropTable | trapchests, tcdt | 使用哪些 MythicMob 掉落表填充结构模板中的陷阱箱。 |  |
| blocksPerTick | bpt | 每刻放置的方块数量。为 0 时，所有方块都会在同一刻内粘贴。 | 0 |
| duration | d | 大于 0 时，在经过指定刻数后撤销粘贴操作。 | 0 |

## 示例 {#examples}

```yaml
  Skills:
  - fawePaste{schematic=deserttempleiron.schem;y=6;air=true;chestDropTable=IronDropTable} @origin
```

## 别名 {#aliases}

- pasteSchematic
- schematicPaste
- wePaste
