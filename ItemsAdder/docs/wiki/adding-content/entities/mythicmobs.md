---
title: "MythicMobs"
source_url: "https://wiki.itemsadder.com/adding-content/entities/mythicmobs"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# MythicMobs

## 为 MythicMobs 生物更换外观

可以将自定义模型用作任意 MythicMobs 生物的外观。

此插件本身不依赖 MythicMobs，不过部分服务器可能希望与其配合使用。

## 更换模型

在以下路径创建 **MythicMobs** 生物配置文件：`plugins/MythicMobs/entities/ninja_skeleton.yml`\
（文件名可自行决定）。

不要将类型设为 `PLAYER`，否则会造成头部和身体旋转问题。

```yaml
ninja_skeleton:
  Type: ZOMBIE
  Display: '&aNinja Skeleton'
  Health: 10
  Damage: 2
  Options:
    MovementSpeed: 0
    Silent: true
  Skills:
  - customentity{model=custom:ninja_skeleton} @self ~onSpawn
  - customentity{play=attack} @self ~onAttack
  - customentity{walk=b_walk} @self ~onAttack
```

本例将 **MythicMobs** 生物的外观更换为 `ninja_skeleton`。

```yaml
customentity{model=MODEL NAME} @self ~onSpawn
```

## 动画

本例还添加了一些 Skills，用于动态替换生物动画。\
`{play=attack}` 用于播放攻击动画，本例在实体攻击时播放。

\
`{walk=b_walk}` 用于将行走动画替换为 `b_walk`，这是“愤怒”行走动画，因为该生物刚攻击了其他实体，并拥有攻击目标。

### 动画

* `customentity{idle=ANIMATION}`：更改待机动画
* `customentity{walk=ANIMATION}`：更改行走动画
* `customentity{attack=ANIMATION}`：更改攻击动画
* `customentity{death=ANIMATION}`：更改死亡动画
* `customentity{play=ANIMATION}`：立即播放动画
* `customentity{stop=ANIMATION}`：停止当前动画

## 骨骼

### 可见性

通过配置控制骨骼的隐藏与显示

```
- bone{name=BONE;visible=TRUE/FALSE} TARGETER ~EVENT
```

示例：在特定事件发生时隐藏腿部骨骼

```
- bone{name=leftLeg;visible=false} @self ~onDamaged
```

### 颜色

通过配置更改骨骼颜色

```
- bone{name=BONE;color=COLOR} TARGETER ~EVENT
```

默认颜色（白色）：`16777215`\
[颜色选择器](https://minecraftcommand.science/armor-color)

示例：自定义实体受伤时更改骨骼颜色

```
- bone{name=leftLeg;color=16711790} @self ~onDamaged
```

### 附魔光效

通过配置在骨骼上显示附魔光效

```
- bone{name=BONE;enchant=TRUE/FALSE} TARGETER ~EVENT
```

示例：自定义实体受伤时在骨骼上显示附魔光效

```
- bone{name=leftLeg;enchant=true} @self ~onDamaged
```

### 将上述属性应用到每个骨骼

```
- bone{all=true;PROPERTY=VALUE} TARGETER ~EVENT
```

示例：自定义实体受伤时隐藏所有骨骼

```
- bone{all=true;visible=false} @self ~onDamaged
```

## 乘坐骨骼

```
- mountentity{bone=BONE;locked=TRUE/FALSE;control=TRUE/FALSE} TARGETER ~EVENT
```

示例：右键点击时骑乘自定义实体，禁用 SHIFT 下马（低于 1.16 的客户端不支持），并禁止用 WASD 控制实体。

```
- mountentity{bone=mountbone;locked=true;control=false} @trigger ~onInteract
```

警告：如果要这样手动处理骑乘，必须在自定义实体的 **ItemAdder** 配置中设置此属性：

`mount_on_interact: false`

```yaml
info:
  namespace: custom
entities:
  testmm:
    display_name: "testmm"
    type: ZOMBIE
    model_folder: entity/testmm
    speed:
      movement: 0.25
      flying: 0.25
    mount_on_interact: false
```

### 下马

移除部分乘坐骨骼上的乘客

```
- dismountentity{bones=BONE1,BONE2,BONE3} TARGETER ~EVENT
```

移除单个乘坐骨骼上的乘客

```
- dismountentity{bones=BONE1} TARGETER ~EVENT
```

移除全部乘坐骨骼上的乘客

```
- dismountentity{all=true} TARGETER ~EVENT
```

示例：

```
- dismountentity{bones=mount1,mount2} @self ~onDamaged
- dismountentity{all=true} @self ~onDamaged
```

### 骨骼目标选择器

骨骼目标选择器返回指定骨骼的位置。

```
@bone{bone=BONE}
```

示例：每隔 3 刻在骨骼中心播放一次粒子。

```
- effect:particles{vd=50;p=end_rod;amount=10;speed=0;hS=0.2;vS=0.2;repeat=270;repeatInterval=1} @bone{bone=rightArm} ~onTimer:3
```

