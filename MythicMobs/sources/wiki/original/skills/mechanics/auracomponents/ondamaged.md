# On Damaged

## Description {#description}

Applies an aura component to the target that triggers a skill when they take
damage.

| [Implemented Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders#variable-placeholders) |
| --- |
| `<skill.var.damage-amount>` |
| `<skill.var.damage-type>` |
| `<skill.var.damage-cause>` |

## Attributes {#attributes}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| onHit | ondamagedskill, ondamaged, od, onhitskill, oh | [Metaskill] to execute if the target is damaged |  |
| cancelEvent | cE, canceldamage | Whether or not to cancel the event that triggered the aura | false |
| conditions | cond, c | If `cancelEvent` is enabled, the hit is only cancelled when these conditions pass. They are checked against the caster of the aura and do not change whether the `onHit` skill runs or a charge is used |  |
| damageSub | sub, s | An optional static decrease (or increase if negative) to the original hit's damage | 0 |
| damageMultiplier | multiplier, m | An optional multiplier on the original hit's damage | 1 |
| damagemodifiers | damagemods, damagemod | Allows the aura to apply damage modifiers. Also accepts a list, as shown in the example. Placeholders can be used as the modifier's amount (**Premium only**). |  |
| deflectProjectiles | deflect, reflect | Whether projectiles should be deflected | false |
| deflectconditions | dconditions | If `deflectProjectiles` is enabled, it will have to follow the specified set of conditions to work |  |
| modDamageType | damagetype | The [type](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/entity/EntityDamageEvent.DamageCause.html) of the damage that must be received in order to trigger the onHit metaskill |  |

<svg aria-hidden="true" class="wiki-alert__icon" viewbox="0 0 24 24"><circle cx="12" cy="12" r="9"></circle><path d="M12 11v5"></path><path d="M12 8h.01"></path></svg>Note

The aura only consumes a charge and applies `cancelEvent`, `damageSub`, `damageMultiplier` or `damageModifiers` **if the `onHit` skill executed successfully**: its chance roll succeeds, it is not on cooldown and all of its conditions pass. If the skill fails, the damage event is left untouched and no charge is consumed. If no `onHit` skill is configured, the execution always counts as successful.

Additionally, `cancelEvent` takes precedence over the damage-modifying attributes: if `cancelEvent` is `true`, the hit is cancelled and `damageSub`, `damageMultiplier` and `damageModifiers` are ignored. When `conditions` are set and fail, the hit is not cancelled and those attributes apply instead.

## Examples {#examples}

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

Every hit plays the sound and uses one of the 5 charges. Hits of 6 damage or less are cancelled, stronger hits deal half damage.

```yaml
  Skills:
  - aura{auraName=barrier;d=600;charges=5;components=[
    - onDamaged{cancelEvent=true;damageMultiplier=0.5;
      conditions=[ - compareValues{v1="<skill.var.damage-amount>";op=LTE;v2=6} true ];
      onHit=[ - sound{s=item.shield.block} @self ]}
    ]} @self
```

## Aliases {#aliases}

- onDamage
