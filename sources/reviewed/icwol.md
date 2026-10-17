用一行文本定义物品堆。请注意，内容中不得包含空格。物品名称、物品描述等内容需要空格时，用下划线 `_` 代替；需要实际的下划线时，则写成双下划线 `__`。

##### 较复杂的物品示例

```text
diamondsword;{#Gray}My_Uber_Sword;&2Goblin_Slayer!\n{#pink}With_Love!;sharpness:3,durability:3;hideenchants
```

```text
bow;AttackDamage:1.5:multiply_base:Mainhand,Luck:1:multiply_base:Head;unbreakable;hideunbreakable
```

```text
leatherchestplate;#pink;Redstone:Coast
```

##### 材质

物品定义必须以材质名称开头。例如，`snowball`、`SNOWBALL`，甚至 `SNOW_BALL` 都可以识别。

###### 子值

子值之间用 `;` 分隔，后面跟上用于指定类型的标识，值则放在 `{}` 内。如果名称或物品描述中需要使用 `;`，请写成 **`;;`**。不得包含空格；用 `_` 代替空格，用 `__` 表示下划线。

##### 数量

数量写在材质名称后面，用 - 分隔。例如，**`ACACIA_PRESSURE_PLATE-5`** 表示 5 个物品。未指定数量时，默认使用 1。  
也可以用 `;` 分隔数量，例如 **`ACACIA_PRESSURE_PLATE;5`**。

##### 物品名称

物品名称写作 `n{&2Custom_Item_Name}`。如果它是第一个无法识别为其他参数的文本条目，也可以直接写作 `&2Custom_Item_Name`。如果内容包含 `\n`，则不会作为物品名称处理，而会作为物品描述。

示例：`BREAD-12;&2Tasty!` 或 `BREAD-12;n{&2Tasty_food!}`

##### 物品描述

物品描述写作 `l{&2First_Line\n&3Second_line}`，也可以直接写作 `&2First_Line\n&3Second_line`。使用 `\n` 分隔描述中的各行，内容中不得包含空格。如果只有一行，则必须放在 `l{}` 内，或先在它前面定义物品名称。

示例：`BREAD-12;l{&2Eat_Me!}` 或 `BREAD-12;&2Eat_Me!\n{#blue}Tasty!`

##### 附魔

物品附魔写作 `sharpness:2,durability:5`；包含多个附魔时，需要将它们分隔。

示例：`Bow;durability:5,power:1`

##### 自定义模型数据

物品的自定义模型数据写作 `cm{123456}`，其中必须填写整数。

示例：`carrot;cm{1234}`

##### 属性

物品属性写作 **`AttackDamage:1.5:add:Mainhand,Luck:1:multiply_base:Head`**。第一个值指定属性类型，后面是需要改变的数值。这个数值可以是任意小数，并按指定的运算方式处理。运算方式可以用数字 0、1、2 指定，也可以使用运算名称 add、multiply_base、multiply。

类型

- **Armor**
- **ArmorToughness**
- **AttackDamage**
- **AttackKnockback**
- **AttackSpeed**
- **FlyingSpeed**
- **FollowRange**
- **KnockbackResistance**
- **Luck**
- **MaxHealth**
- **MovementSpeed**
- **JumpHeight**
- **SpawnReinforcements**

运算方式

- **0** 或 **add**
- **1** 或 **multiply_base**
- **2** 或 **multiply**

槽位

- **Mainhand**
- **Offhand**
- **Head**
- **Chest**
- **Legs**
- **Feet**

示例：`bow;AttackDamage:1.5:multiply_base:Mainhand,Luck:1:multiply_base:Head`

##### 物品标记

物品标记写作 `hide_attributes,hide_enchants`，各标记之间用逗号分隔。

标记

- **hide_armor_trim**
- **hide_attributes**
- **hide_destroys**
- **hide_dye**
- **hide_enchants**
- **hide_placed_on**
- **hide_potion_effects**
- **hide_unbreakable**

示例：`diamondsword;hideunbreakable,hideattributes,hide_enchants`

##### 刷怪笼类型

仅适用于刷怪笼。可以直接用 `creeper` 或当前服务器版本中存在的其他实体类型来指定刷怪笼类型。  
补充：设置刷怪笼名称会更改刷怪笼的自定义名称。如果不使用 **n{[name]}** 格式定义物品的自定义名称，应在设置刷怪笼名称之前设置物品名称；名称会被移到物品描述部分。

示例：`spawner;&2My_Creepy_Spawner!;creeper` 或 `spawner;creeper;n{&2My_Creepy_Spawner!}`

##### 皮革盔甲颜色

仅适用于皮革盔甲物品。写法为 `leatherboots;662266`、`leatherboots;red` 或 **`leatherboots;125,23,123`**。

示例：`leatherboots;lightpurple` 或 `leatherboots;random`

##### 画

仅适用于画。直接填写画的名称即可。

类型

- Alban
- Aztec
- Aztec2
- Bomb
- Burning_skull
- Bust
- Courbet
- Creebet
- Donkey_kong
- Earth
- Fighters
- Fire
- Graham
- Kebab
- Match
- Pigscene
- Plant
- Pointer
- Pool
- Sea
- Skeleton
- Skull_and_roses
- Stage
- Sunset
- Void
- Wanderer
- Wasteland
- Water
- Wind
- Wither

示例：**`painting;pool`**

##### 山羊角

仅适用于山羊角。直接填写山羊角的名称即可。

类型

- Ponder
- Sing
- Seek
- Feel
- Admire
- Call
- Yearn
- Dream

示例：**`goathorn;call`**

##### 盔甲纹饰

适用于 1.20+ 服务器。

盔甲纹饰写作 `iron:dune`。可以任意组合材质和图案，但只能使用一种材质和一种图案。

纹饰材质

- **Iron**
- **Copper**
- **Gold**
- **Lapis**
- **Emerald**
- **Diamond**
- **Netherite**
- **Redstone**
- **Amethyst**
- **Quartz**

纹饰图案

- **Coast**
- **Dune**
- **Eye**
- **Host**
- **Raiser**
- **Rib**
- **Sentry**
- **Shaper**
- **Silence**
- **Snout**
- **Spire**
- **Tide**
- **Vex**
- **Ward**
- **Wayfinder**
- **Wild**

示例：**`chainmailchestplate;iron:dune`**

##### 药水

对于药水物品，可以用 **`speed:true:true`** 这样的写法，指定药水类型、是否增强效果，以及是否延长持续时间。

示例：`potion;speed:true:true`

##### 特殊参数

这些特殊参数用于指定物品的特定设置，例如 `unbreakable`。

**Unbreakable** — 使物品无法损坏。  
示例：`diamondsword;unbreakable`

##### 纹样陶片

仅适用于饰纹陶罐，例如 **`decoratedpot;Skull,Archer,Angler,Explorer`**。可以使用少于 4 个陶片，超过 4 个的部分会被忽略。

- **Angler**
- **Archer**
- **Arms_up**
- **Blade**
- **Brewer**
- **Burn**
- **Danger**
- **Explorer**
- **Friend**
- **Heartbreak**
- **Heart**
- **Howl**
- **Miner**
- **Mourner**
- **Plenty**
- **Prize**
- **Sheaf**
- **Shelter**
- **Skull**
- **Snort**

示例：**`decoratedpot;Skull,Archer,Angler,Explorer`**
