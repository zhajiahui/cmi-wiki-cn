---
title: 命令
source_url: https://wiki.mythiccraft.io/mythicmobs/drops/DropTypes/Command
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 命令

# Command {#command}

## 说明 {#description}

掉落时，控制台只会执行一次命令，与指定的数量无关。可以分别使用施法者作用域和触发者作用域的占位符，获取掉落此命令的生物以及击杀它的实体的信息。若要获取原始数量，则可以使用 `<drop.amount>` [占位符](../../skills/placeholders.md#misc-placeholders)。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| command | cmd | 要执行的命令 |  |
| ascaster | caster, ac, sudo, asmob | 是否以掉落物所属生物的身份执行命令，而不是控制台 | false |
| astrigger | trigger, at | 是否以掉落触发者的身份执行命令，而不是控制台 | false |
| asop | op, operator | 是否以完整权限执行命令 | false |

## 示例 {#examples}

```yaml
  Drops:
  - command{cmd="say Hello World! I was dropped <drop.amount> times!"} 1-10 1
```

## 别名 {#aliases}

- cmd
