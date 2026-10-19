---
title: 生成消息
source_url: https://wiki.mythiccraft.io/mythicmobs/Guides/Spawn-Message
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 生成消息 {#spawn-message}

**难度：入门**

当 Boss 等特殊生物生成时，你可能希望服务器中的玩家都能知道。可以将 [Message 机制](../skills/mechanics/message.md)与 [onSpawn 触发器](../skills/triggers/onspawn.md)结合使用。

请注意，如果刷怪点位于当前未加载的区块中，这种方法可能无法对该刷怪点生成的生物生效。

这个基本示例只会向 [@server](../skills/targeters/playersonserver.md) 发送消息，通知大家生物已经生成。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Skills:
  - message{m="&6The Skeleton King has spawned!"} @server ~onSpawn
```

这样已经可以使用，但你可能还想向玩家显示生物的坐标！可以通过[施法者占位符](../skills/placeholders.md)实现。

```yaml
SkeletonKing:
  Type: WITHER_SKELETON
  Display: '&6Skeleton King'
  Health: 500
  Damage: 10
  Skills:
  - message{m="&6The Skeleton King has spawned! You can find it at, &aX<&co>&b<caster.l.x> &aY<&co>&b<caster.l.y> &aZ<&co>&b<caster.l.x>"} @server ~onSpawn
```

我们使用了以下占位符：

- `<&co>`：插入 `:` 符号，直接使用该符号会影响语法。
- `<caster.l.x>`：显示施法者的 X 坐标。
- `<caster.l.y>`：显示施法者的 Y 坐标。
- `<caster.l.z>`：显示施法者的 Z 坐标。
