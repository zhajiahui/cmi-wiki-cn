---
title: Guardianbeam
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/guardianbeam
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Guardianbeam {#guardianbeam}

## 说明 {#description}

在原点与目标之间绘制守卫者光束。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| duration | d, maxduration, md | 效果生效的时间，单位为刻。 | 400 |
| interval | int, i | 效果的更新频率。 | 1 |
| startYOffset | syo | 光束起点的 y 轴偏移。 | 1 |
| targetYOffset | tyo | 光束目标端的 y 轴偏移。 | 0 |
| fromOrigin | fo | 是否让效果从 @origin 而不是 @self 开始。 | false |
| onstartskill | onstart, os | 效果开始时执行的元技能。 |  |
| ontickskill | ontick, ot | 每个更新间隔执行的元技能。 |  |
| onendskill | onend, oe | 效果结束时执行的元技能。 |  |

## 示例 {#examples}

```yaml
Guardian_Beam:
   Skills:
   - guardianbeam{d=200;i=1;syo=1;fromOrigin=false;oS=AStartingSkill;oT=ATickingSkill;oE=AEndingSkill} @Target
```

## 别名 {#aliases}

- effect:guardianbeam
- effect:beam
- e:guardianbeam
- e:beam
