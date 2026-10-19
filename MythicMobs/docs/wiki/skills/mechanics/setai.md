---
title: Setai
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setai
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Setai {#setai}

## 说明 {#description}

切换目标AI

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| ai | state, value | 设置生物的 AI 状态。`true` 为启用，`false` 为禁用 | false |

## 示例 {#examples}

此示例将关闭生物的人工智能5秒

```yaml
TemporaryAISwitcher:
  Skills:
  - setAI{ai=false} @self
  - delay 100
  - setAI{ai=true} @self
```

## 别名 {#aliases}

- ai
