---
title: Remount
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/remount
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Remount {#remount}

## 说明 {#description}

让施法生物重新骑上生成时所骑乘的生物。

如果骑手的坐骑已消失或被杀死，此动作将不起作用。

## 属性 {#attributes}

> *此技能机制没有属性。*

## 示例 {#examples}

本例的 Mythic 生物名为 Rider，骑乘一匹马。Rider 受伤时下马，右键交互时重新上马。

```yaml
Rider:
  Type: skeleton
  Display: 'Rider'
  Health: 12
  Mount: TestHorse
  Skills:
  - dismount ~onDamaged
  - remount ~onInteract
TestHorse:
  Type: horse
  Display: 'Test Horse'
  Health: 20
```
