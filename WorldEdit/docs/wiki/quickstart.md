---
title: 快速入门
source_url: https://worldedit.enginehub.org/en/latest/quickstart/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldEdit Documentation 7.4 (en/latest), snapshot b16b7f1e2fe9
---

# 快速入门 { #quick-start }

## 开始之前 { #first-things-first }

- 如果使用 Bukkit，你需要相应权限才能使用 WorldEdit。可以将自己设为 OP（`/op yourname`）来获得权限。Sponge 服务器同样需要设置权限，不过 Sponge 不通过 OP 授予全部权限。

- 如果使用 NeoForge/Fabric 进行单人游戏，只有世界开启了作弊，WorldEdit 才会启用。

- 如果使用 NeoForge/Fabric 服务器，只有 OP 能使用 WorldEdit。

!!! tip "提示"

    对于 NeoForge/Fabric，你可以：

    - 在 WorldEdit 的设置文件（参见[配置](config.md)）中开启“cheat-mode”，这样即使在生存模式中也能使用 WorldEdit（在服务器上则允许所有人使用）。

    - 或者开启“use-in-creative”，让自己在创造模式中使用 WorldEdit（在服务器上则允许处于创造模式的玩家使用）。

### 想显示选区边界线？ { #want-to-see-selection-lines }

要显示选区边界线，可以选择以下方式：

1. 通过 `//drawsel` 使用服务端提供的有限选区边界显示。它只支持不超过 48x48x48 的长方体选区，旧版上限为 32x32x32，而且必须处于创造模式。这些限制来自 Minecraft 长期以来的结构方块实现。

2. 使用第三方客户端模组，例如 [WorldEdit CUI（Fabric）](https://modrinth.com/mod/worldedit-cui)。此模组需要 Fabric，因此必须先安装 Fabric。

!!! note "注意"

    使用 Minecraft 1.12 或更早版本时，除了下载旧版 WorldEdit（版本 6），可能还需要 [Mumfrey 开发的旧版 WorldEditCUI](https://www.minecraftforum.net/forums/mapping-and-modding-java-edition/minecraft-mods/1292886-worldeditcui)。它需要的是 LiteLoader，安装步骤见对应页面。

无论以何种方式安装 WorldEdit（Bukkit 服务器、单人游戏等），选区线条模组都能使用。

## 快速移动 { #getting-around }

先来看看如何快速移动。

> 1. 看向一个距离不太远的方块，输入 `/jumpto`。
>
> 2. 站在树下，输入 `/ascend`。
>
> 3. 站在树顶时，输入 `/descend`。
>
> 4. 站在树干后面，直视前方，确认另一侧有空间，然后输入 `/thru`。

也可以拿出指南针（或输入 `//wand -n`），看向附近的方块并左键单击。想穿墙时，右键单击墙壁即可。

## 创建选区 { #making-selections }

长方体就像三维的矩形。在 WorldEdit 中，通过设置长方体的两个点来选定所需区域。

![../_images/cuboid.png](assets/d84ee71cb357-cuboid.png)

![../_images/cuboid-dark.png](assets/4bd5168c152f-cuboid-dark.png)

如何选择这两个点？你可以：

> - 手持木斧，用左键和右键单击方块（使用 `//wand` 获取木斧）。
>
> - 站在某个位置，输入 `//pos1` 和 `//pos2`。
>
> - 看向方块，输入 `//hpos1` 和 `//hpos2`。

**练习：**选出一个大约 15x15x15 的区域供测试，然后继续下一节。

## 操作选区 { #doing-things-with-the-selection }

> 1. 将整个选区设为基岩：`//set minecraft:bedrock`（`minecraft` 可以省略。如果在支持模组的平台上游玩，需要使用模组的命名空间来标识方块，例如 `//set ic2:stone`。）
>
> 2. 将整个选区设为石头：`//set 1`（这是 Minecraft 1.12 及更早版本使用的旧版 ID。如果已经熟悉这些 ID，仍然可以使用，但建议学习方块名称，使用名称也更方便——1.13+ 新增的方块没有这些 ID！）
>
> 3. 将选区设为 50% 砂岩和 50% 玻璃：`//set sandstone,glass`。
>
> 4. 将砂岩替换为泥土：`//replace sandstone dirt`。
>
> 5. 清空区域：`//set air`。
>
> 6. 生成一个有趣的形状：`//g 35 data=(32+15/2/pi*atan2(x,y))%16; (0.75-sqrt(x^2+y^2))^2+z^2<0.25^2`。
>
> 7. 面向一个正方向（不要朝向对角线），重复选区内容：`//stack 4`。

现在撤销这些更改！

> - 撤销 7 次：`//undo 7`。

## 调整选区 { #adjusting-the-selection }

已经选好了一个长方体，接下来调整它！

> 1. 向上扩展，让长方体增高 10 个方块：`//expand 10 up`。
>
> 2. 向面朝的方向扩展，让长方体增长 5 个方块：`//expand 5`。
>
> 3. 向下收缩，让长方体降低 10 个方块：`//contract 10 down`。

## 使用笔刷 { #playing-with-brushes }

> 1. 拿一把镐（或任意想用的物品），将它选为当前手持物品。
>
> 2. 启用半径为 5 的石头笔刷：`/br sphere stone 5`。
>
> 3. 瞄准离自己较远的地面，右键单击以放置大型石球。
>
> 4. 让笔刷只影响草方块：`/mask grass`。
>
> 5. 将放置的石头改为羊毛：`/material red_wool,green_wool`。
>
> 6. 继续右键单击其他区域。
>
> 7. 停用笔刷：`/brush none`。

## 继续学习…… { #continuing-on }

查看其余[文档](index.md)。
