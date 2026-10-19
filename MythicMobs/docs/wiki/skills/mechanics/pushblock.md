---
title: Push Block
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PushBlock
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Push Block {#push-block}

## 说明 {#description}

按活塞逻辑，将目标位置的方块向指定方向推动。方向可以是方位名称或位置目标选择器。指定位置目标时，只向该位置推动一次。此机制遵守活塞规则，也会推动相连的黏液块，但只处理与黏液块相邻或位于其前方的方块，无法带动被推方块后方相连的黏液块。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| direction | dir, d | 移动方向，也可以是目标选择器 | NORTH |
| onPush | then | 成功推动方块后执行的元技能 |  |
| onFail |  | 推动方块失败时执行的元技能 |  |

### Direction 属性 {#direction-attribute}

方向属性可以是 `named direction` 或 `targeter`

### 具名方向 {#named-direction}

可能的命名方向是

- `NORTH`
- `SOUTH`
- `EAST`
- `WEST`
- `UP`
- `DOWN` 你可以像下面这样使用它们

```yaml
  - pushblock{dir=UP} @SelfLocation{y=-0.1}
```

### 目标选择器 {#targeters}

你还可以使用目标选择器作为属性值，如下所示

```yaml
  - pushblock{dir=@Forward{f=1}} @SelfLocation{y=-0.1}
```

## 示例 {#examples}

```yaml
  Skills:
  - pushblock{dir=@Forward{f=1}} @ForwardWall{f=5;y=1;h=2;w=2}
```
