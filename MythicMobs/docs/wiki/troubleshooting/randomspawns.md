---
title: 随机生成排错
source_url: https://wiki.mythiccraft.io/mythicmobs/Troubleshooting/RandomSpawns
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 随机生成排错

# RandomSpawns 不生效 {#randomspawns-not-working}

- 检查 randomspawn 的 `Chance`。设置过低可能就是原因，可先将它设为 `1`，检查问题是否由此导致。如果问题仍然存在，请继续执行以下步骤，解决问题前暂时保持该值。
- 检查世界难度。如果要生成敌对生物类型，难度应设为和平以外的模式！
- 移除**所有限制**，例如 `biome` 和 `conditions`，然后检查是否能正常工作
- 检查是否有拼写错误的单词，例如：
  - 生物内部名称
  - 世界名称
- 如果删除所有条件后 RandomSpawn 能正常工作，就逐一加回条件，找出导致问题的条件。如果仍不清楚这些条件为何导致问题，可前往我们的 [Discord](https://www.mythiccraft.io/discord) 寻求帮助
- 如果 randomspawn 仍然无法工作，请根据 randomspawn 的 `Action` 采取下面列出的操作来继续调试

### ADD 操作 {#add-action}

- 确保插件的生成配置正确设置
  - （低于 MM 5.6.1）：配置文件位于 `/MythicMobs/config.yml`
  - （MM 5.6.1 或更高版本）：配置文件位于 `/MythicMobs/config/config-spawning.yml`
- 检查配置文件中的 `GeneraSpawnPoints` 是否已启用，否则 ADD 操作不会生效
- 确保你处于生存或冒险模式，因为其他游戏模式将不起作用
- 如果以上方法均失败，请通过我们的 [discord](https://www.mythiccraft.io/discord) 寻求帮助

### REPLACE 操作 {#replace-action}

- 检查世界难度，应设为和平以外的模式！
- 确保世界可以自然地生成怪物（例如，通过确保`doMobSpawning`游戏规则设置为`true`等）。
- 检查区域插件（[World Guard](https://dev.bukkit.org/projects/worldguard)、[Grief Defender](https://www.spigotmc.org/resources/1-12-2-1-20-4-griefdefender-claim-plugin-grief-prevention-protection.68900/) 等）的[标志](https://worldguard.enginehub.org/en/latest/regions/flags/#mobs-fire-and-explosions)，确认区域内是否有[阻止生物生成的标志](https://worldguard.enginehub.org/en/latest/regions/flags/#mobs-fire-and-explosions)
