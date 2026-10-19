---
title: Skybox
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Skybox
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Skybox {#skybox}

## 说明 {#description}

更改目标玩家的天空盒。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| skybox | sky, s, type, t, environment, env, e | 向玩家显示的天空盒 | 0 |

### Skybox 属性 {#skybox-attribute}

| 值 | 说明 |
| --- | --- |
| 小于 1 的任意整数 | 取消修改后的天空盒 |
| 大于 0 的任意整数 | 雨天 |

## 示例 {#examples}

让 20 格内的每个玩家看到 rain（下雨）天空效果。

```yaml
  Skills:
  - skybox{s=1} @PIR{r=20}
```

## 别名 {#aliases}

- effect:skybox
- e:skybox
