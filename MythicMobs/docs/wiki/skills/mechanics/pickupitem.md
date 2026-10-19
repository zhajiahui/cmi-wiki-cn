---
title: Pickupitem
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/pickupitem
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Pickupitem {#pickupitem}

## 说明 {#description}

如果施法者是玩家，则拾起目标物品。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| fakelooting | fl | 是否播放假的拾取动画。 | true |
| onpickup | pickup, then | 拾取物品后执行的[元技能]。 |  |

### OnPickup 属性 {#onpickup-attribute}

被调用的 Metaskill 的一些链接数据将被覆盖/设置为以下内容

| 数据 | 值 |
| --- | --- |
| Location | 被拾取物品的位置。 |
| Origin | 被拾取物品的位置。 |
| Item | 被拾取的物品。 |

## 示例 {#examples}

```yaml
  Skills:
  - pickupitem @ItemsInRadius{r=10}
```
