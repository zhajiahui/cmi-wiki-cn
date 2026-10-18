# Residence 原文核对备注

此文件是译者的核对记录，不进入 Wiki 正文。正文保留各原文页面的适用条件、命令参数和示例。

1. **页面年代不同。** 官网首页虽然在 2025 年修改，支持版本仍列到 Minecraft 1.17；指令、权限和标志页面最后修改于 2019 年。未将其改写为当前所有版本的通用说明。
2. **选区工具不一致。** “创建领地”页写默认木锄，指令页写默认木斧。译文分别保留；创建页原有 `/res tool` 查询方法也已保留。
3. **市场命令存在两套写法。** 市场页使用 `(allowRenewing) (stayInMarket) (allowAutoPay)`，旧指令列表使用 `repeat:t/f`。均按所属页面原样保留，未拼接为新语法。
4. **市场告示牌行数含糊。** 原文先说第二、第三行，又写第二、第三、第四行，并说从第一行开始续写。译文按上下文表述为从可填写领地名的位置开始换行，仍保留两处行数说明。
5. **权限说明疑似复制错误。** `residence.bypass.tp` 被解释为绕过 `command` 标志；按原文保留，没有改成推测的 `tp`。
6. **标志页示例与参数说明不一致。** `/res pset` 的参数说明与带领地名的例子不完全一致；原文还在 `[FlagName_]` 中带下划线。译文保留对应技术字符串。
7. **标志值说明含糊。** 原文说 `enable`、`disable` 始终需要第二个标志设置，没有进一步解释。译文未扩写其机制。`wspeed1` 和 `wspeed2` 都写 `%1`，按原文保留。
8. **战争冷却的注释与示例值矛盾。** 注释写默认 79200 秒、22 小时，示例中的 `Cooldown` 和 `PlayerCooldown` 却均为 120。代码和注释完整保留。
9. **API 包含旧版接口和不完整片段。** 原文使用 `CustomEventListener`、`Event.Type.CUSTOM_EVENT`；部分片段缺少变量名，或将参数类型与变量同时写入调用表达式。所有 21 个 API 代码块原样保留，未声称能够直接编译。
10. **原文重复与拼写。** 首页“租期结束恢复区域”和“多层子领地”各重复一次，译文保留。首页的 `Couldron` 按原名保留；标志说明中的 `WordEdit` 统一写为同站其他段落使用的 `WorldEdit`，不改变其所指项目。

来源：[首页](https://www.zrips.net/residence/)、[创建领地](https://www.zrips.net/residence/creating-residence/)、[市场](https://www.zrips.net/residence/market/)、[指令](https://www.zrips.net/residence/commands/)、[权限](https://www.zrips.net/residence/permissions/)、[标志](https://www.zrips.net/residence/flags/)、[战争](https://www.zrips.net/residence/raid/)、[API](https://www.zrips.net/residence/api/)。
