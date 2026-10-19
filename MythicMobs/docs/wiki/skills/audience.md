---
title: 接收对象
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Audience
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 接收对象

# 受众 {#audience}

通过在支持受众的机制中使用 `audience=<audience type>` 属性并指定要使用的受众类型，受众属性可用于仅向特定玩家组而不是整个服务器显示效果。这有助于防止不必要地向每个人显示过多的粒子，并且可以在一定程度上减少客户端延迟。

受众类型有：

- `self`/`caster`：技能机制的施法者。
- `nonSelfWorld`/`nonSelf`：同一世界中除施法者之外的所有玩家。
- `target`：技能机制的目标。
- `world`：世界上的每一个玩家
- `tracked`/`trackedplayers`/：客户端可以渲染施法者的所有玩家。
- `nearby`/`nearbyplayers`：附近的每个玩家（比`65536`块更近）
- `@Targeter`：目标选择器选中的所有玩家。

> 默认值为`tracked`

其中 `audience=@Targeter` 尤其值得注意，它允许将任意实体目标选择器的结果用作效果显示对象。

```yaml
    Skills:
    - effect:particles{particle=reddust;y=2;audience=@Owner} @self
```

## [执行接收对象](https://gist.github.com/Taiyou06/0cb4963bec081a8928ffdd54f8a5a44a) {#execution-audiences}

显示对象作用域的处理会在重新登录、重启和整个效果执行链中持续生效。
