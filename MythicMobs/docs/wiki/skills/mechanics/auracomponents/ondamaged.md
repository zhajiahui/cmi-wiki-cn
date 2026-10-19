---
title: On Damaged
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/OnDamaged
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# On Damaged {#on-damaged}

## 说明 {#description}

将光环组件应用于目标，当目标受到伤害时会触发技能。

| [已实现的占位符](../../placeholders.md#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| onHit | ondamagedskill, ondamaged, od, onhitskill, oh | 目标受伤时执行的[元技能]。 |  |
| cancelEvent | cE, canceldamage | 是否取消触发光环的事件。 | false |
| conditions | cond, c | 启用 `cancelEvent` 时，仅在这些条件通过后才取消命中。条件以光环施法者为检查对象，不影响 `onHit` 技能是否执行，也不影响是否消耗充能次数。 |  |
| damageSub | sub, s | 从原始命中伤害中减少的固定值，可选；负值则会增加伤害。 | 0 |
| damageMultiplier | multiplier, m | 对原始命中伤害应用的倍率，可选。 | 1 |
| damagemodifiers | damagemods, damagemod | 允许光环应用伤害修饰符。也接受列表，写法见示例。修饰符的数值可以使用占位符，**仅 Premium 版**支持。 |  |
| deflectProjectiles | deflect, reflect | 是否反弹弹射物。 | false |
| deflectconditions | dconditions | 启用 `deflectProjectiles` 后，必须满足指定的一组条件才会生效。 |  |
| modDamageType | damagetype | 触发 onHit 元技能所必须受到的伤害[类型](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html)。 |  |

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>Note

只有 **`onHit` 技能成功执行时**，此光环才消耗一次次数，并应用 `cancelEvent`、`damageSub`、`damageMultiplier` 或 `damageModifiers`。成功表示概率判定通过、未在冷却且全部条件满足。失败时保持伤害事件原样，不消耗次数。未配置 `onHit` 技能时始终视为成功。

此外，`cancelEvent`优先于修改伤害属性：如果`cancelEvent`是`true`，则命中被取消，`damageSub`、`damageMultiplier`和`damageModifiers`被忽略。当 `conditions` 设置并失败时，命中不会取消，而是应用这些属性。

## 示例 {#examples}

```yaml
  Skills:
  - aura{auraName=damageResist;d=200;components=[
    - onDamaged{
      onTick=[
        - particles{p=flame;amount=10;hS=0.4}
      ];
      damageMods="FIRE 0.5, MAGIC 0.3, CUSTOM <caster.var.customresistance>"} @self ~onInteract
    ]}
```

每次命中都会播放声音，并消耗 5 次可用次数中的一次。伤害不超过 6 的命中会被取消，更高伤害的命中则造成一半伤害。

```yaml
  Skills:
  - aura{auraName=barrier;d=600;charges=5;components=[
    - onDamaged{cancelEvent=true;damageMultiplier=0.5;
      conditions=[ - compareValues{v1="<skill.var.damage-amount>";op=LTE;v2=6} true ];
      onHit=[ - sound{s=item.shield.block} @self ]}
    ]} @self
```

## 别名 {#aliases}

- onDamage
