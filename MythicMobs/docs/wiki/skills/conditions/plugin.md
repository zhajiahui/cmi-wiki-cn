---
title: Plugin
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/plugin
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Plugin {#plugin}

## 说明 {#description}

检查指定的插件是否在服务器上运行

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| plugin | pl, p | 要检查的插件。 | MythicMobs |

## 示例 {#examples}

```yml
  Conditions:
  - plugin{p=ThePluginName} true
```

## 别名 {#aliases}

- pluginexists
- hasplugin
