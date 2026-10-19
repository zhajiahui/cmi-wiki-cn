---
title: Disguisetarget
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/disguisetarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Disguisetarget {#disguisetarget}

## 说明 {#description}

为目标生物应用伪装描述。需要安装 LibsDisguises 并开启伪装功能。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| disguise | d, type | 要应用到目标上的伪装。 | player Ashijin |
| audience |  | 伪装的[可见对象](../audience.md)。 |  |

## 示例 {#examples}

```yaml
Skills:
  - disguisetarget{d=SHEEP} @target
```

> 这个例子会导致目标变成一只羊。

##  {#section}

```yaml
Skills:
  - disguisetarget{d="player libraryaddict setCustomName '&7Jeb' setSkin Notch.png"} @target
```

> 这个将把它变成一个使用 Notch 皮肤的玩家，并给它显示名称 *Jeb*。颜色代码可在名牌字段中使用。
