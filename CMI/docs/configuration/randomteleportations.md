---
title: 随机传送（RandomTeleportations.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/RandomTeleportations.yml
---

# 随机传送（RandomTeleportations.yml）

文件：`plugins/CMI/Settings/RandomTeleportations.yml`

## `RandomTeleportation` { #randomteleportation }

```yaml title="RandomTeleportations.yml · RandomTeleportation（1/2）"
RandomTeleportation:
  # 再次使用命令前需要等待的时长
  Cooldown: 5
  # 最多尝试多少次，寻找有效传送位置
  # 建议保持较小值，因为玩家冷却结束后可以重试
  MaxTries: 20
  # 随机传送排除的生物群系
  ExcludedBiomes:
  - Ocean
  - Deep ocean
  - Deep cold ocean
  - Cold ocean
  - Deep lukewarm ocean
  - Lukewarm ocean
  - Warm ocean
  - River
  # 设为 true，为检测到的全部世界生成默认随机传送设置
  # 设为 false，不再自动生成世界设置，但仍可手动添加
  AutoGenerateWorlds: true
```

```yaml title="RandomTeleportations.yml · RandomTeleportation（2/2）"
RandomTeleportation:
  Worlds:
    # 使用此功能的世界名称。按相应世界名称添加条目，即可启用随机传送
    world:
      Enabled: true
      # 寻找有效位置的尝试次数，通常直接影响检查的区块数量
      # 设为 0，使用文件顶部的默认 MaxTries
      MaxTries: 0
      # 寻找有效位置的冷却时间，设为 0 使用文件顶部的默认 Cooldown
      Cooldown: 0
      Range:
        # 相对中心位置的最大坐标范围，例如 1000 表示中心两侧 -1000 到 1000 格
        # 例如 centerX 为 2000、centerZ 为 3000、MaxRange 为 1500，传送范围为 x:500;z:1500 到 x:3500;z:4500
        Max: 1000
        # 例如 maxcord 为 1000、mincord 为 500，范围为 -1000 到 -500，以及 1000 到 500 的坐标区间
        Min: 500
      Center:
        X: 0
        Z: 0
      # 随机传送区域的形状。地图为方形时保持 false
      Circle: false
      # 只尝试传送到最高方块，忽略洞穴位置
      # 例外是 Ignore.Leaves 为 true 时，会在树叶下方有空位时尝试将玩家放在叶下
      SurfaceOnly: false
      # 启用后，允许从其他世界随机传送到此世界
      FromAnotherWorld: true
      # 启用后，随机传送到此世界需要 cmi.randomteleport.world 权限
      RequireWorldPermission: false
      YLimits:
        # 寻找位置时的 Y 轴限制。若要减少传送到地下的情况，可设为 63
        # 较高限制可能增加寻找有效位置的时间
        Min: -64
        Max: 320
      Ignore:
        Water: true
        Lava: true
        Leaves: true
        PowderSnow: false
        # 启用后，不将玩家传送到会强制进入爬行状态的一格高空间
        CrawlSpaces: false
        # 随机传送时排除的地面材质
        Materials: []
        # 随机传送时排除的生物群系
        # 留空表示包含全部
        # 此项为空且 ExcludedBiomes 有设置时，使用 ExcludedBiomes
        Biomes: []
      # 随机传送时优先查找的生物群系
      # 填写生物群系名称后，忽略 Ignore.Biomes
      PreferredBiomes: []
    world_nether:
      Enabled: true
      MaxTries: 0
      Cooldown: 0
      Range:
        Max: 1000
        Min: 500
      Center:
        X: 0
        Z: 0
      Circle: false
      SurfaceOnly: false
      FromAnotherWorld: true
      RequireWorldPermission: false
      YLimits:
        Min: 0
        Max: 128
      Ignore:
        Water: true
        Lava: true
        Leaves: true
        PowderSnow: false
        CrawlSpaces: false
        Materials: []
        Biomes: []
      PreferredBiomes: []
    world_the_end:
      Enabled: true
      MaxTries: 0
      Cooldown: 0
      Range:
        Max: 1000
        Min: 500
      Center:
        X: 0
        Z: 0
      Circle: false
      SurfaceOnly: false
      FromAnotherWorld: true
      RequireWorldPermission: false
      YLimits:
        Min: 0
        Max: 256
      Ignore:
        Water: true
        Lava: true
        Leaves: true
        PowderSnow: false
        CrawlSpaces: false
        Materials: []
        Biomes: []
      PreferredBiomes: []
    rpgworld:
      Enabled: true
      MaxTries: 0
      Cooldown: 0
      Range:
        Max: 1000
        Min: 500
      Center:
        X: 0
        Z: 0
      Circle: false
      SurfaceOnly: false
      FromAnotherWorld: true
      RequireWorldPermission: false
      YLimits:
        Min: -64
        Max: 320
      Ignore:
        Water: true
        Lava: true
        Leaves: true
        PowderSnow: false
        CrawlSpaces: false
        Materials: []
        Biomes: []
      PreferredBiomes: []
```
