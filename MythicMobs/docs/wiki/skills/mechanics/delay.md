---
title: Delay
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/delay
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Delay {#delay}

## 说明 {#description}

导致当前技能树延迟 X 个游戏刻。   游戏刻数可以按位置指定为 `delay 60`，或通过 `ticks` 属性指定为 `delay{ticks=60}`。两种形式都接受占位符，因此可以在运行时解析持续时间，例如`delay{ticks=<caster.var.x>}`。通过添加 `delay=TICKS` [通用属性](../mechanics.md#universal-attributes)，延迟也可以直接用作机制内部的属性。这样，延迟不会应用于整个技能树，而仅应用于单个机制。

技能延迟和属性延迟的工作方式不同。

> 这个机制也可以用来完成[Intratick Scheduling](../intratick-scheduling.md)

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ticks |  | 延迟执行的刻数，接受占位符。 | 0 |

## 示例 {#examples}

```yaml
Skills:
  - ignite{ticks=60}
  - delay 60
  - explode
```

`ticks`属性是表示为属性的相同延迟，其值可以是占位符。

```yaml
Skills:
  - ignite{ticks=60}
  - delay{ticks=<caster.var.x>}
  - explode
```

这是使用延迟通用属性的示例。它可以在任何技能机制内部工作，并将其延迟指定的游戏刻数。

```yaml
Skills:
  - skill{skill=exampleskill;delay=200}
  - explode{delay=80}
```
