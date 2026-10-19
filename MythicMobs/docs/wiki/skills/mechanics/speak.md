---
title: Speak
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/speak
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Speak {#speak}

## 说明 {#description}

让施法者使用聊天和对话气泡说话。支持全息图。你可以使用 `\n` 在全息图中强制添加一条新线

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| offset | o, yo, yoffset | 全息图的 y 偏移量。 | 1 |
| radius | r | 能看到聊天消息的实体范围半径 | 12 |
| maxlinelength | ll, mll, ml, linelength | 全息图的最大长度 | 22 |
| lineprefix | lp | 全息图的前缀。 | &f |
| message | m, msg | 要显示的消息，同时影响全息图和聊天栏 |  |
| chatprefix | cp | 聊天消息的前缀 | <caster.name>&f<&co> |
| duration | d, ticks, time, t | 全息图显示的持续时间。 | MESSAGE LENGTH * 4 |
| sendchatmessage | chatmessage, chat | 消息是否显示在聊天栏中 | true |
| audience |  | 机制的[接收对象（Audience）](../audience.md) | tracked |

> 该机制继承了[光环](aura.md)机制的所有属性
>

> > - `auraname` 属性**固定为** `#speaking`。
> > - `charges` 属性**固定为** `1`。
> > - `maxStacks` 属性**固定为** `1`。
> > - `mergeSameCaster` 属性**固定为** `false`。
> > - `overwriteCaster` 属性**固定为** `true`。
> > - `refreshDuration` 属性**固定为** `false`。

## 示例 {#examples}

```yaml
  Skills:
  - speak{
    offset=0.6f;
    radius=30;
    maxlinelength=22;
    lineprefix="&5";
    message=" I just spawned!";
    chatprefix=<caster.name>&f<&co>;
    duration=200} @self ~onSpawn
```

## 别名 {#aliases}

- speech
