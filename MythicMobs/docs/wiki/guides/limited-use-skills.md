---
title: 限制使用次数的技能
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Limited-Use-Skills
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 限制使用次数的技能

**难度：中级**

有时你可能希望技能只能使用固定次数，例如让僵尸最多发射 7 颗火球。本指南将实现这一效果！

我们将用变量记录技能已经使用的次数，一旦达到指定的总次数，技能就会停止生效。

# 特定用途 {#specific-uses}

这个示例会递增变量，但变量达到 7 后，技能就会停止生效。

```yaml
FireballSkill:
  Conditions:
  - variableequals{var=caster.fireballs;val=7} false
  Skills:
  - setvariable{var=caster.fireballs;val=<caster.var.fireballs|0>+1}
  - <Your skills mechanics go here>
```

在这个示例中，每次技能运行，都会向变量加上 "1"；如果变量完全不存在，则通过[变量回退值](../skills/variables.md#variable-fallback)将其设为 1，然后像平常一样运行机制。

技能设置了 [VariableEquals](../skills/conditions/variableequals.md) 条件，因此变量一旦达到 7，该条件就会阻止技能运行。

如果想重置计数器，只需使用 [VariableUnset](limited-use-skills.md) 机制。

```yaml
Skills:
- variableunset{var=caster.fireballs}
```
