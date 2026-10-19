---
title: Block Unmask
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/BlockUnmask
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Block Unmask {#block-unmask}

## 说明 {#description}

blockunmask 效果用于撤销 blockmask 效果造成的方块伪装。例如，可以在生物死亡后，对较大半径范围使用此效果，清除之前发送的虚假方块更新。不过，这并非必需：当某个区块为玩家重新加载时，blockmask 创建的方块伪装就会恢复，但仅对该玩家恢复。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| radius | r | 取消方块伪装效果的半径。 | 0 |
| shape | s | 效果的形状，`Sphere`/`Cube`。 | SPHERE |

## 示例 {#examples}

将强制反转指定半径内由块遮罩效果创建的所有效果。

```yaml
  Skills:
  - effect:blockunmask{r=30}
```

## 别名 {#aliases}

- effect:blockUnmask
- e:blockunmask
