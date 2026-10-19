---
title: 优先级与继承
source_url: https://worldguard.enginehub.org/en/latest/regions/priorities/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 优先级与继承 { #priority-and-inheritance }

如[快速入门](quick-start.md)所述，区域可以重叠。一般情况下，玩家必须拥有**所有**重叠区域的建造权限，才能在重叠位置建造。但利用优先级和继承，可以不必满足这一规则。

## 优先级 { #priorities }

每个区域的默认优先级为 0，可改为正数或负数。数字越大，优先级越高。有效范围为 -2147483648 到 2147483647，包括两个端点；实际使用时通常会选择 -2、10、15 或 100 等更合理的数字。

- 对于成员关系及谁可以建造：某个位置有多个重叠区域时，只考虑优先级最高的区域。

- 对于[区域旗标](flags.md)，使用已定义该旗标且优先级最高的区域。

用 `/rg setpriority` 设置优先级：

```text
/rg setpriority example 5
```

示例：在出生点创建“pub”区域，只允许“pub group”中的人建造，尽管出生点已有允许“builders”建造的区域

如果只是创建一个与 spawn 重叠的区域，玩家就必须同时属于“pub”*和*“builders”，才能在酒馆内建造。因此，应把 pub 区域的优先级调高。

1. 选中酒馆范围。

2. 创建“pub”区域：



   ```text
   /rg define pub
   ```

3. 将“pub”优先级提高到大于 0 的数值，超过 spawn 区域的优先级：



   ```text
   /rg setpriority pub 10
   ```

示例：在允许 PvP 的“arena”区域中，创建一个禁止 PvP 的特殊“heal”区域

这里的目标是覆盖竞技场中的 `pvp = allow` 旗标。

1. 选中治疗区域。

2. 创建“heal”区域：



   ```text
   /rg define heal
   ```

1. 将 `pvp` 设为 `deny`：



   ```text
   /rg flag heal pvp deny
   ```

1. 将“heal”优先级提高到大于 0 的数值，超过 arena 区域的优先级：



   ```text
   /rg setpriority heal 10
   ```

注意：旗标冲突时，*deny* 会覆盖 *allow*，因此实际上不必提高“heal”的优先级。但如果想用 *allow* 覆盖 *deny*，就必须调整优先级。

## 继承 { #inheritance }

继续上面的酒馆示例：如果希望 builders 和 pub 成员*都*能在酒馆内建造，该怎么办？可以把 builders 组添加到 pub 区域，也可以让 pub 从 spawn 区域*继承*成员。

为区域指定父区域后：

- 它会继承父区域的成员和所有者

- *如果*子区域未定义某个旗标，就会继承父区域的该旗标

这适用于：

- 一个主区域及其内部的小地块

- 创建模板区域，让子区域继承旗标

每个区域最多只能有一个父区域。使用 `/rg setparent` 设置：

```text
/rg setparent region_name parent_name
```

不指定父区域名称即可取消父区域：

```text
/rg setparent region_name
```

WorldGuard 会检测并阻止循环继承。

示例：创建一个内部有多个地块的“mall”

创建 mall、plot1 和 plot2 后，为地块设置父区域：

```text
/rg setparent plot1 mall
/rg setparent plot2 mall
```

假设有一个“mall_owners”组，将它添加到 mall 区域：

```text
/rg addowner mall g:mall_owners
```

商场所有者便可在地块内建造。

如果给某个地块添加成员或所有者，该玩家只能在自己的地块内建造：

```text
/rg addowner plot1 sk89q
```

!!! note "注意"

    活塞等非玩家关联对象也可以是区域成员，成员继承并非只适用于玩家。因此，父区域内的活塞也能将方块推入子区域。

### 模板区域 { #template-regions }

如前文所述，子区域会继承父区域的旗标，因此父区域可以作为所有子区域的基础模板。

但你可能希望模板区域*没有实际空间范围*，因为它并不用于保护任何地方。一种办法是创建没有实际大小的“全局区域”：在创建区域命令中加入 `-g` 即可：

```text
/rg define -g plot_template
```

示例：让商场示例中的地块继承“plot_template”区域

创建地块模板区域：

```text
/rg define -g plot_template
```

让地块继承地块模板：

```text
/rg setparent plot1 plot_template
/rg setparent plot2 plot_template
```

让地块模板继承 mall：

```text
/rg setparent plot_template mall
```

假设想允许玩家使用商场内的任意箱子，*但地块内的除外*。先在 mall 上设置 `chest-access`：

```text
/rg flag mall chest-access allow
```

接下来需要禁止所有地块的 `chest-access`。好在可以直接使用地块模板：

```text
/rg flag plot_template chest-access deny
```

### 继承与优先级的关系 { #inheritance-versus-priorities }

优先级更高的父区域会覆盖子区域。因此，只有子区域优先级不低于父区域时，继承才会正常工作。

## 区域组与重叠区域 { #region-groups-and-overlapping-regions }

如前所述，可以让旗标只针对特定区域组：

```text
/rg flag mall pvp -g nonmembers deny
```

只有一个区域时，很容易判断哪些玩家是成员。但区域重叠时就没那么直观：玩家是否只需属于其中任意一个区域？

答案是否定的。玩家必须属于*设置该旗标的区域*。

例如，假设两个区域重叠：

- Spawn 设置 `pvp -g nonmembers deny`，没有成员

- Market 的成员包含“sk89q”

由于 sk89q 不是 spawn 的成员，他仍会被禁止 PvP。

### 存在继承关系时 { #in-the-context-of-inheritance }

区域指定父区域后，会同时继承旗标和成员列表，因此玩家*也可以*属于它的某个子区域。

例如，假设有两个区域：

- Market 设置 `pvp -g nonmembers deny`，没有成员

- Shop1 的成员包含“sk89q”，并且**继承** market

sk89q 是成员吗？是的，因此允许 sk89q 进行 PvP。

!!! note "注意"

    如前所述，父区域的优先级**不应**高于子区域，否则无法正确工作。父区域会覆盖子区域，进而禁止 sk89q 进行 PvP。
