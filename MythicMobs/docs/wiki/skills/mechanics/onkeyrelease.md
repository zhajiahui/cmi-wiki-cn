---
title: On Key Release
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/OnKeyRelease
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Key Release {#on-key-release}

## 说明 {#description}

将光环应用于目标实体，当玩家释放特定键时触发技能。

按键通过 [AriKeys](https://www.spigotmc.org/resources/arikeys.97150/) 的按键 ID 指定，因此必须安装 AriKeys。光环生效期间，玩家松开绑定按键时执行 `onRelease` 技能。

> 此机制需要安装 [AriKeys](https://www.spigotmc.org/resources/arikeys.97150/) 插件。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onRelease | or | 松开按键时触发的技能。 |  |
| key | k | 触发技能的按键 ID。 |  |

> 该机制继承了[光环](aura.md)机制的所有*可继承*属性

## 示例 {#examples}

施加持续 10 秒的光环，期间玩家松开绑定按键时施放 `ChargeRelease` 技能。

```yaml
  Skills:
  - onKeyRelease{key=keybind.charge;onRelease=ChargeRelease;duration=200} @trigger
```

## 别名 {#aliases}

- keyRelease
- kr
