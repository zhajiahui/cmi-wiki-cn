---
title: 收集悬赏头颅
source: https://docs.phoenixdevt.fr/bounty-hunters/features/head-hunting
source_snapshot: '2026-10-19'
---

# 收集悬赏头颅 {#💀-head-hunting}

启用 *Head Hunting* 功能后，赏金猎人需要收集悬赏目标的头颅，才能领取赏金。猎人要手持头颅，右键点击发布悬赏的玩家。完成后即可领取悬赏，奖励会发给猎人。

```yml
# When enabled, players have to bring the target's head back to the
# bounty creator and right click it in order to claim the bounty.
# Make sure you both disable 'drop-head.killer' and 'drop-head.creator'
# Reload your server when changing this option.
head-hunting:
  enabled: false
```

确保在使用猎头时启用[头部掉落](head-hunting.md#head-drops)，以便猎人在杀死目标时能够真正获得目标的头部。

我们还建议关闭以下选项以避免悬赏堆叠。关闭时，两个不同的玩家将悬赏放在同一目标上将导致两个不同的悬赏，而不是一个较大的悬赏。

```yml
# When disabled, using /bounty will NOT increase the player's
# current bounty but will rather create one new bounty with the
# very same target.
bounty-stacking: true
```

如果关闭此选项，则会掉落两个头，猎人必须将两个头带到各自的悬赏创造者处，才能获得两个悬赏，就好像它是两个不同的悬赏一样。由你决定是否启用此选项！

## 头滴 {#head-drops}

当领取悬赏时，悬赏目标的头部可能会掉落。你可以在主配置文件中配置此功能。你还可以选择在认领悬赏时有机会掉落玩家头。

```yml
# Drops the player head when claiming a bounty or give the head to
# the bounty creator. Make sure you disable the 'drop-head.killer'
# option when toggling on.
drop-head:

  # Drops the head on the ground.
  killer:
    enabled: false
    chance: 100

  # Give the head to the bounty creator or save it in the bounty head
  # GUI that can be opened using /redeembountyheads. This option can also
  # be used with Head Hunting to give the head to the right clicked player.
  creator:
    enabled: false
    chance: 100
```

请注意，那里有两个不同的选项。第一个是每当悬赏目标被杀死时，使一个头掉在地板上。

*creator* 选项可用于**将玩家头赋予悬赏创建者**。如果悬赏的创建者离线，或者如果他的物品栏在悬赏被认领时已满，则该头将被保存，并且可以随时使用 */redeembountyheads* 免费兑换。如果他有一个空闲插槽，他将立即在他的物品栏中收到玩家头。

---

原文：[💀 Head Hunting](https://docs.phoenixdevt.fr/bounty-hunters/features/head-hunting) · 原文归档：2026-10-19
