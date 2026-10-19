---
title: Chunk Load
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/ChunkLoad
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Chunk Load {#chunk-load}

## 说明 {#description}

为目标实体添加光环组件，在光环持续期间强制加载持有者所在区块。

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.63.66-1.15 1.12-1.62A6 6 0 1 0 7.79 12.38c.45.46.93.98 1.12 1.62"></path></svg>Tip

这可以防止持有者在附近没有玩家时卸载（从而冻结），这对于在战斗人员死亡后必须保持活动状态的 Boss 非常有用

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 在持有者周围保持加载的区块半径，0 表示仅加载其所在区块，上限为服务器的模拟距离。 | 0 |
| lag | tps, tpsthreshold | 服务器过去 1 分钟的平均 TPS 降至此值或以下时，光环会终止并解除强制加载。 | 0 |

## 别名 {#aliases}

- keeploaded
- loadchunk
