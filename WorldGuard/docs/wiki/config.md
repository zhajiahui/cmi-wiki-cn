---
title: 配置
source_url: https://worldguard.enginehub.org/en/latest/config/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 配置 { #configuration }

WorldGuard 的许多功能都通过配置选项控制，如禁用药水、戴南瓜潜水等。本页列出所有可用的配置选项。

## 配置文件 { #configuration-files }

安装 WorldGuard 并运行过服务器后，可以在 **plugins/WorldGuard** 文件夹中找到主配置文件：

- `config.yml`

每个世界还各有自己的配置文件：

- `worlds/world/config.yml`

- `worlds/world_nether/config.yml`

- `worlds/mining_world/config.yml`

打开各世界的配置文件时，会发现其中几乎没有内容。需要覆盖某项设置时，将该设置复制到对应世界的配置文件中即可。

示例：为单个世界设置配置项

假设已在主配置文件中将 `block-creeper-block-damage` 设为 true：

```text
mobs:
    block-creeper-explosions: false
    block-creeper-block-damage: true
    block-wither-explosions: false
```

但希望在下界中将其设为 `false`。打开 `worlds/world_nether/config.yml`，将内容替换为：

```text
mobs:
    block-creeper-block-damage: false
```

只需复制相关配置行及其所有父级分类。

## 设置 { #settings }

!!! note "注意"

    这里列出的选项仅供参考。修改选项前，应先在 `config.yml` 中找到它，因为有些设置必须嵌套在其他配置项下面。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">op-permissions</td>
