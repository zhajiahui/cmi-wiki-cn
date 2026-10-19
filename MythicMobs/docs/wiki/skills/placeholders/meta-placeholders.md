---
title: 元占位符
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholders/meta-placeholders
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 元占位符

可以在占位符末尾追加与其类型对应的关键字（下文称为 `meta keywords`），以修改占位符的返回值和返回类型。

```yaml
<some.placeholder.{keywords}>
```

每个关键字都有一个

- `Input Type`，这是关键字适用的占位符类型
- `Output Type`，这是可以从关键字的返回值创建的占位符类型

> 元关键字中的任何位置都支持占位符，因此每个关键字本身也可以是另一个待解析的占位符

---

```yaml
<caster.name.capitalize>
```

> `<caster.name>` 返回 STRING
> 在 String 类型的所有关键字中，我们使用的是 `capitalize` 关键字，它的输出是 String 类型。这意味着
>

> - 它应用于字符串值
> - 它对其值进行某种形式的转换（在本例中，将字符串的每个字符大写）
> - 它返回一个字符串值

```yaml
<caster.name.size>
```

> `<caster.name>` 返回 STRING
> 在 String 类型的所有关键字中，我们使用的是 `size` 关键字，它的输出是 Integer 类型。这意味着
>

> - 它应用于字符串值
> - 它对其值进行某种形式的转换（在本例中，返回字符串的长度）
> - 它返回一个整数值

---

由于每个元关键字都有特定的输入类型和输出类型，因此可以将它们*串联*起来：每个关键字转换前一个值，再将结果传递给下一个关键字，从而获得组合效果

```yaml
<skill.var.exampleString.substring{from=0;to=9}.size.add{amount=1}>
```

> 在 String 类型的所有关键字中，我们使用的是 `substring` 关键字，它的输出是 String 类型。这意味着
>

> - 它应用于字符串值
> - 它会转换该值（此处是提取字符串的前 10 个字符）
> - 它返回一个字符串值
>

> 在 String 类型的所有关键字中，我们使用的是 `size` 关键字，它的输出是 Integer 类型。这意味着
>

> - 它作用于字符串值（即 `substring` 关键字刚返回的值）
> - 它对其值进行某种形式的转换（在本例中，返回字符串的长度，我们知道该长度将在 0 和 10 之间）
> - 它返回一个整数值
>

> 在 Integer 类型的所有关键字中，我们使用 `add` 关键字，它的输出是 Integer 类型。这意味着
>

> - 它作用于整数值（即 `size` 关键字刚返回的值）
> - 它会转换该值（此处是将整数的值加上 1）
> - 它返回一个整数值

