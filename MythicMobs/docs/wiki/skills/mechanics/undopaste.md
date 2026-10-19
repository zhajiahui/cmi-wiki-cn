---
title: Undopaste
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics/undopaste
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Undopaste {#undopaste}

## 说明 {#description}

根据 ID 或结构文件，撤销之前通过 [fawePaste](fawepaste.md) 机制粘贴的内容。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| pasteID | pid, id | 要撤销的粘贴操作 ID |  |

> 该机制继承了[光环](aura.md)机制的所有*可继承*属性

## 示例 {#examples}

```yaml
ExampleMob:
  Skills:

  # With ID
  - fawePaste{s=cgym.schem;id=abc} @self ~onSpawn
  - undoPaste{id=abc} @self ~onDamaged

  # Without ID
  - fawePaste{s=lab.schem} @self ~onSpawn
  - undoPaste{id=lab.schem} @self ~onDamaged
```

## 别名 {#aliases}

- undoschem
- undoschematic
