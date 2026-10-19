---
title: Setlevel
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setlevel
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setlevel {#setlevel}

## 说明 {#description}

导致施法生物改变其等级。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| action | a | 要执行的运算类型 | SET |
| level | l | 运算使用的数量 | 1 |

## Action 属性 {#action-attribute}

可用的操作有

- `SET`
- `ADD`
- `SUBTRACT`
- `MULTIPLY`
- `DIVIDE`

## 示例 {#examples}

当它生成时，这会将生物等级设置为3

```yaml
    - setlevel{a=set;l=3} @self ~onSpawn
```

##  {#section}

每次杀死玩家时，怪物等级都会增加 1

```yaml
    - setlevel{a=add;l=1} ~onKillPlayer
```

##  {#section-2}

生物生成时，将等级设为 1 到 5 的随机值，再加上 testlevel 记分板中假玩家 `__GLOBAL__` 的分数。

```yaml
    - setlevel{a=set;l="<random.1to5> + <global.score.testlevel>"} @self ~onSpawn
```

> 非字符串属性内的 [占位符](../placeholders.md) 和 [数学运算](../math.md) 的用法是 [**仅限高级版**](../../premium-features.md)

## 别名 {#aliases}

- modifylevel
