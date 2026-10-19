---
title: Setprojectilebulletmodel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setprojectilebulletmodel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setprojectilebulletmodel {#setprojectilebulletmodel}

## 说明 {#description}

设置当前弹射物子弹的CustomModelData。 （仅限DISPLAY子弹类型）

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| value | v, model, m | 要为投射物设置的模型 | 0 |

## 示例 {#examples}

此示例将弹射物子弹型号设置为 1234。

```yaml
  Skills:
  - setProjectileBulletModel{model=1234}
```
