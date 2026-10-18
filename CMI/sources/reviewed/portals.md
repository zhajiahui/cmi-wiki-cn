![](https://www.zrips.net/wp-content/uploads/2022/09/giphy.webp)

CMI 的传送门功能可以创建传送门，在玩家穿过时执行命令。

传送门支持[专用命令](https://www.zrips.net/cmi/commands/specialized/)。

传送门无需设置传送目标点，也可以只依靠命令运作。创建新传送门前，需要先选择一个区域。传送门可以从多种粒子效果中选择一种来显示，也可以不显示粒子。此功能支持 BungeeCord，可以将传送目标点设在同一群组网络中的其他服务器上。

## 创建传送门

要**创建**传送门，需要一把**木锹**（CMI 默认的选区工具），以及 `cmi.command.portals` 和 `cmi.select` 权限。

**1.** 选择传送门所在的区域。选中的区域会用粒子标记。

![](https://www.zrips.net/wp-content/uploads/2022/09/PortalSelected-1024x576.png)

**2.** 选好区域后，使用 `/cmi portals new [portalName]` 创建传送门。   
例如，要创建名为 **Test1** 的传送门，执行 `/cmi portals new Test1`。  
**3.** 可以选择设置传送门的目标点。聊天栏中会出现一条可点击的消息。

![](https://www.zrips.net/wp-content/uploads/2019/02/portals2.png)

**4.** 输入 `/cmi portals edit Test1`，通过图形界面编辑传送门设置。在界面中可以：

- 启用或禁用传送门。
- 开启或关闭粒子显示。
- 更改粒子类型。
- 更改粒子数量。
- 更改侧边粒子收缩的百分比。
- 更改粒子激活范围，单位为方块；玩家进入该范围后才会显示粒子。
- 向没有 `cmi.command.portal.[portalname]` 权限的玩家显示粒子。
- 更改粒子颜色（仅适用于红石粉尘粒子）。
- 更改粒子大小（仅适用于红石粉尘粒子）。
- 在没有有效传送位置时执行传送门命令。
- 编辑传送门命令。
- 设置玩家是否需要 `cmi.command.portal.[portalname]` 权限才能使用传送门。
- 在玩家没有 `cmi.command.portal.[portalname]` 权限时给予提示。
- 阻止没有 `cmi.command.portal.[portalname]` 权限的玩家使用传送门。
- 设置传送门外的安全位置。
- 设置传送门的传送位置。
- 传送到传送门的目标位置。
- 传送到传送门所在的位置。
- 用当前选区重新定义传送门区域。
- 删除传送门。
![](https://www.zrips.net/wp-content/uploads/2022/09/PortalGUI.png)

**5.** 要**添加命令**，点击界面中的附魔书物品。

![](https://www.zrips.net/wp-content/uploads/2019/02/portals5.png)

**6.** 点击绿色的 `[+]`，添加一条新命令，然后在聊天栏中输入命令。*（支持专用命令。）*

命令开头不要加 `/`（正斜杠）。

可以使用 `[playerName]` 变量，代入与传送门交互的玩家名称。

![](https://www.zrips.net/wp-content/uploads/2022/09/PortalCommandsInterface.png)

**7.** 例如，添加如下命令：

![](https://www.zrips.net/wp-content/uploads/2022/09/PortalExampleCommands.png)

**8.** 设置完成。玩家穿过传送门时，会获得失明效果，并被取消飞行。

也可以点击红色的 `[X]` 按钮，删除施加失明效果的命令。

**9.** 传送门在 `~/plugins/CMI/Saves/Portals.yml` 文件中的保存格式如下。

```text
  Test1:
    Loc: 358.0:64.0:77.0:358.0:67.0:81.0
    enabled: true
    effect: reddust
    color: 8224125
    showParticles: true
    Tp: world;-979.5;82.0;544.5;90.3;2.4
    kickBack: true
    particlesByPermission: false
    requiresPerm: false
    informOnMissingPerm: false
    particleAmount: 20
    particleHide: 0
    activationRange: 16
    commandsWithoutTp: true
    commands:
    - cmi effect [playerName] blindness 2 1 -s
    - cmi fly [playerName] false​
```

## 注意事项

在 CMI 的 config.yml 文件中，可以配置分配给所有传送门的命令，默认命令是 `cmi effect [playerName] blindness 2 1 -s`。

如果要移除该命令，将其替换为 `none` 即可。

```text
Portals:
  # Defines in milliseconds how often to check if player entered portal or not
  # Bigger numbers can help slightly lower server load but small portals, 1 block depth without back wall can be passed through without teleportations if player moves fast enought
  CheckInterval: 300
  # Defines in milliseconds how often to check if player entered portal range for particles to apear
  CheckParticleInterval: 500
  Defaults:
    # Should we perform commands without set destination location by default
    # This only effects newly created portal areas
    # When set to true at moment you create portal you can enter it and commands defined belove will be performed without teleporting you anywhere
    # This can be change for each portal independently with ingame portal editor
    PerformCommands: true
    # Commands to be performed on teleport event
    Commands:
    - cmi effect [playerName] blindness 2 1 -s
```

## 补充说明

- 传送门支持 BungeeCord 群组网络，可以将玩家传送到其他服务器。设置时，先创建传送门，打开图形界面，点击位置按钮。聊天栏中会出现一条消息。前往目标服务器，该服务器也应安装 CMI，然后点击这条消息。这样设置后，玩家穿过传送门时就会被传送到指定服务器。记得在 BungeeCord 代理服务器上安装 [CMI-Bungee jar](https://zrips.net/cmib/)。  
  ![](https://www.zrips.net/wp-content/uploads/2022/09/PortalsBungeeCordServerLocation.png)  
  ![](https://www.zrips.net/wp-content/uploads/2022/09/PortalsBungeeCordLocationMessage.png)
- 传送门命令支持跨 BungeeCord 群组网络执行，并会在玩家传送后执行。
- 在传送门的命令部分添加以下内容，可以在玩家进入传送门时播放音效：  
  ![](https://www.zrips.net/wp-content/uploads/2022/10/PortalSoundCommands.png)注意：音效名称可能随 Minecraft 版本而不同。
- 输入 `/cmi portals`，可以按距离由近到远查看所有传送门。
- 每个传送门可以添加任意数量的命令，也支持使用专用命令。
- 使用 `/cmi portals forceupdate [portalName]` 可以强制更新传送门。
- 使用 `/cmi portals enabled [portalName] [true/false]` 可以启用或禁用传送门。

## 命令、权限与占位符

---

命令：

```text
> cmi checkcommand portal
/cmi portals (new/nearest/forceupdate/setlocation/enabled) (portalName) (world:x:y:z:yaw:pitch)
>
```

权限：

```text
> cmi checkperm portal
cmi.command.portal.[portalname] - Allows to use portal
cmi.command.portals - Set portals
cmi.select - Visualize selection before creating a portal
>
```

占位符：

```text
No relative placeholders for portals
```
