---
title: Modifyprojectile
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/modifyprojectile
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Modifyprojectile {#modifyprojectile}

## 说明 {#description}

修改激活机制的弹射物、导弹或轨道。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| trait | t | 要修改的特性：`INERTIA`、`POWER`、`VELOCITY`、`RADIUS` 和 `YOFFSET`。 | `VELOCITY` |
| action | a | 修改弹射物特性时使用的操作：`ADD`、`SET`、`MULTIPLY`。 | `MULTIPLY` |
| value | v | 修改时使用的数值。 | 0 |

### Trait 属性 {#trait-attribute}

可能的值为：

- `INERTIA` - [导弹](missile.md) 的惯性。
- `POWER` - [弹射物](projectile.md)、[导弹](missile.md)、[轨道](orbital.md)的威力
- `VELOCITY` - [弹射物](projectile.md)、[导弹](missile.md)的威力
- `RADIUS`：[orbital](orbital.md) 的威力。
- `YOFFSET`：[orbital](orbital.md) 的高度。

## 示例 {#examples}

本例发射的弹射物会逐渐减速直到停止。将配置加入 skills.yml 后，即可用下方游戏内命令测试。

`/mm test cast TestingModifyProjectile`

```yaml
TestingModifyProjectile:
  Skills:
  - projectile{oT=TMP_oT;i=1;v=8;d=200;mr=100} @forward{f=100;y=0}
TMP_oT:
  Skills:
  - particles{particle=flame;a=2;hs=0;vs=0;s=0;y=0} @origin
  - modifyProjectile{trait=VELOCITY;action=MULTIPLY;value=0.95}
```