1. [通用元关键字](meta-placeholders.md#universal-meta-keywords)
2. [整数元关键字](meta-placeholders.md#integer-meta-keywords)
3. [浮点数元关键字](meta-placeholders.md#float-meta-keywords)
4. [长整数元关键字](meta-placeholders.md#long-meta-keywords)
5. [双精度浮点数元关键字](meta-placeholders.md#double-meta-keywords)
6. [布尔元关键字](meta-placeholders.md#boolean-meta-keywords)
7. [字符串元关键字](meta-placeholders.md#string-meta-keywords)
8. [集合元关键字](meta-placeholders.md#set-meta-keywords)
9. [位置元关键字](meta-placeholders.md#location-meta-keywords)
10. [向量元关键字](meta-placeholders.md#vector-meta-keywords)
11. [列表元关键字](meta-placeholders.md#list-meta-keywords)
12. [映射元关键字](meta-placeholders.md#map-meta-keywords)
13. [时间元关键字](meta-placeholders.md#time-meta-keywords)
14. [物品元关键字](meta-placeholders.md#item-meta-keywords)

# 通用元关键字 {#universal-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .cache |  | 根据输入值及其后使用的关键字，在首次解析此占位符时缓存结果；此后每次解析都直接返回缓存值 |
| .formatted | STRING | 返回更便于阅读的输入值表示 |
| .typename | STRING | 返回上一个值的返回类型名称 |
| .toInteger | INTEGER | 不进行任何特定运算，将该值转换为 Integer，以便继续链式调用 Integer 元关键字 |
| .toFloat | FLOAT | 不进行任何特定运算，将该值转换为 Float，以便继续链式调用 Float 元关键字 |
| .toLong | LONG | 不进行任何特定运算，将该值转换为 Long，以便继续链式调用 Long 元关键字 |
| .toDouble | DOUBLE | 不进行任何特定运算，将该值转换为 Double，以便继续链式调用 Double 元关键字 |
| .toBoolean | BOOLEAN | 不进行任何特定运算，将该值转换为 Boolean，以便继续链式调用 Boolean 元关键字 |
| .toString | STRING | 不进行任何特定运算，将该值转换为 String，以便继续链式调用 String 元关键字 |
| .toLocation | LOCATION | 不进行任何特定运算，将该值转换为 Location，以便继续链式调用 Location 元关键字 |
| .toVector | VECTOR | 不进行任何特定运算，将该值转换为 Vector，以便继续链式调用 Vector 元关键字 |
| .toList | LIST | 不进行任何特定运算，将该值转换为 List，以便继续链式调用 List 元关键字 |
| .toSet | SET | 不进行任何特定运算，将该值转换为 Set，以便继续链式调用 Set 元关键字 |
| .toMap | MAP | 不进行任何特定运算，将该值转换为 Map，以便继续链式调用 Map 元关键字 |
| .toTime | TIME | 不进行任何特定运算，将该值转换为 Time，以便继续链式调用 Time 元关键字 |

> [转到说明>>](meta-placeholders.md)

# Integer 元关键字 {#integer-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .add{amount=[Integer]} | INTEGER | 将该值与指定 Integer 相加 |
| .sub{amount=[Integer]} | INTEGER | 将该值减去指定 Integer |
| .mul{amount=[Integer]} | INTEGER | 将该值与指定 Integer 相乘 |
| .div{amount=[Integer]} | INTEGER | 将该值除以指定 Integer |
| .abs | INTEGER | 该值的绝对值 |
| .min{amount=[Integer]} | INTEGER | 返回该值与 `amount` 中较大的一个，因此 `amount` 作为下限 |
| .max{amount=[Integer]} | INTEGER | 返回该值与 `amount` 中较小的一个，因此 `amount` 作为上限 |
| .clamp{min=[Integer];max=[Integer]} | INTEGER | 将该值限制在 `min` 与 `max` 之间。任一边界均可省略，默认使用 Integer 的最小值和最大值。例如：`<caster.var.spawn_chance.clamp{min=0;max=100}>` |

> [转到说明>>](meta-placeholders.md)

# Float 元关键字 {#float-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .add{amount=[Float]} | FLOAT | 将该值与指定 Float 相加 |
| .sub{amount=[Float]} | FLOAT | 将该值减去指定 Float |
| .mul{amount=[Float]} | FLOAT | 将该值与指定 Float 相乘 |
| .div{amount=[Float]} | FLOAT | 将该值除以指定 Float |
| .abs | FLOAT | 该值的绝对值 |
| .min{amount=[Float]} | FLOAT | 返回该值与 `amount` 中较大的一个，因此 `amount` 作为下限 |
| .max{amount=[Float]} | FLOAT | 返回该值与 `amount` 中较小的一个，因此 `amount` 作为上限 |
| .clamp{min=[Float];max=[Float]} | FLOAT | 将该值限制在 `min` 与 `max` 之间。任一边界均可省略，默认使用 Float 的最小值和最大值。例如：`<caster.var.spawn_chance.clamp{min=0;max=100}>` |
| .round | INTEGER | 将该值舍入为最接近的 Integer |
| .precision{amount=[Integer]} | FLOAT | 返回相同的浮点值，但限制最大小数精度；多余的小数位使用 HALF_UP 方式舍入 |

> [转到说明>>](meta-placeholders.md)

# Long 元关键字 {#long-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .add{amount=[Long]} | LONG | 将该值与指定 Long 相加 |
| .sub{amount=[Long]} | LONG | 将该值减去指定 Long |
| .mul{amount=[Long]} | LONG | 将该值与指定 Long 相乘 |
| .div{amount=[Long]} | LONG | 将该值除以指定 Long |
| .abs | LONG | 该值的绝对值 |
| .min{amount=[Long]} | LONG | 返回该值与 `amount` 中较大的一个，因此 `amount` 作为下限 |
| .max{amount=[Long]} | LONG | 返回该值与 `amount` 中较小的一个，因此 `amount` 作为上限 |
| .clamp{min=[Long];max=[Long]} | LONG | 将该值限制在 `min` 与 `max` 之间。任一边界均可省略，默认使用 Long 的最小值和最大值。例如：`<caster.var.spawn_chance.clamp{min=0;max=100}>` |

> [转到说明>>](meta-placeholders.md)

# Double 元关键字 {#double-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .add{amount=[Double]} | DOUBLE | 将该值与指定 Double 相加 |
| .sub{amount=[Double]} | DOUBLE | 将该值减去指定 Double |
| .mul{amount=[Double]} | DOUBLE | 将该值与指定 Double 相乘 |
| .div{amount=[Double]} | DOUBLE | 将该值除以指定 Double |
| .abs | DOUBLE | 该值的绝对值 |
| .min{amount=[Double]} | DOUBLE | 返回该值与 `amount` 中较大的一个，因此 `amount` 作为下限 |
| .max{amount=[Double]} | DOUBLE | 返回该值与 `amount` 中较小的一个，因此 `amount` 作为上限 |
| .clamp{min=[Double];max=[Double]} | DOUBLE | 将该值限制在 `min` 与 `max` 之间。任一边界均可省略，默认使用 Double 的最小值和最大值。例如：`<caster.var.spawn_chance.clamp{min=0;max=100}>` |
| .round | LONG | 将该值舍入为最接近的 Long |
| .precision{amount=[Integer]} | DOUBLE | 返回相同的浮点值，但限制最大小数精度；多余的小数位使用 HALF_UP 方式舍入 |

> [转到说明>>](meta-placeholders.md)

# Boolean 元关键字 {#boolean-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .inverse | BOOLEAN | 该值的反值 |
| .number | INTEGER | 将该值表示为 0（false）或 1（true） |
| .yesno | STRING | 将该值表示为 no（false）或 yes（true） |
| .union.{Boolean} | BOOLEAN | 与指定 Boolean 进行逻辑 OR（或）运算 |
| .intersection.{Boolean} | BOOLEAN | 与指定 Boolean 进行逻辑 AND（与）运算 |
| .difference.{Boolean} | BOOLEAN | 该值为 true 且参数为 false 时返回 True |

> [转到说明>>](meta-placeholders.md)

# String 元关键字 {#string-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .size | INTEGER | 字符串的长度 |
| .uppercase | STRING | 将字符串转换为大写 |
| .lowercase | STRING | 将字符串转换为小写 |
| .capitalize | STRING | 将字符串的首字符转换为大写 |
| .trim | STRING | 去除字符串开头和结尾的空格 |
| .replace{from=old;to=new} | STRING | 将字符串中出现的 `old` 替换为 `new` |
| .remove{value=text} | STRING | 移除字符串中出现的 `text` |
| .contains{value=text} | BOOLEAN | 字符串是否包含 `text` |
| .substring{from=[Integer];to=[Integer]} | STRING | 从 `from` 索引到 `to` 索引的子字符串 |
| .shift{amount=[Integer]} | STRING | 移除开头的 `Integer` 个字符 |
| .split{regex=[String];with=[String]} | STRING | 按 `regex` 拆分字符串，再使用 `with` 字符串连接 |
| .indexof{value=[String]} | INTEGER | `value` 文本首次出现的索引 |
| .lastindexof{value=[String]} | INTEGER | `value` 文本最后一次出现的索引 |
| .startswith{value=[String]} | BOOLEAN | 字符串是否以 `value` 开头 |
| .endswith{value=[String]} | BOOLEAN | 字符串是否以 `value` 结尾 |
| .append{value=[String]} | STRING | 将 `value` 追加到字符串末尾 |
| .prepend{value=[String]} | STRING | 将 `value` 添加到字符串开头 |
| .insert{index=[Integer];value=[String]} | STRING | 在指定 `index` 处插入 `value` |
| .regex{regex=[String]} | BOOLEAN | 字符串是否匹配 `regex` 模式 |
| .{index} | STRING | 返回指定 `index` 处的字符 |

> [转到说明>>](meta-placeholders.md)

# Set 元关键字 {#set-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .size | INTEGER | 集合中的元素数量 |
| .join{with=[String]} | STRING | 使用 `with` 分隔符连接所有元素 |
| .contains{value=[String]} | BOOLEAN | 集合是否包含指定 `value` |

> [转到说明>>](meta-placeholders.md)

# Location 元关键字 {#location-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .x | DOUBLE | X 坐标 |
| .y | DOUBLE | Y 坐标 |
| .z | DOUBLE | Z 坐标 |
| .world | STRING | 世界名称 |
| .yaw | DOUBLE | yaw（偏航角） |
| .pitch | DOUBLE | pitch（俯仰角） |
| .coords | LIST | 包含 X、Y、Z 坐标的列表。需要对其调用 .toVector 时也可使用 |

> [转到说明>>](meta-placeholders.md)

# Vector 元关键字 {#vector-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .x | DOUBLE | X 分量 |
| .y | DOUBLE | Y 分量 |
| .z | DOUBLE | Z 分量 |
| .normalized | VECTOR | 归一化后的向量 |
| .length | DOUBLE | 向量的长度（模） |
| .add{amount=[Vector]} | VECTOR | 加上另一个向量 |
| .sub{amount=[Vector]} | VECTOR | 减去另一个向量 |
| .mul{amount=[Vector]} | VECTOR | 将该向量与另一个向量相乘 |
| .div{amount=[Vector]} | VECTOR | 将该向量除以另一个向量 |
| .rotate{axis=[String];angle=[Double]} | VECTOR | 将该向量绕 `axis` 轴旋转 `angle` 弧度 |

> [转到说明>>](meta-placeholders.md)

# List 元关键字 {#list-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .size | INTEGER | 列表中的元素数量 |
| .first | STRING | 列表的第一个元素 |
| .last | STRING | 列表的最后一个元素 |
| .reverse | LIST | 反转后的列表 |
| .sort | LIST | 按字母顺序排序后的列表 |
| .sortnum | LIST | 按数值排序后的列表。列表中的每个元素都必须是数字 |
| .shuffle | LIST | 打乱列表，随机排列其中的元素 |
| .get{index=[Integer]} | STRING | 指定 `index` 处的元素 |
| .join{with=[String]} | STRING | 使用 `with` 分隔符连接元素 |
| .contains{value=[String]} | BOOLEAN | 列表是否包含 `value` |
| .maxnumber | DOUBLE | 列表中的最大数值 |
| .minnumber | DOUBLE | 列表中的最小数值 |
| .indexof{value=[String]} | INTEGER | `value` 首次出现的索引 |
| .lastindexof{value=[String]} | INTEGER | `value` 最后一次出现的索引 |
| .slice{from=[Integer];to=[Integer]} | LIST | 列表从 `from` 到 `to` 的切片 |
| .slicefrom{from=[Integer]} | LIST | 列表从 `from` 到末尾的切片 |
| .sliceto{to=[Integer]} | LIST | 列表从开头到 `to` 的切片 |
| .append{value=[String]} | LIST | 将 `value` 添加到列表末尾 |
| .prepend{value=[String]} | LIST | 将 `value` 添加到列表开头 |
| .insert{index=[Integer];value=[String]} | LIST | 在指定 `index` 处插入 `value` |
| .remove{index=[Integer]} | LIST | 移除指定 `index` 处的值 |
| .{index} | STRING | 指定 `index` 处的元素 |

> [转到说明>>](meta-placeholders.md)

# Map 元关键字 {#map-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .size | INTEGER | 键值对数量 |
| .keys | LIST | 所有键的列表 |
| .values | LIST | 所有值的列表 |
| .get{key=[String]} | STRING | 指定 `key` 关联的值 |
| .{key} | STRING | 指定 `key` 关联的值 |
| .sortByValue | LIST | 按关联值排序的键列表（所有值都是数字时按数值排序，否则按字母顺序排序） |

> [转到说明>>](meta-placeholders.md)

# Time 元关键字 {#time-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .delta{value=[Long]} | INTEGER | 该值的时间与给定 `value` 时间戳之间的差值 |
| .formatted{value=[String]} | STRING | 使用指定格式表示日期/时间。格式可使用 Java 函数 [ZoneOffset.of](https://docs.oracle.com/javase/8/docs/api/java/time/ZoneOffset.html#of-java.lang.String-) 接受的任意模式 |
| .duration | STRING | 将 Time 视为原始的“毫秒数”，并显示合计的秒、分、时、天、月和年数。可用于倒计时等场景，尤其适合与 `.delta` 元关键字配合使用 |

> [转到说明>>](meta-placeholders.md)

# Item 元关键字 {#item-meta-keywords}

| 占位符 | 返回类型 | 返回值 |
| --- | --- | --- |
| .withType{type=[String]} | ITEM | 返回同一物品，但将其类型设为指定的 `type` 材质（不区分大小写，必须匹配有效的 `Material` 枚举） |
| .withDurability{durability=[Integer]} | ITEM | 返回同一物品，但将其耐久度设为指定整数 `durability` |
| .withMaxDurability{durability=[Integer]} | ITEM | 返回同一物品，但将其最大耐久度设为指定整数 `durability` |
| .withLore{lore=[List]} | ITEM | 返回同一物品，但将其描述设为指定的字符串列表。 |
| .withName{name=[String]} | ITEM | 返回同一物品，但将其显示名称设为 `name` |
| .withMythicType{type=[String]} | ITEM | 返回同一物品，但将其持久化的 "Mythic Type" 设为 `type`，使 Mythic 将修改后的物品视为 `type` 对应的 Mythic 物品 |
| .withEnchants{enchant=[Map]} | ITEM | 返回同一物品，但用映射中提供的附魔替换原附魔。应用新附魔前会移除全部原有附魔 |
| .withCustomData{namespace=[String];key=[String];value=[String]} | ITEM | 返回同一物品，但带有自定义持久化数据（将 `value` 存储在 `namespace:key` 下） |
| .withAmount{amount=[Integer]} | ITEM | 返回同一物品，但将其堆叠数量设为 `value` |
| .withUUID{uuid=[String]} | ITEM | 返回同一物品，但将其 UUID NBT 设为指定值 |
| .withTimestamp{timestamp=[Long]} | ITEM | 返回同一物品，但将其时间戳 NBT 设为指定整数值 |
| .withCustomModelData{value=[String]} | ITEM | 返回同一物品，但将其 Custom Model Data 设为 `value` |
| .withModel{namespace=[String];value=[String]} | ITEM | 返回同一物品，但将其物品模型设为 `{namespace}:{path}` |
| .type | STRING | 物品类型的字符串表示（Material 名称） |
| .durability | INTEGER | 物品的当前耐久度值 |
| .maxDurability | INTEGER | 物品的最大耐久度值 |
| .lore | LIST | 物品描述，以字符串列表表示 |
| .name | STRING | 物品的显示名称。 |
| .mythicType | STRING | 物品持久化的 "Mythic Type" 值（若已设置） |
| .enchants | MAP | 物品上所有附魔的映射 |
| .getCustomData{namespace=[String];key=[String]} | STRING | 存储在物品自定义持久化数据 `{namespace}:{key}` 下的字符串值 |
| .customModelData | INTEGER | 物品的 Custom Model Data 值 |
| .model | STRING | 物品的模型标识符，格式为 `namespace:path` |
| .amount | INTEGER | 物品的堆叠数量 |

> [转到说明>>](meta-placeholders.md)
