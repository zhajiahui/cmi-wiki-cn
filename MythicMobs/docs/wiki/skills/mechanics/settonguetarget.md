---
title: Settonguetarget
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/settonguetarget
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Settonguetarget {#settonguetarget}

## 说明 {#description}

将青蛙施法者的舌头目标设置为目标实体。

## 属性 {#attributes}

> *该技能机制没有属性*

## 示例 {#examples}

右键单击时将青蛙的舌头目标设置为最近的实体。

```yaml
MyLovingFrog:
  Type: FROG
  Skills:
  - setTongueTarget @EIR{r=5;limit=1;sort=NEAREST} ~onInteract
```

## 别名 {#aliases}

- tonguetarget
