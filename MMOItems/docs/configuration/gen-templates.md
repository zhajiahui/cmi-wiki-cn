---
title: gen-templates.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: gen-templates.yml
source_version: 6.10.1-SNAPSHOT
---

# gen-templates.yml

文件：`gen-templates.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `basic-template` { #basic-template }

```yaml title="gen-templates.yml · basic-template"
basic-template:

    # 此模板可以替换的材质列表。
    replace: [STONE]
    
    # 区块被选中进行世界生成的概率。
    # (0.7 = 70% 概率)
    chunk-chance: 0.7
    
    # 生成的深度范围。此示例
    # 允许方块在 Y 坐标 10 到 24 之间生成
    depth: 10=24
    
    # 每条矿脉生成的方块数量。
    # (注意：这是最大值，也可能生成更小的矿脉)
    vein-size: 5
    
    # 每个区块生成的矿脉数量。
    vein-count: 2
```

## `slime-chunks-only` { #slime-chunks-only }

```yaml title="gen-templates.yml · slime-chunks-only"
slime-chunks-only:
    replace: [STONE]
    
    # 使用此选项，仅在史莱姆区块中启用此模板
    slime-chunk: true
    
    chunk-chance: 0.6
    depth: 0=100
    vein-size: 1
    vein-count: 4
```

## `moutain-template` { #moutain-template }

```yaml title="gen-templates.yml · moutain-template"
# 'biome' 选项的使用示例
moutain-template:
    replace: [EMERALD_ORE]
    chunk-chance: 0.7
    depth: 10=100
    vein-size: 6
    vein-count: 2
    
    # 在山地生物群系中生成
    # 如果使用 '!mountains'，方块将在山地生物群系以外的所有地方生成。
    # 不使用 ! -> 生物群系白名单
    # 使用 ! -> 生物群系黑名单
    biomes:
    - moutains
```

## `nether-template` { #nether-template }

```yaml title="gen-templates.yml · nether-template"
# 'world' 选项的使用示例
nether-template:
    replace: [NETHER_QUARTZ_ORE]
    chunk-chance: 0.7
    depth: 10=100
    vein-size: 6
    vein-count: 2
    
    # 在此填写世界列表。世界列表同样可以
    # 通过 ! 使用白名单或黑名单
    worlds:
    - world_nether
```
