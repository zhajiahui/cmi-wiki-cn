---
title: 技能命令
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Skill-Commands
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 技能命令

通过技能命令，可以将使用此功能的元技能注册为可执行的命令

> **此功能需要 [MythicMobs Premium](../premium-features.md) 或 [MythicRPG](https://mythiccraft.io/index.php?resources/mythicrpg-spells-classes-professions-more.129/)！**

例如，以下元技能

```yaml
MyExampleSkills:
  Command:
    Id: skillTest
    Aliases:
    - testSkill
    Completions:
      example:
      - players
  Skills:
  - message{m=<skill.var.example> our hero!} @self
```

会注册 `/skilltest` 命令。执行 `/skilltest Seyarada` 后，施法者会看到消息 `Seyarada our hero!`

以这种方式使用时，元技能始终以命令执行者作为继承目标

# 技能命令选项 {#skill-commands-options}

`Command` 字段会将所在元技能注册为命令，并启用所有相关选项

## Id {#id}

将注册的命令的名称

## 别名 {#aliases}

可用于作为命令触发相关元技能的其他有效名称。例如，在上面的示例中，使用 `/skilltest` 或 `/testskill` 将产生相同的结果

## 自动补全 {#completions}

命令中可通过 Tab 补全的参数。以键值对形式设置：键是用于存储输入参数的技能作用域变量名称；值是有效输入值的列表，在输入对应参数时用于 Tab 补全。还可以使用特定关键字，系统会将其自动替换为实际列表，使补全值随所用关键字动态变化

> 超出补全参数部分的额外参数会存入技能作用域变量 `excessArgs`
> <skill.var.excessArgs>

### 自动补全关键字 {#completions-keywords}

| 关键字 | 说明 |
| --- | --- |
| worlds | 服务器中的每个世界 |
| players | 服务器中的每名玩家 |
| items | 每种原版物品 |
| mythicitems | 每个已注册的 Mythic 物品 |

```yaml
    Completions:
      target:
      - players
```

# 示例 {#examples}

```yaml
RandomTP:
  Command:
    Id: randomtp
    Aliases:
    - rtp
    - wild
    Completions:
      target:
      - players
  Conditions:
  - hasPermission{p=rtp.use} true "&cYou do not have permission to use that command"
  - holding{m=DIAMOND} true "&cYou can only use this command while holding a diamond"
  Skills:
  - consumeHeldItem # Take away the diamond as payment
  - potion{t=SLOW_FALLING;l=5;d=100;p=false} @self
  - command{c=teleport <skill.var.target> <random.-999to999> 100 <random.-999to999>}
  FailedConditionsSkills:
  - e:p{p=VILLAGER_ANGRY;hs=1;vs=1;a=100} @self
  - s{s=entity.villager.no} @self
```
