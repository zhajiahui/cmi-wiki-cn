---
title: 假人选项
source_url: https://wiki.mythiccraft.io/mythicmobs/Mobs/MannequinOptions
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 假人选项 {#mannequin-options}

所有可用的人体模型实体选项。所有这些选项都位于 `MannequinOptions` 部分下，如下所示：

```yml
cool_display:
  Type: MANNEQUIN
  MannequinOptions:
    Player: Herobrine
```

1. [Immovable](mannequinoptions.md#immovable)
2. [Description](mannequinoptions.md#description)
3. [HideDescription](mannequinoptions.md#hidedescription)
4. [MainHand](mannequinoptions.md#mainhand)
5. [Pose](mannequinoptions.md#pose)
6. [Player](mannequinoptions.md#player)
7. [Skin](mannequinoptions.md#skin)
8. [Cape](mannequinoptions.md#cape)
9. [Elytra](mannequinoptions.md#elytra)
10. [Model](mannequinoptions.md#model)

#### Immovable {#immovable}

人体模型是否不可移动 默认为`false`

```yaml
  MannequinOptions:
    Immovable: true
```

#### 说明 {#description}

人体模型的描述。将出现在模特名字下方。

```yaml
  MannequinOptions:
    Description: "Hello World!"
```

#### HideDescription {#hidedescription}

是否隐藏人体模型的描述 默认为`false`

```yaml
  MannequinOptions:
    HideDescription: true
```

#### MainHand {#mainhand}

指定主手。可选 LEFT 或 RIGHT，即 [MainHand Spigot 枚举](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/inventory/MainHand.html)中的值。

```yaml
  MannequinOptions:
    MainHand: LEFT
```

#### Pose {#pose}

人体模型的姿势。   可以是 [Pose Spigot Enum](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/entity/Pose.html) 中可用的任何姿势

```yaml
  MannequinOptions:
    Pose: DYING
```

#### Player {#player}

指定用于人偶皮肤的玩家，默认为 `Ashijin`。

```yaml
  MannequinOptions:
    Player: _xXSuperN00B67Xx_
```

#### Skin {#skin}

用于人体模型皮肤的纹理请参考 [minecraft wiki](https://minecraft.wiki/w/Mannequin#Entity_data:~:text=%5BString%5D%C2%A0texture,a%20default%20skin.) 了解更多信息

```yaml
  MannequinOptions:
    Skin: namespace:directory/texturename
```

#### Cape {#cape}

用于人体模型斗篷的纹理请参考 [minecraft wiki](https://minecraft.wiki/w/Mannequin#Entity_data:~:text=%5BString%5D%C2%A0cape,displaying%20no%20cape.) 了解更多信息

```yaml
  MannequinOptions:
    Cape: namespace:directory/texturename
```

#### Elytra {#elytra}

用于人体模型鞘翅的纹理请参考 [minecraft wiki](https://minecraft.wiki/w/Mannequin#Entity_data:~:text=%5BString%5D%C2%A0elytra,the%20default%20elytra.) 了解更多信息

```yaml
  MannequinOptions:
    Elytra: namespace:directory/texturename
```

#### Model {#model}

人体模型的模型类型。   可以是 [SkinModel Spigot Enum](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/profile/PlayerTextures.SkinModel.html) 中可用的任何模型，默认为 `CLASSIC`

```yaml
  MannequinOptions:
    Model: SLIM
```
