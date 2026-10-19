---
title: Teleport
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleport
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Teleport {#teleport}

## 说明 {#description}

将施法者传送到目标位置/实体。传送的终点将位于一个区域内，该区域的大小取决于 `spreadh` 和 `spreadv` 属性。

技能会尽量在散布范围内寻找安全落点，通常避免将生物传送进方块。unsafe 属性允许传送到目标实体所在位置。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| spreadh | sh, r, radius | 落点的水平散布范围。 | 0 |
| spreadv | sv | 落点的垂直散布范围。 | 0 |
| preservepitch | pp | 是否沿用 pitch 值 | true |
| preserveyaw | py | 是否沿用 yaw 值 | true |
| unsafe | us | 不寻找安全传送位置（忽略 sH 和 sV） | false |

## 示例 {#examples}

此示例将生物传送到目标玩家的5块内，在同一垂直轴上。

```yaml
Warp:
  Skills:
  - teleport{spreadh=5;spreadv=0} @target
```

## 别名 {#aliases}

- tp
