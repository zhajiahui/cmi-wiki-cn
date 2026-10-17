![](https://www.zrips.net/wp-content/uploads/2019/02/2018-03-22_13-57-38.gif)

动态告示牌会根据配置更新文本。它可以向每位玩家显示各自的信息，也可以向所有人显示相同的公共信息。

例如，用对应占位符显示玩家余额，或显示玩家当前手持物品的价格。文本不限于四行，超出四行的部分会自动滚动。

先放置一块告示牌，原有文字不影响创建，也可以完全留空。

[![](https://www.zrips.net/wp-content/uploads/2019/02/dsign1.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign1.jpg)

看着告示牌执行 `/cmi dsign new didly`。

周围会出现粒子，标示更新区域。只有玩家站在这个区域里，告示牌才会更新；站在告示牌另一侧的玩家看不到文本，无需为他们更新，从而减少服务器负担。

[![dsign2](https://www.zrips.net/wp-content/uploads/elementor/thumbs/dsign2-o3lnvg3o2f7chcsj5ioj1un8xdwhhe606dm19kpeyo.jpg "dsign2")](https://www.zrips.net/wp-content/uploads/2019/02/dsign2.jpg) [![](https://www.zrips.net/wp-content/uploads/2019/02/dsign3-1024x446.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign3.jpg)

执行创建指令后，聊天中会出现类似下面的消息：

[![](https://www.zrips.net/wp-content/uploads/2019/02/dsign4.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign4.jpg)

下面添加文本，显示玩家手持物品的价格，效果与页首动画一致。

点击 `[+]`，输入第一行：

`%cmi_iteminhand_realname%`

该占位符显示玩家当前手持物品的名称。回车后，再依次添加两行：

`%cmi_iteminhand_amount%`

`&7Worth: %cmi_iteminhand_worth%`

结果如下：

[![](https://www.zrips.net/wp-content/uploads/2019/02/dsign6.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign6.jpg) [![](https://www.zrips.net/wp-content/uploads/2019/02/dsign7-1024x367.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign7.jpg)

告示牌默认每 5 秒更新一次。这个例子可以改成更短的间隔：点击 `<Open gui>`，在打开的界面中找到更新间隔按钮，将其改为 1 秒。

[![](https://www.zrips.net/wp-content/uploads/2019/02/dsign8.jpg)](https://www.zrips.net/wp-content/uploads/2019/02/dsign8.jpg)

告示牌会自动为每位玩家更新。

还可以关闭个性化显示，让所有人看到相同的信息。显示在线人数等公共信息时，这种方式效率更高。

更新范围也可以调整，适合告示牌所在空间较宽或较窄时使用，避免不必要的更新。默认范围通常已经足够。

动画中的最后一行来自另一项功能：[交互指令](/cmi/commands/interactive-commands/)。