<td markdown="span">TRUE</td>
<td markdown="span">是否为 OP 玩家授予 WorldGuard 的全部权限，即使所用权限插件没有为 OP 提供这些权限。</td>
</tr>
<tr>
<td markdown="span">summary-on-start</td>
<td markdown="span">TRUE</td>
<td markdown="span">服务器启动时，显示各世界的 WorldGuard 设置摘要。输出内容较多，世界很多时应禁用此项。</td>
</tr>
<tr>
<td markdown="span">auto-invincible</td>
<td markdown="span">FALSE</td>
<td markdown="span">拥有 `worldguard.auto-invincible` 权限的玩家加入时，自动进入无敌模式。</td>
</tr>
<tr>
<td markdown="span">auto-invincible-group</td>
<td markdown="span">FALSE</td>
<td markdown="span">属于 `wg-invincible` 权限组的玩家加入时，自动进入无敌模式。</td>
</tr>
<tr>
<td markdown="span">auto-no-drowning-group</td>
<td markdown="span">FALSE</td>
<td markdown="span">属于 `wg-amphibious` 权限组的玩家加入时，自动获得水下呼吸。</td>
</tr>
<tr>
<td markdown="span">use-player-move-event</td>
<td markdown="span">TRUE</td>
<td markdown="span">是否允许 WorldGuard 多使用少量 CPU，以处理需要追踪玩家移动的功能。治疗、饱食度恢复、欢迎消息等部分[区域旗标](regions/flags.md)需要启用此项。</td>
</tr>
<tr>
<td markdown="span">use-player-teleports</td>
<td markdown="span">TRUE</td>
<td markdown="span">追踪玩家移动时，是否将传送事件也考虑在内。如果使用玩家移动事件及依赖它的旗标，应始终启用此项。</td>
</tr>
<tr>
<td markdown="span">use-particle-effects</td>
<td markdown="span">TRUE</td>
<td markdown="span">操作被取消时，WorldGuard 是否显示粒子效果。</td>
</tr>
<tr>
<td markdown="span">disable-permission-cache</td>
<td markdown="span">FALSE</td>
<td markdown="span">WorldGuard 会缓存某些权限检查，以改善较慢权限插件的性能。如果使用现代权限插件时遇到权限更新不及时的问题，可尝试将此项设为 `TRUE`。</td>
</tr>
<tr>
<td markdown="span">custom-metrics-charts</td>
<td markdown="span">TRUE</td>
<td markdown="span">向 [bStats](https://bstats.org/plugin/bukkit/WorldGuard/3283)报告一些额外统计数据。</td>
</tr>
<tr>
<td markdown="span">host-keys</td>
<td markdown="span"></td>
<td markdown="span">玩家连接服务器时必须使用的主机名列表，详见[主机密钥](host-keys.md)。</td>
</tr>
</tbody>
</table>

### security.* { #security }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">deop-everyone-on-join</td>
<td markdown="span">FALSE</td>
<td markdown="span">移除所有加入服务器的玩家的 OP 身份。</td>
</tr>
<tr>
<td markdown="span">block-in-game-op-command</td>
<td markdown="span">FALSE</td>
<td markdown="span">禁止在游戏内使用 /op 命令。</td>
</tr>
<tr>
<td markdown="span">host-keys-allow-forge-clients</td>
<td markdown="span">FALSE</td>
<td markdown="span">使用[主机密钥](host-keys.md)时，允许使用 Forge 的玩家加入。</td>
</tr>
</tbody>
</table>

### build-permission-nodes.* { #build-permission-nodes }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">通过为玩家授予相应权限来限制建造的功能，详见[建造权限](build-perms.md)。</td>
</tr>
<tr>
<td markdown="span">deny-message</td>
<td markdown="span">&eSorry, but you are not permitted to do that here.</td>
<td markdown="span">在建造权限检查拒绝操作时发送的消息。未设置消息时使用默认消息。</td>
</tr>
</tbody>
</table>

### event-handling.* { #event-handling }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-entity-spawns-with-untraceable-cause</td>
<td markdown="span">FALSE</td>
<td markdown="span">Bukkit 并不总会向插件提供实体生成的确切原因，因此玩家有可能绕过保护来生成实体，例如使用刷怪蛋。此选项会阻止无法确定真实原因的情况。由于原因不明的情况相当多，建议保持禁用。</td>
</tr>
<tr>
<td markdown="span">interaction-whitelist</td>
<td markdown="span">[]</td>
<td markdown="span">不应受到保护的方块类型列表。例如，将箱子加入列表后，[区域保护](regions/index.md)就不会保护箱子。此项主要用于服务器存在非原版功能（由其他插件或模组添加的游戏功能），而你不希望这些功能被阻止的情况。</td>
</tr>
<tr>
<td markdown="span">emit-block-use-at-feet</td>
<td markdown="span">[]</td>
<td markdown="span">使用这些物品时，还会要求玩家拥有*理论上*修改其脚下方块的权限。此项主要针对某些插件或模组物品：它们使用会影响世界的投射物，却不向 WorldGuard 检查权限。不过，这并非完善的解决方案，因为玩家仍可站在自己有权限的位置，向想影响的区域*内部*发射投射物。</td>
</tr>
<tr>
<td markdown="span">ignore-hopper-item-move-events</td>
<td markdown="span">FALSE</td>
<td markdown="span">禁用漏斗向容器存入物品或从容器取出物品的相关保护。服务器漏斗很多时，设为 true 可略微改善性能，但要注意：只要距离边界足够近，区域外的漏斗就能抽取区域内的物品。</td>
</tr>
<tr>
<td markdown="span">break-hoppers-on-denied-move</td>
<td markdown="span">TRUE</td>
<td markdown="span">漏斗尝试抽取物品而被拒绝时（前一个配置项必须为 false），WorldGuard 会破坏漏斗方块，防止它不断重复尝试。</td>
</tr>
</tbody>
</table>

示例：不保护工作台

可以使用 `interaction-whitelist` 选项：

```text
interaction-whitelist: [workbench]
```

### protection.* { #protection }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">item-durability</td>
<td markdown="span">TRUE</td>
<td markdown="span">设为 `false` 后，物品永远不会损坏。</td>
</tr>
<tr>
<td markdown="span">remove-infinite-stacks</td>
<td markdown="span">FALSE</td>
<td markdown="span">移除堆叠数量为“无限”的物品，实际指任何堆叠数量小于 0 的物品；这通常是数值超过最大值后溢出为负数的结果。</td>
</tr>
<tr>
<td markdown="span">disable-xp-orb-drops</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止掉落经验球。</td>
</tr>
<tr>
<td markdown="span">use-max-priority-association</td>
<td markdown="span">FALSE</td>
<td markdown="span">活塞等非玩家关联对象，是否只视为其所在的最高优先级区域的成员。设为 `false` 时，这些对象属于其所在的所有区域，因此活塞可以将方块从某个区域内部向外推入周围区域，除非外部只有一个受保护的[全局区域](regions/global-region.md)。设为 `true` 时，活塞则无法将方块从区域内部向外推入优先级更低、受保护的周围区域。</td>
</tr>
</tbody>
</table>

### gameplay.* { #gameplay }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-potions</td>
<td markdown="span">[]</td>
<td markdown="span">禁止使用的药水类型列表。可用类型名称见 [Bukkit 列表](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)。</td>
</tr>
<tr>
<td markdown="span">block-potions-overly-reliably</td>
<td markdown="span">FALSE</td>
<td markdown="span">WorldGuard 是否采取更严格的措施，阻止 block-potions 中列出的药水。一般无需启用，因为它可能拦截超出预期的情况。</td>
</tr>
<tr>
<td markdown="span">disable-conduit-effects</td>
<td markdown="span">FALSE</td>
<td markdown="span">WorldGuard 是否禁用潮涌核心的效果。</td>
</tr>
</tbody>
</table>

示例：禁用夜视和迅捷药水

使用 [Bukkit 中列出的名称](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/potion/PotionEffectType.html)：

```text
block-potions: [night_vision, speed]
```

### simulation.sponge.* { #simulation-sponge }

!!! warning "警告"

    这些设置默认不包含在配置中。此功能已弃用，并计划在未来版本中移除。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否模拟 Minecraft Classic 中海绵方块的工作方式。从生存模式引入到 Minecraft 1.8 之间的数年里，海绵并不起作用；不过，此设置现已过时，不再推荐使用。</td>
</tr>
<tr>
<td markdown="span">radius</td>
<td markdown="span">3</td>
<td markdown="span">海绵的作用半径。</td>
</tr>
<tr>
<td markdown="span">redstone</td>
<td markdown="span">FALSE</td>
<td markdown="span">红石是否能控制模拟的海绵方块。</td>
</tr>
</tbody>
</table>

### default.* { #default }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">pumpkin-scuba</td>
<td markdown="span">FALSE</td>
<td markdown="span">头盔栏中戴着南瓜（南瓜灯除外）的玩家是否获得水下呼吸。</td>
</tr>
<tr>
<td markdown="span">disable-health-regain</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用生命值自动恢复。</td>
</tr>
</tbody>
</table>

### physics.* { #physics }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">no-physics-gravel</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止砂砾下落。</td>
</tr>
<tr>
<td markdown="span">no-physics-sand</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止沙子下落。</td>
</tr>
<tr>
<td markdown="span">vine-like-rope-ladders</td>
<td markdown="span">FALSE</td>
<td markdown="span">梯子是否像藤蔓一样工作：只要最上方的梯子方块位于有效位置（贴在墙上），其余梯子就不会脱落。</td>
</tr>
<tr>
<td markdown="span">allow-portal-anywhere</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否允许在无效位置放置传送门方块。</td>
</tr>
<tr>
<td markdown="span">disable-water-damage-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">不会被水流破坏的方块类型列表。</td>
</tr>
</tbody>
</table>

示例：防止水流破坏红石粉和红石火把

材质名称来自 [Bukkit 材质列表](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)：

```text
physics:
    disable-water-damage-blocks: [redstone_wire, redstone_torch]
```

### ignition.* { #ignition }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-tnt</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止 TNT 引爆。</td>
</tr>
<tr>
<td markdown="span">block-tnt-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否使 TNT 不再破坏方块。</td>
</tr>
<tr>
<td markdown="span">block-lighter</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用打火石。</td>
</tr>
</tbody>
</table>

### fire.* { #fire }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-lava-fire-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">岩浆是否能够引发火灾。</td>
</tr>
<tr>
<td markdown="span">disable-all-fire-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">火焰是否能够蔓延。</td>
</tr>
<tr>
<td markdown="span">disable-fire-spread-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">火焰无法蔓延到或至少无法烧毁的方块类型列表。</td>
</tr>
<tr>
<td markdown="span">lava-spread-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">设置此列表后，除空气外，岩浆只能流到列表中指定的方块上。</td>
</tr>
</tbody>
</table>

### mobs.* { #mobs }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">block-creeper-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用苦力怕爆炸的影响。</td>
</tr>
<tr>
<td markdown="span">block-creeper-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用苦力怕爆炸造成的方块破坏。</td>
</tr>
<tr>
<td markdown="span">block-wither-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用凋灵爆炸的影响。</td>
</tr>
<tr>
<td markdown="span">block-wither-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用凋灵爆炸造成的方块破坏。</td>
</tr>
<tr>
<td markdown="span">block-wither-skull-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用凋灵之首的影响。</td>
</tr>
<tr>
<td markdown="span">block-wither-skull-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用凋灵之首造成的方块破坏。</td>
</tr>
<tr>
<td markdown="span">block-enderdragon-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用末影龙造成的方块破坏。</td>
</tr>
<tr>
<td markdown="span">block-enderdragon-portal-creation</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用末影龙创建传送门的能力。</td>
</tr>
<tr>
<td markdown="span">block-fireball-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用火球爆炸的影响。</td>
</tr>
<tr>
<td markdown="span">block-fireball-block-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用火球造成的方块破坏。</td>
</tr>
<tr>
<td markdown="span">anti-wolf-dumbness</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否让狼在走进岩浆、卡住等多种情况下保持无敌。狼刚加入游戏时，Minecraft 的寻路能力很差，狼经常会走进岩浆或火中。不过，Minecraft 中伙伴型生物的 AI 至今仍有不少改进空间，因此此设置可能依然有用。</td>
</tr>
<tr>
<td markdown="span">allow-tamed-spawns</td>
<td markdown="span">TRUE</td>
<td markdown="span">是否允许生成可驯服的生物，如狼、马、猫等。</td>
</tr>
<tr>
<td markdown="span">disable-enderman-griefing</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用末影人拾取和放置方块的能力。</td>
</tr>
<tr>
<td markdown="span">disable-snowman-trails</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用雪傀儡留下雪迹的功能。</td>
</tr>
<tr>
<td markdown="span">block-painting-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用生物破坏画的能力。</td>
</tr>
<tr>
<td markdown="span">block-item-frame-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用生物破坏物品展示框的能力。</td>
</tr>
<tr>
<td markdown="span">block-armor-stand-destroy</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用生物破坏盔甲架的能力。</td>
</tr>
<tr>
<td markdown="span">block-plugin-spawning</td>
<td markdown="span">TRUE</td>
<td markdown="span">为应用部分配置选项或保护世界区域，是否在需要时阻止由插件生成的生物。</td>
</tr>
<tr>
<td markdown="span">block-above-ground-slimes</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止史莱姆在地表生成。</td>
</tr>
<tr>
<td markdown="span">block-other-explosions</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用其他类型的爆炸。</td>
</tr>
<tr>
<td markdown="span">block-zombie-door-destruction</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用僵尸破门的能力。</td>
</tr>
<tr>
<td markdown="span">block-vehicle-entry</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止生物进入载具。</td>
</tr>
<tr>
<td markdown="span">block-creature-spawn</td>
<td markdown="span">[]</td>
<td markdown="span">禁止生成的实体类型列表。</td>
</tr>
</tbody>
</table>

### player-damage.* { #player-damage }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-fall-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的摔落伤害。</td>
</tr>
<tr>
<td markdown="span">disable-lava-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的岩浆伤害。</td>
</tr>
<tr>
<td markdown="span">disable-fire-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的火焰伤害。</td>
</tr>
<tr>
<td markdown="span">disable-lightning-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的雷击伤害。</td>
</tr>
<tr>
<td markdown="span">disable-drowning-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的溺水伤害。</td>
</tr>
<tr>
<td markdown="span">disable-suffocation-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的窒息伤害。</td>
</tr>
<tr>
<td markdown="span">disable-contact-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的接触伤害，如仙人掌伤害。</td>
</tr>
<tr>
<td markdown="span">teleport-on-suffocation</td>
<td markdown="span">FALSE</td>
<td markdown="span">玩家窒息时，是否将其传送到能找到的安全位置，通常是上方。此功能可能让玩家穿过垂直屏障。</td>
</tr>
<tr>
<td markdown="span">disable-void-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家的虚空伤害，即掉入世界底部时受到的伤害。</td>
</tr>
<tr>
<td markdown="span">teleport-on-void-falling</td>
<td markdown="span">FALSE</td>
<td markdown="span">玩家掉入虚空时，是否将其传送到能找到的安全位置。此功能可能让玩家进入平常无法到达的区域。</td>
</tr>
<tr>
<td markdown="span">reset-fall-on-void-teleport</td>
<td markdown="span">FALSE</td>
<td markdown="span">虚空传送时重置摔落距离。关闭此项可能使玩家因摔落伤害死亡，不过至少物品不会掉在虚空中。</td>
</tr>
<tr>
<td markdown="span">disable-explosion-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家受到的爆炸伤害。</td>
</tr>
<tr>
<td markdown="span">disable-mob-damage</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用生物对玩家造成的伤害。</td>
</tr>
<tr>
<td markdown="span">disable-death-messages</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁用玩家死亡消息。</td>
</tr>
</tbody>
</table>

### crops.* { #crops }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-creature-trampling</td>
<td markdown="span">FALSE</td>
<td markdown="span">禁止生物踩坏耕地。</td>
</tr>
<tr>
<td markdown="span">disable-player-trampling</td>
<td markdown="span">FALSE</td>
<td markdown="span">禁止玩家踩坏耕地。</td>
</tr>
</tbody>
</table>

### turtle-egg.* { #turtle-egg }

选项与 crops 部分相同，但针对海龟蛋。

### sniffer-egg.* { #sniffer-egg }

选项与 crops 部分相同，但针对嗅探兽蛋。

### weather.* { #weather }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">prevent-lightning-strike-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">不会被闪电击中的方块类型列表。</td>
</tr>
<tr>
<td markdown="span">disable-lightning-strike-fire</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止雷击引发的火灾。</td>
</tr>
<tr>
<td markdown="span">disable-thunderstorm</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否始终阻止雷暴开始。</td>
</tr>
<tr>
<td markdown="span">disable-weather</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否始终阻止天气事件（包括雷暴）开始。</td>
</tr>
<tr>
<td markdown="span">disable-pig-zombification</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止猪被雷击后“僵尸化”。</td>
</tr>
<tr>
<td markdown="span">disable-villager-witchification</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止村民被雷击后变成女巫。</td>
</tr>
<tr>
<td markdown="span">disable-powered-creepers</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止苦力怕被雷击后变成闪电苦力怕。</td>
</tr>
<tr>
<td markdown="span">always-raining</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否始终下雨或下雪。</td>
</tr>
<tr>
<td markdown="span">always-thundering</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否始终打雷。</td>
</tr>
</tbody>
</table>

### dynamics.* { #dynamics }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">disable-mushroom-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止蘑菇扩散。</td>
</tr>
<tr>
<td markdown="span">disable-ice-melting</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止冰融化。</td>
</tr>
<tr>
<td markdown="span">disable-snow-melting</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止雪融化。</td>
</tr>
<tr>
<td markdown="span">disable-snow-formation</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止积雪形成。</td>
</tr>
<tr>
<td markdown="span">disable-ice-formation</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止冰形成。</td>
</tr>
<tr>
<td markdown="span">disable-leaf-decay</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止树叶腐烂。</td>
</tr>
<tr>
<td markdown="span">disable-grass-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止草生长。</td>
</tr>
<tr>
<td markdown="span">disable-mycelium-spread</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止菌丝体扩散。</td>
</tr>
<tr>
<td markdown="span">disable-vine-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止藤蔓和海带生长。</td>
</tr>
<tr>
<td markdown="span">disable-rock-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止滴水石等岩石生长。</td>
</tr>
<tr>
<td markdown="span">disable-sculk-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止幽匿生长。</td>
</tr>
<tr>
<td markdown="span">disable-crop-growth</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止小麦、胡萝卜、西瓜等作物生长。</td>
</tr>
<tr>
<td markdown="span">disable-soil-dehydration</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止耕地脱水。</td>
</tr>
<tr>
<td markdown="span">disable-coral-block-fade</td>
<td markdown="span">FALSE</td>
<td markdown="span">珊瑚离开水后是否仍然存活。</td>
</tr>
<tr>
<td markdown="span">disable-copper-block-fade</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否禁止铜块氧化。</td>
</tr>
<tr>
<td markdown="span">snow-fall-blocks</td>
<td markdown="span">[]</td>
<td markdown="span">设置此方块类型列表后，雪只能落在列表中的方块上。</td>
</tr>
</tbody>
</table>

### chest-protection.* { #chest-protection }

!!! warning "警告"

    这些设置默认不包含在配置中。基于告示牌的箱子保护已弃用，并计划在未来版本中移除。详见[箱子保护](chest-protection.md)。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">启用[箱子保护](chest-protection.md)。</td>
</tr>
<tr>
<td markdown="span">disable-off-check</td>
<td markdown="span">TRUE</td>
<td markdown="span">即使箱子保护关闭，WorldGuard 仍会阻止创建带有 `[Lock]` 的告示牌，以免日后启用保护时，玩家提前锁定原本不属于自己的箱子。将此选项设为 `true`，会在箱子保护关闭时禁用这项检查。</td>
</tr>
</tbody>
</table>

### blacklist.* { #blacklist }

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">use-as-whitelist</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否反转黑名单的用途，让玩家只能执行黑名单中被禁止的操作。</td>
</tr>
</tbody>
</table>

### blacklist.logging.* { #blacklist-logging }

这些设置决定[黑名单](blacklist.md)中的“log”动作如何工作，可以同时启用多个日志输出目标。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">console:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">TRUE</td>
<td markdown="span">是否启用控制台日志。</td>
</tr>
<tr>
<td markdown="span">database:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否启用数据库日志。</td>
</tr>
<tr>
<td markdown="span">dsn</td>
<td markdown="span">`jdbc:mysql://localhost:3306/minecraft`</td>
<td markdown="span">数据库连接字符串。默认值中的 `minecraft` 是数据库名称。</td>
</tr>
<tr>
<td markdown="span">user</td>
<td markdown="span">root</td>
<td markdown="span">连接数据库使用的用户名。</td>
</tr>
<tr>
<td markdown="span">pass</td>
<td markdown="span"></td>
<td markdown="span">连接数据库使用的密码。</td>
</tr>
<tr>
<td markdown="span">table</td>
<td markdown="span">blacklist_events</td>
<td markdown="span">使用的数据表。</td>
</tr>
<tr>
<td markdown="span">file:</td>
<td markdown="span"></td>
<td markdown="span"></td>
</tr>
<tr>
<td markdown="span">enable</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否启用文件日志。</td>
</tr>
<tr>
<td markdown="span">path</td>
<td markdown="span">worldguard/logs/%Y-%m-%d.log</td>
<td markdown="span">日志文件的路径模式。</td>
</tr>
<tr>
<td markdown="span">open-files</td>
<td markdown="span">10</td>
<td markdown="span">同时打开的文件句柄数量上限，即操作系统中的文件句柄。</td>
</tr>
</tbody>
</table>

### regions.* { #regions }

!!! hint "提示"

    `use-creature-spawn-event` 无法按世界单独覆盖。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">wand</td>
<td markdown="span">minecraft:leather</td>
<td markdown="span">右键点击方块以查看影响该位置的区域时，使用的物品 ID。默认物品是皮革；以前是线，但后来 Minecraft 为线添加了实际用途。</td>
</tr>
<tr>
<td markdown="span">disable-bypass-by-default</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否默认禁用绕过保护的权限。</td>
</tr>
<tr>
<td markdown="span">announce-bypass-status</td>
<td markdown="span">FALSE</td>
<td markdown="span">玩家登录时是否显示 `/region bypass` 的提示。</td>
</tr>
<tr>
<td markdown="span">invincibility-removes-mobs</td>
<td markdown="span">FALSE</td>
<td markdown="span">启用后，如果玩家因无敌[区域旗标](regions/flags.md)而处于无敌状态，攻击该玩家的生物会从世界中移除。</td>
</tr>
<tr>
<td markdown="span">fake-player-build-override</td>
<td markdown="span">TRUE</td>
<td markdown="span">名称以 `[` 开头、以 `]` 结尾的玩家是否绕过所有保护。这类情况只会出现在某些第三方插件或模组中：它们使用“假玩家”，而没有触发相应的正常事件。</td>
</tr>
<tr>
<td markdown="span">explosion-flags-block-entity-damage</td>
<td markdown="span">TRUE</td>
<td markdown="span">各种 `-explosion` [区域旗标](regions/flags.md)在启用时是否也禁止实体受到伤害。</td>
</tr>
<tr>
<td markdown="span">high-frequency-flags</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否根据[区域旗标](regions/flags.md)处理火焰蔓延、流体流动等高频事件，例如 `fire-spread`、`water-flow` 和 `lava-flow`。默认禁用，因为这些旗标很少使用，而且在玩家和区域都非常多的情况下，启用此项可能影响性能。</td>
</tr>
<tr>
<td markdown="span">protect-against-liquid-flow</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否阻止流体在区域之间流动，以免玩家把岩浆或水流引入其他玩家的区域进行破坏。此项必须与 `high-frequency-flags` 同时启用才会生效。</td>
</tr>
<tr>
<td markdown="span">use-paper-entity-origin</td>
<td markdown="span">FALSE</td>
<td markdown="span">在 [Paper 服务器](https://papermc.io)上，此选项会让实体视为其生成区域的成员，而非当前所在区域的成员。这样可自动防止游荡进区域的生物意外破坏该区域。注意，这与生物追踪区域内玩家的情况不同；后者仍取决于玩家的权限，而不是生物的权限。</td>
</tr>
<tr>
<td markdown="span">max-claim-volume</td>
<td markdown="span">30000</td>
<td markdown="span">通过[自助认领区域](regions/claiming.md)可认领的单个区域的方块数量上限。</td>
</tr>
<tr>
<td markdown="span">claim-only-inside-existing-regions</td>
<td markdown="span">FALSE</td>
<td markdown="span">玩家是否只能在现有区域内认领区域。</td>
</tr>
<tr>
<td markdown="span">cancel-chat-without-recipients</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否取消没有接收者的聊天消息，例如所有在线玩家都处于 `receive-chat` 设为 `deny` 的区域时。启用此项可能让外部聊天接收端（如 Discord 桥接插件）也无法显示这些消息。</td>
</tr>
<tr>
<td markdown="span">nether-portal-protection</td>
<td markdown="span">TRUE</td>
<td markdown="span">是否阻止可能在保护区域中创建新传送门的传送门旅行。</td>
</tr>
<tr>
<td markdown="span">set-parent-on-claim</td>
<td markdown="span"></td>
<td markdown="span">通过[自助认领区域](regions/claiming.md)创建的新区域，会自动将此区域 ID 对应的区域设为[父区域](regions/priorities.md#inheritance)。</td>
</tr>
<tr>
<td markdown="span">location-flags-only-inside-regions</td>
<td markdown="span">FALSE</td>
<td markdown="span">位置类型的[区域旗标](regions/flags.md)所指定的位置，是否必须在对应区域内部。</td>
</tr>
<tr>
<td markdown="span">titles-always-use-default-times</td>
<td markdown="span">TRUE</td>
<td markdown="span">如果使用欢迎或离开标题，而其他插件导致标题过快消失，请将此项设为 true。</td>
</tr>
<tr>
<td markdown="span">max-region-count-per-player:</td>
<td markdown="span"></td>
<td markdown="span">玩家通过[自助认领区域](regions/claiming.md)最多可认领的区域数量。可以在下方为各权限组添加条目（如“default”），设置不同上限。“default”是默认上限。如果玩家同时属于多个列出的权限组，则使用其中最高的上限。</td>
</tr>
<tr>
<td markdown="span">default</td>
<td markdown="span">7</td>
<td markdown="span">（见上文。）</td>
</tr>
</tbody>
</table>

示例：为不同权限组设置不同的区域数量上限

为每个权限组分别添加条目：

```text
max-region-count-per-player:
    default: 7
    builders: 20
    moderators: 40
```

!!! warning "警告"

    此分类中还有一些额外设置，但不建议修改：

    <table>
    <colgroup>
    </colgroup>
    <thead>
    <tr>
    <th markdown="span">配置项</th>
    <th markdown="span">默认值</th>
    <th markdown="span">说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td markdown="span">enable</td>
    <td markdown="span">TRUE</td>
    <td markdown="span">是否启用定义区域的功能。</td>
    </tr>
    <tr>
    <td markdown="span">use-creature-spawn-event</td>
    <td markdown="span">TRUE</td>
    <td markdown="span">是否处理生物移动事件，以应用某些与生物有关的[区域旗标](regions/flags.md)。</td>
    </tr>
    </tbody>
    </table>

### regions.uuid-migration.* { #regions-uuid-migration }

这些设置用于从旧版 WorldGuard 和 Minecraft 迁移。以前，Minecraft 账号仅通过名称识别；大约在 Minecraft 1.7 末期，游戏改为在内部使用“UUID”识别玩家，玩家也由此*可以改名*。但旧配置仍按名称引用玩家，因此以下设置会在服务器启动时执行一次向 UUID 的转换，之后自动禁用。

通过再次修改设置，可以重复运行 UUID 迁移；每次只会转换尚未转为 UUID 的名称。如果没有需要转换的名称，就不会执行任何操作。

!!! hint "提示"

    这些设置无法按世界单独覆盖。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">perform-on-next-start</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否在下次服务器启动时执行一次 UUID 迁移。如果配置文件中尚无此项，WorldGuard 会将其视为 `true`，完成转换后再设为 `false`。</td>
</tr>
<tr>
<td markdown="span">keep-names-that-lack-uuids</td>
<td markdown="span">TRUE</td>
<td markdown="span">有时，添加到区域的玩家名称实际上并不存在。此选项会在区域数据中保留无法转换的名称，方便以后移除，或通过调整本节设置重新执行转换。</td>
</tr>
</tbody>
</table>

### regions.sql.* { #regions-sql }

!!! warning "警告"

    这些设置默认不包含在配置中。WorldGuard 区域存储的 SQL 支持已弃用，并计划在未来版本移除，请迁移到 YAML 存储。更多信息见[存储驱动](regions/storage.md)。

!!! hint "提示"

    这些设置无法按世界单独覆盖。

<table>
<colgroup>
</colgroup>
<thead>
<tr>
<th markdown="span">配置项</th>
<th markdown="span">默认值</th>
<th markdown="span">说明</th>
</tr>
</thead>
<tbody>
<tr>
<td markdown="span">use</td>
<td markdown="span">FALSE</td>
<td markdown="span">是否使用 MySQL 存储数据，详见[存储驱动](regions/storage.md)。</td>
</tr>
<tr>
<td markdown="span">dsn</td>
<td markdown="span">`jdbc:mysql://localhost/worldguard`</td>
<td markdown="span">数据库连接字符串。默认值中的 `worldguard` 是数据库名称。</td>
</tr>
<tr>
<td markdown="span">username</td>
<td markdown="span">worldguard</td>
<td markdown="span">连接数据库使用的用户名。</td>
</tr>
<tr>
<td markdown="span">password</td>
<td markdown="span">worldguard</td>
<td markdown="span">连接数据库使用的密码。</td>
</tr>
<tr>
<td markdown="span">table-prefix</td>
<td markdown="span"></td>
<td markdown="span">数据表前缀。</td>
</tr>
</tbody>
</table>

## 子页面 { #subpages }

- [主机密钥](host-keys.md)
