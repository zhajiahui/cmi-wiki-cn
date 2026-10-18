Residence 市场内置领地告示牌功能，玩家无需输入命令即可购买或租用领地。先创建领地，将其加入市场，再放置告示牌，在第一行写上 `[market]` 即可。

## 创建带告示牌的市场领地

用下面的命令将领地加入出租市场：

`/res market rentable [residenceName] [costToRent] [intervalInDays] (allowRenewing) (stayInMarket) (allowAutoPay)`

例如，执行 `/res market rentable MyHouse 1000 7`，会将 MyHouse 挂到市场上，租金为每周 1000。

如果告示牌放在领地内，只需将第一行设为 `[market]`，其他内容会自动填入，之后即可点击操作。

如果告示牌放在领地外，需要在第二、第三行填写领地名。领地名可以写在第二、第三、第四行；从第一处可填写的位置开始，一行写不下时接着写到下一行。

## 指令和权限

更多领地市场命令见[指令列表](https://www.zrips.net/residence/commands/)。

相关权限见[权限节点](https://www.zrips.net/residence/permissions/)。
