---
title: Randommessage
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/randommessage
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Randommessage {#randommessage}

## 说明 {#description}

向目标玩家发送随机消息。如果目标不是玩家，则不执行任何操作。可以将多少消息添加到列表中没有限制。特殊字符#会导致该技能失败。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| messages | m, message, msg, msgs | 发送给玩家的消息字符串列表，用逗号分隔。每个字符串都必须加引号，并且可以使用变量。 |  |

## 示例 {#examples}

与施法者交互时，向 20 格内的每个玩家发送一条随机消息。

```yaml
  Skills:
  - randommessage{
      m=
      "message 1",
      "message 2",
      "message 3";
      } @PIR{r=20} ~onInteract
```

##  {#section}

这将执行与上面相同的操作，但这次向每个玩家发送 2 随机消息

```yaml
  Skills:
  - randommessage{m="one test","not a test","test";repeat=1} @PIR{r=20} ~onInteract
```

## 别名 {#aliases}

- randommsg
- rm
- rmsg
