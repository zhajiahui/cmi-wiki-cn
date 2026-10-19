---
title: Prison
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/prison
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Prison {#prison}

## 说明 {#description}

将目标实体围困在由方块组成的临时监狱内。创建的块将在指定的时间后自动消失。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| material | m, t, type | 构成囚笼的材质，即方块类型。 | ICE |
| duration | d | 囚笼的持续时间，单位为刻。 | 100 |
| breakable | b | (true/false) 囚笼方块是否可以被破坏。 | false |
| materialdata | md | 已弃用。旧版游戏中存在的材质数据。设置后，插件会尝试将材质转换为新版的对应材质。 | 0 |

## 示例 {#examples}

此技能在施法生物的目标周围创建铁块牢笼，持续 200 游戏刻（10 秒），牢笼可以被挖掘破坏。

```yaml
IronPrison:
  Skills:
  - prison{material=IRON_BLOCK;duration=200;breakable=true} @target
```
