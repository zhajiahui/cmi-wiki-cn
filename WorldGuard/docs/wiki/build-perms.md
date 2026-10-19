---
title: 建造权限
source_url: https://worldguard.enginehub.org/en/latest/build-perms/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 建造权限 { #build-permissions }

这项可选功能可以根据权限节点授予建造权限，可在[配置](config.md)中启用：

```text
build-permission-nodes:
    enable: true
    deny-message:
```

还可以设置一条可选消息，修改玩家在操作被阻止时收到的提示。

## 权限列表 { #permissions-list }

- 放置方块：`worldguard.build.block.place.<material>`

- 破坏方块：`worldguard.build.block.remove.<material>`

- 与方块交互：`worldguard.build.block.interact.<material>`

- 生成实体：`worldguard.build.entity.place.<type>`

- 销毁实体：`worldguard.build.entity.remove.<type>`

- 与实体交互：`worldguard.build.entity.interact.<type>`

- 伤害实体：`worldguard.build.entity.damage.<type>`

- 使用物品：`worldguard.build.item.use.<material>`

权限也会按 `worldguard.build.block.<material>.<action>` 形式检查，因此 `worldguard.build.block.<material>.place` 同样有效。

可用材质名称见 [Bukkit 材质列表](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)。例如，放置床方块的权限为 `worldguard.build.block.place.red_bed`。注意，*Material* 同时包含物品和方块名称。
