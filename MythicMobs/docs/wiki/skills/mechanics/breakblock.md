---
title: Breakblock
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/breakblock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Breakblock {#breakblock}

## 说明 {#description}

破坏目标位置的方块，也会掉落该方块的物品，基岩除外。必须设置 `forcesync=true`。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| doDrops | drops, d | 是否掉落方块。 | true |
| doEffect | effect, e | 是否播放方块破坏粒子。 | true |
| useTool | tool, t | 是否使用玩家手中的工具。 | true |

## 示例 {#examples}

此示例将在右键单击时打破当前世界中位置 x:100,y:64,z:100 处的方块。

```yaml
Skills:
  - breakblock{forcesync=true} @location{c=100,64,100} ~onInteract
```

##  {#section}

### 测试 {#tests}

> 这些测试是使用 /mm testcast TestingBreakBlock 运行的

```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=true} @origin
```

当玩家在手中没有工具的情况下调用此命令时，它不会掉落块或创建粒子效果。

##  {#section-2}

```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=false} @origin
```

玩家空手调用时，会掉落方块，但不产生粒子。将 doEffect 设为   false   时，这一描述同样成立（  true  ）。

##  {#section-3}

```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=false;doDrops=true;useTool=true} @origin
```

当玩家用手中的工具调用此函数时，它会掉落方块并且不会播放粒子效果。

##  {#section-4}

```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=false;useTool=true} @origin
```

当玩家用手中的工具调用此函数时，它不会掉落方块，也不会创建粒子效果。

##  {#section-5}

```yaml
TestingBreakBlock:
  Skills:
  - breakblock{forcesync=true;doEffect=true;doDrops=true;useTool=true} @origin
```

当玩家用手中的工具调用此函数时，它会掉落一个方块，并会创建粒子效果。

## 别名 {#aliases}

- blockBreak
