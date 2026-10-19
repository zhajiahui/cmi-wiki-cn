# Build Permissions { #build-permissions }

An optional feature lets you provide build permissions based on permission nodes. It can be enabled in the [Configuration](https://worldguard.enginehub.org/en/latest/config/):

```text
build-permission-nodes:
    enable: true
    deny-message:
```

An optional message can be set to change the message that players receive when an action is blocked.

## Permissions List { #permissions-list }

- Block place: `worldguard.build.block.place.<material>`

- Block break: `worldguard.build.block.remove.<material>`

- Block interact: `worldguard.build.block.interact.<material>`

- Entity spawn: `worldguard.build.entity.place.<type>`

- Entity destroy: `worldguard.build.entity.remove.<type>`

- Entity interact: `worldguard.build.entity.interact.<type>`

- Entity damage: `worldguard.build.entity.damage.<type>`

- Item use: `worldguard.build.item.use.<material>`

The permissions are also checked in the style of `worldguard.build.block.<material>.<action>`, so `worldguard.build.block.<material>.place` would work too.

The list of usable material names comes from the [Material list in Bukkit](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html). For example, the permission for placing the bed block would be `worldguard.build.block.place.red_bed`. Be aware that *Material* contains both item and block names.
