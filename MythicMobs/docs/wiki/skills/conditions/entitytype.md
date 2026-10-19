---
title: Entitytype
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/conditions/entitytype
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Entitytype {#entitytype}

## 说明 {#description}

测试目标的实体类型是否是指定的类型。   有效实体类型的列表可以在 [Spigot Javadocs](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html) 上找到。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| type | types, t | 要匹配的实体类型列表。 |  |

## 各类型的限制 {#per-type-constraints}

`type`列表中的每个条目都可以携带一个嵌套块，使用形式`type=TYPE{option=value;option=value}`进一步限制对具有特定特征的实体的匹配。   仅当其块中的每个选项都匹配时，该类型的实体才匹配，并且如果实体的值等于为其列出的任何值，则选项匹配。值不区分大小写，破折号和空格被视为下划线。约束选项仅适用于公开匹配特征的实体。所有其他实体类型都会忽略该选项并使约束失败。

| 选项 | 别名 | 适用对象 | 说明 |
| --- | --- | --- | --- |
| variant | v | 青蛙、美西螈、猫、兔子、狐狸、村民、哞菇、牛、鸡、猪、狼、僵尸鹦鹉螺（1.21.11+）、铜傀儡（1.21.9+）。 | 要匹配的变种。对于铜傀儡，此项表示氧化状态。 |
| color | c | 马、绵羊、潜影贝、鹦鹉、羊驼、行商羊驼。 | 要匹配的颜色。名为 `jeb_` 的绵羊匹配 `RAINBOW`。 |
| style | s | Horse | 要匹配的马匹斑纹样式。 |
| mainGene | maingene, main, mg | Panda | 要匹配的熊猫主基因。 |
| hiddenGene | hiddengene, hidden, hg | Panda | 要匹配的熊猫隐藏基因。 |
| biome | b | 村民、僵尸村民。 | 要匹配的村民生物群系类型。 |
| profession | prof, proffesion | 村民、僵尸村民。 | 要匹配的村民职业。 |
| crack | cracks, crackedness, crackiness | 铁傀儡。 | 根据生命值确定的裂纹程度：`NONE`、`LOW`、`MEDIUM`、`HIGH`。 |
| bodyColor | bodycolor, body, bc | 热带鱼。 | 要匹配的身体颜色。 |
| patternColor | patterncolor, pc | 热带鱼。 | 要匹配的图案颜色。 |
| pattern | p | 热带鱼。 | 要匹配的热带鱼图案。 |

```yaml
TargetConditions:
- entityType{type=HORSE{color=WHITE;style=WHITE_DOTS}} true
```

```yaml
TargetConditions:
- entityType{type=CAT{variant=TABBY}} true
```

```yaml
TargetConditions:
- entityType{type=TROPICAL_FISH{bodyColor=WHITE;patternColor=RED;pattern=FLOPPER}} true
```

## 示例 {#examples}

```yaml
Conditions:
- entitytype{t=ZOMBIE} true
```

```yaml
TargetConditions:
- entitytype{t=WITCH} true
```

```yaml
TriggerConditions:
- entitytype{t=PLAYER} true
```

## 别名 {#aliases}

- mobtype
