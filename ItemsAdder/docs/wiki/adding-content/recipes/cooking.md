---
title: "烹饪"
source_url: "https://wiki.itemsadder.com/adding-content/recipes/cooking"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 烹饪

ItemsAdder 允许为你的物品添加自定义熔炉配方，将它们变成其他东西。

**注意：**熔炼权限无法可靠执行，因为无法准确判断是哪位玩家放入了物品。\
例如，机器从容器中抽取物品后，就无法追溯最初将物品放入第一个漏斗的玩家。

如果需要权限限制，应使用合成配方实现。

## 示例

添加烹饪配方时，在 `recipes` 下添加 `cooking` 配置节。名称通常不影响功能，不过建议使用产出物品的名称。

```yaml
recipes:
  cooking:
    cooked_sausage:
      permission: itemsadder.cooked_sausage
      ingredient:
        item: itemsadder:sausage
      machines:
      - FURNACE
      - BLAST_FURNACE
      exp: 1
      cook_time: 200
      result:
        item: itemsadder:cooked_sausage
        amount: 1
```

本例创建了名为 `cooked_sausage` 的 `cooking` 配方。

* `item` 是应该被烹饪的物品。可以通过各自的命名空间使用原版 Minecraft 和自定义物品。
* `machines` 是一个允许熔炼/烹饪该物品的熔炉类型列表。支持的类型有 `FURNACE`、`BLAST_FURNACE` 和 `SMOKER`。
* `exp` 定义了玩家取出物品时获得的经验量。
* `cook_time` 是物品处理所需的时间。时间以刻为单位，这意味着 20 = 1 秒。
* `result` 包含 `item` 和 `amount` 选项，定义了返回的物品和数量。可以通过各自的命名空间使用原版 Minecraft 和自定义物品。
