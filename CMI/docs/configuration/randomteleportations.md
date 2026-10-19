---
title: 随机传送（RandomTeleportations.yml）
source_kind: configuration-comments
translation_review: reviewed
source_file: Settings/RandomTeleportations.yml
---

# 随机传送（RandomTeleportations.yml）

文件：`plugins/CMI/Settings/RandomTeleportations.yml`

来源：用户提供的配置文件；本文仅收录原注释的中文翻译。

## `RandomTeleportation`

### `RandomTeleportation.Cooldown`

再次使用命令前需要等待的时长

### `RandomTeleportation.MaxTries`

最多尝试多少次，寻找有效传送位置<br>
建议保持较小值，因为玩家冷却结束后可以重试

### `RandomTeleportation.ExcludedBiomes`

随机传送排除的生物群系

### `RandomTeleportation.AutoGenerateWorlds`

设为 true，为检测到的全部世界生成默认随机传送设置<br>
设为 false，不再自动生成世界设置，但仍可手动添加

### `RandomTeleportation.Worlds.world`

使用此功能的世界名称。按相应世界名称添加条目，即可启用随机传送

### `RandomTeleportation.Worlds.world.MaxTries`

寻找有效位置的尝试次数，通常直接影响检查的区块数量<br>
设为 0，使用文件顶部的默认 MaxTries

### `RandomTeleportation.Worlds.world.Cooldown`

寻找有效位置的冷却时间，设为 0 使用文件顶部的默认 Cooldown

### `RandomTeleportation.Worlds.world.Range.Max`

相对中心位置的最大坐标范围，例如 1000 表示中心两侧 -1000 到 1000 格<br>
例如 centerX 为 2000、centerZ 为 3000、MaxRange 为 1500，传送范围为 x:500;z:1500 到 x:3500;z:4500

### `RandomTeleportation.Worlds.world.Range.Min`

例如 maxcord 为 1000、mincord 为 500，范围为 -1000 到 -500，以及 1000 到 500 的坐标区间

### `RandomTeleportation.Worlds.world.Circle`

随机传送区域的形状。地图为方形时保持 false

### `RandomTeleportation.Worlds.world.SurfaceOnly`

只尝试传送到最高方块，忽略洞穴位置<br>
例外是 Ignore.Leaves 为 true 时，会在树叶下方有空位时尝试将玩家放在叶下

### `RandomTeleportation.Worlds.world.FromAnotherWorld`

启用后，允许从其他世界随机传送到此世界

### `RandomTeleportation.Worlds.world.RequireWorldPermission`

启用后，随机传送到此世界需要 cmi.randomteleport.world 权限

### `RandomTeleportation.Worlds.world.YLimits.Min`

寻找位置时的 Y 轴限制。若要减少传送到地下的情况，可设为 63<br>
较高限制可能增加寻找有效位置的时间

### `RandomTeleportation.Worlds.world.Ignore.CrawlSpaces`

启用后，不将玩家传送到会强制进入爬行状态的一格高空间

### `RandomTeleportation.Worlds.world.Ignore.Materials`

随机传送时排除的地面材质

### `RandomTeleportation.Worlds.world.Ignore.Biomes`

随机传送时排除的生物群系<br>
留空表示包含全部<br>
此项为空且 ExcludedBiomes 有设置时，使用 ExcludedBiomes

### `RandomTeleportation.Worlds.world.PreferredBiomes`

随机传送时优先查找的生物群系<br>
填写生物群系名称后，忽略 Ignore.Biomes
