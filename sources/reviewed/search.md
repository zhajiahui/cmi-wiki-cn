适用于 CMI **9.7.12.0** 及以上版本。

该指令用于在玩家背包和末影箱中查找指定物品，也可以查询玩家的游戏模式、飞行模式等状态。

![](https://www.zrips.net/wp-content/uploads/2025/04/searchSearching.png)

结果会区分物品所在位置，包括背包、末影箱，以及其中的潜影盒和收纳袋。在潜影盒或收纳袋里找到物品时，结果窗口也会标示。下图是同一名玩家的查找结果：

![](https://www.zrips.net/wp-content/uploads/2025/04/searchList.png)

示例中，末影箱内共有 17 个，普通背包内共有 7 个，分散在潜影盒或收纳袋中。结果只提供大致位置，具体物品还需要自行查找。

## 用法示例

```text
/cmi search diamondsword
```

按材质查找所有玩家背包和末影箱中的钻石剑，先查在线玩家，再查离线玩家。自定义名称、描述和附魔不影响此项匹配。

```text
/cmi search diamondsword;n{Some_Custom_Name}
```

按名称查找，格式见[一行创建物品](https://www.zrips.net/cmi/commands/icwol/)。名称只需包含指定文字，无需完整匹配。查找时忽略颜色，只比较文字。

```text
/cmi search diamondsword;l{Some_Custom_Lore}
```

按物品描述查找。同样只需描述中包含指定文字，无需完整匹配。

```text
/cmi search diamondsword;e{sharpness:5}
```

指定附魔后，除了检查材质，还会要求钻石剑具有锋利 5 或更高等级。可以同时指定多个附魔，例如 `diamondsword;e{sharpness:3,luck:2}`。

```text
/cmi search diamondsword;cm{123456}
```

按指定的自定义模型数据查找。

```text
/cmi search diamondsword:3
```

按数量查找，会统计整个背包中的数量，并匹配超过指定数量的结果。返回的是背包或末影箱这一完整位置中的物品总量，可能包含潜影盒或收纳袋里的物品。这与单纯查找符合条件的物品略有不同。

```text
/cmi search hand
```

以主手物品为样本查找。匹配条件取决于样本的复杂程度：有自定义名称就比较名称，有附魔就比较附魔；若是普通物品，则只比较材质。

```text
/cmi search lead;e{thorns:1} diamondsword;e{sweeping:1}
```

用空格分开各个物品条件，可以同时查找多种物品。示例查找带指定附魔的拴绳和钻石剑。

同时查找多种物品时，结果只显示找到的数量，不区分具体是哪种物品。若同时查找“指定附魔的钻石剑”和“所有钻石剑”，同一物品可能重复匹配，结果数量可能高于实际物品数量。

```text
/cmi search oversize
```

查找堆叠数量超过该物品默认上限的物品堆。

```text
/cmi search results
```

显示当前或上一次查找的结果。

```text
/cmi search cancel
```

取消正在进行的查找。

### 自定义物品匹配条件

以手持物品查找时，可以指定只比较部分属性。例如，`/cmi search hand material name` 只比较材质和名称，忽略其他属性。

`/cmi search hand enchant` 只比较附魔，附魔书也会被视为有效结果。

可用条件：`material, name, lore, enchant, modeldata`。

## 其他查询选项

```text
/cmi search survival/cmi search creative/cmi search spectator/cmi search adventure
```

查找处于指定游戏模式的玩家。

```text
/cmi search god
```

查找开启无敌模式的玩家。

```text
/cmi search fly
```

查找有飞行权限的玩家。

```text
/cmi search maxhp:21
```

查找最大生命值达到指定值或更高的玩家。数值可以自行指定；玩家默认生命值为 20。
