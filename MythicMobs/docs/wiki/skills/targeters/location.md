---
title: Location
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Location
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Location {#location}

## 说明 {#description}

以世界中的指定坐标为目标

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| location | loc, l, c | 完整位置，格式为 `x,y,z,yaw,pitch`。 |  |
| x |  | 未设置 `location` 时，此项为目标位置的 x 坐标。 | 0 |
| y |  | 未设置 `location` 时，此项为目标位置的 y 坐标。 | 0 |
| z |  | 未设置 `location` 时，此项为目标位置的 z 坐标。 | 0 |
| yaw |  | 未设置 `location` 时，此项为目标位置的偏航角。 | 0 |
| pitch |  | 未设置 `location` 时，此项为目标位置的俯仰角。 | 0 |
| world | w | 要选择为目标的世界。未设置时，选择施法者所在世界。 |  |

## 示例 {#examples}

```yaml
ExampleSkill:
  Skills:
  - setblock{m=DIAMOND_BLOCK} @Location{location=100,70,-120,0,0}
  - setblock{m=EMERALD_BLOCK} @Location{x=100;y=71;z=-120}
```

## 别名 {#aliases}

- l
- loc
