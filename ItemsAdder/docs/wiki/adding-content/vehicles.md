---
title: "载具"
source_url: "https://wiki.itemsadder.com/adding-content/vehicles"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 载具

可以创建功能有限的简单载具，丰富游戏内容。这些载具的实现较为简单。

```yaml
info:
  namespace: my_vehicles
items:
  shopping_cart:
    enabled: true
    display_name: Shopping Cart
    permission: my_vehicles.ground.shopping_cart
    resource:
      material: PAPER
      generate: false
      model_path: item/shopping_cart
    behaviours:
      vehicle:
        sit_height: 2
        step_height: 0.1
        hitbox:
          length: 2
          width: 2.3
          height: 1
        speed:
          drive: 0.3
          jump: 0.3
        fuel:
          start: 60
          max: 300
          items:
            banana: 30
            pear: 30
        smoke:
          amount: 1
```

默认示例包包含一些载具示例，可从[这里下载](https://github.com/ItemsAdder/OtherPacks/releases)。


## 属性

#### `sit_height`

玩家乘坐位置的座椅高度。

#### `step_height`

载具可自动跃过的最大高度。

#### `hitbox`

载具碰撞箱。

#### `speed`

载具速度。

#### `fuel`

与载具交互时，可用于补充燃料条的物品。

#### `smoke`

在载具后方生成的烟雾。

## 创建高级载具

可以使用新的实体系统创建高级载具，例如加入多个座位、动画和声音。

更多信息见：

[实体](entities.md)

### 高级载具示例包

可从[这里](https://www.spigotmc.org/resources/wheelchairs-rideable-wheelchairs-for-itemsadder.127743/)下载一个高级载具示例包。

