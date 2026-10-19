---
title: modifiers/example_modifiers.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: modifiers/example_modifiers.yml
source_version: 6.10.1-SNAPSHOT
---

# modifiers/example_modifiers.yml

文件：`modifiers/example_modifiers.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `sharp` { #sharp }

```yaml title="modifiers/example_modifiers.yml · sharp"
sharp:
    chance: 0.3
    prefix: "&f锋利"
    stats:
        attack-damage: 3
        lore:
        - "&7更加锋利！"
```

## `group_example` { #group_example }

```yaml title="modifiers/example_modifiers.yml · group_example"
group_example:
    max: 3
    modifiers:
        sharp: 1
        fiery: 1
        lucky: 1
```

## `rare_group` { #rare_group }

```yaml title="modifiers/example_modifiers.yml · rare_group"
rare_group:
    min: 1
    max: 1
    modifiers:
        arcane: 1
        accuracy: 1
        ancient: 1
```

## `fiery` { #fiery }

```yaml title="modifiers/example_modifiers.yml · fiery"
fiery:
    chance: 0.1
    prefix:
        format: "&c炽热"
        priority: 1
    stats:
        ability:
            on-hit:
                type: burn
                mode: on_hit
```

## `lucky` { #lucky }

```yaml title="modifiers/example_modifiers.yml · lucky"
# 提高暴击几率的幸运修饰器
lucky:
    prefix: "&f幸运"
    stats:
        critical-strike-chance:
            base: 9
            spread: .1
            max-spread: .3
```

## `arcane` { #arcane }

```yaml title="modifiers/example_modifiers.yml · arcane"
# 提供更多魔力
arcane:
    suffix: "&f之奥术"
    stats:
        max-mana:
            base: 6
            scale: 1
            spread: .1
            max-spread: .3
```

## `ancient` { #ancient }

```yaml title="modifiers/example_modifiers.yml · ancient"
ancient:
    prefix: "&f远古"
    stats:
        magic-damage:
            base: 7
            scale: 3
            spread: .5
            max-spread: .9
```

## `accuracy` { #accuracy }

```yaml title="modifiers/example_modifiers.yml · accuracy"
accuracy:
    suffix: "之精准"
    stats:
        critical-strike-chance:
            base: 9
            spread: .1
            max-spread: .3
        weapon-damage:
            base: 12
            spread: .1
            max-spread: .3
```

## `swiftness` { #swiftness }

```yaml title="modifiers/example_modifiers.yml · swiftness"
swiftness:
    suffix: "之迅捷"
    stats:
        perm-effects:
            speed: 1
```

## `heavy` { #heavy }

```yaml title="modifiers/example_modifiers.yml · heavy"
# 使武器变为双手武器，但提高伤害和暴击伤害的修饰器
heavy:
    prefix: "&f沉重"
    stats:
        two-handed: true
        attack-damage:
            base: 3
            scale: 1
        critical-strike-power:
            base: 10
            scale: 2
```

## `blazing` { #blazing }

```yaml title="modifiers/example_modifiers.yml · blazing"
# 元素修饰器
blazing:
    prefix: "&f炽燃"
    stats:
        element:
            fire:
                damage:
                    base: 20
                    spread: .2
                    max-spread: .5
```

## `impending-doom` { #impending-doom }

```yaml title="modifiers/example_modifiers.yml · impending-doom"
# 爱你，泰拉瑞亚！
impending-doom:
    suffix: "&f之末日将临"
    stats:
        magic-damage:
            base: 7
            scale: 3
            spread: .5
            max-spread: .9
        ability:
            on-hit:
                type: life_ender
                mode: on-hit
                damage:
                    base: 5
                    scale: 2
                    spread: .3
                    max-spread: .5
```
