**CMI 监狱功能**有 4 条命令：

**`/cmi jail [playerName] (time) (jailName) (cellId) (-s) (r:jail_reasson)`** 用于监禁玩家。time 为可选参数，未指定时使用默认时长。jailName 也是可选参数，未指定时选择最近的监狱。cellId 同样可选，未指定时使用空闲牢房。监禁原因可以填写任意内容，并会显示在占位符中。

`/cmi jailedit`   
管理所有监狱的主要命令。

`/cmi jaillist`   
列出所有监狱，以及每座监狱的牢房数量和囚犯人数。点击后可以查看详细信息。

`/cmi unjail [playerName]`   
用于释放玩家，同样是一条重要命令。

创建监狱前，先查看 config.yml 文件。

```text
Jail:
  # Defines in milliseconds how often to check if the player leaves the jail area
  # Bigger numbers can help slightly lower server load
  CheckInterval: 500
  # Defines default jail time when time is not provided with a command
  DefaultTime: 300
  # Chat range in blocks while the player is in jail
  # Set to 0 to allow talking
  # set to -1 to prevent talking in general while jailed
  ChatRange: 20
  # When set to true jail time will decrease while the player is offline
  # When set to false jail time will only be counted while the player is online
  CountWhileOffline: false
  # When set to true jail time will not decrease if player gets into afk mode while being jailed
  # When set to false, time will pass normally
  NoAfk: false
  # Do you want to prevent players damage while he is in jail
  PreventDamage: true
  # Do you want to prevent players hunger while he is in jail
  PreventHunger: true
  Commands:
    # Commands to be performed when the player gets jailed
    OnJail:
    - ''
    # Commands to be performed when the player gets unjailed
    OnUnJail:
    - ''
  WhiteListedCmds:
  - cmi msg
  - cmi reply
```

根据自己的偏好和需求调整配置。例如，可以根据服务器类型修改默认监禁时长，默认只有 5 分钟。

如果想防止被监禁的玩家在聊天栏刷屏，可以设置聊天范围，毕竟他们被关着也没别的事可做。将范围限制为一定的方块距离后，他们仍可聊天，但只有附近的玩家能看到，例如同在监狱里的其他玩家。

默认情况下，玩家退出服务器后，剩余刑期不会减少。这样可以要求玩家服满整个刑期，而不是直接退出，等时间到了再回来。

防止玩家挂机也有帮助，因为玩家可能只是让账号保持登录，自己转头去做作业之类的事（是的，确实会这样……）。

如果仍想允许被监禁的玩家使用一些基础命令，可以将这些命令加入白名单。

下面开始创建监狱。

首先，**建造一座简单的监狱**，例如：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail1.jpg)

不必建得很复杂。

然后使用 CMI 的选区工具，默认为**木锹**，选择一个区域。选区会用粒子效果标记。

![](https://www.zrips.net/wp-content/uploads/2019/06/jail2.jpg)

使用 `/cmi jailedit addjail [jailName]` 创建监狱。这里取一个“很有创意”的名字 **myJail**，所以命令为 **/cmi jailedit addjail myJail**。

随后会显示现有监狱列表，其中应包含刚创建的监狱，如下图所示：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail3.jpg)

接下来就简单了（没错，刚才那一步才是最难的，毕竟谁知道监狱该怎么建呢……）。在聊天栏中点击新建的监狱，为它创建牢房。新建监狱中只会显示一个 **[+]**。走进第一间牢房，点击这个 **[+]** 按钮，就会看到现有牢房列表，其中应包含刚添加的牢房，如下图所示：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail4.jpg)

可以按需要重复这一步，牢房数量没有上限。一般建议将牢房彼此隔开；这不是功能限制，只是通常的做法。毕竟，我们也不希望囚犯一起策划越狱！

此时监狱已经可以使用，但还有一点不便：玩家熬过 5 分钟刑期后，虽然已不再处于监禁状态，却仍会留在监狱里，像是有人忘了通知他们释放一样。因此，需要设置监狱外的传送位置，将服刑结束的玩家送出去。往前数第二张图中有一个灰色的 **[tp]** 按钮。走到监狱外的目标位置，点击它，就会收到类似“**Set new outside location**”的确认消息，监狱外的位置就设好了。之后可以按需要修改这个位置。

现在设置已完成：监狱里有牢房，也有玩家获释后前往的监狱外位置。

## 补充功能

被监禁的玩家会看到 Boss 血条消息，显示剩余刑期。

![](https://www.zrips.net/wp-content/uploads/2019/06/jail5.jpg)

## 监狱告示牌

如果想向其他人展示这里关着谁、还要关多久，可以使用动态告示牌或全息文字，两种方式任选其一。

先设置告示牌。放置一块告示牌，位置不限，然后执行 **/cmi dsign new** 创建动态告示牌，会出现类似内容：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail6.jpg)

虽然外观很简单，但已能实现需要的功能。

添加如下内容：

```text
%cmi_jail_time_myJail_1%
%cmi_jail_username_myJail_1%
%cmi_jail_reason_myJail_1%
```

这会显示监禁时间、被监禁的玩家，以及监禁原因；原因只会在监禁玩家时有填写的情况下显示。最终设置应如下所示：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail7.jpg)

如果想让刷新更快，可以打开动态告示牌的图形界面（Open GUI），调小默认刷新间隔。不过对于牢房信息，默认间隔通常就够用。

![](https://www.zrips.net/wp-content/uploads/2019/06/jail8.jpg)

## 监狱全息文字

如果更喜欢醒目的显示方式，可以创建**全息文字**。站在要放置全息文字的位置，执行类似 **/cmi hologram new myJailCell1** 的命令，其中 myJailCell1 只是示例中的全息文字名称。会出现如下内容：

![](https://www.zrips.net/wp-content/uploads/2019/06/jail9.jpg)

是不是很眼熟？确实与刚才相似。添加以下内容：

```text
%cmi_jail_time_myJail_1%
%cmi_jail_username_myJail_1%
%cmi_jail_reason_myJail_1%
```

这样会以和动态告示牌相同的方式显示被监禁玩家的信息。注意，全息文字的默认更新间隔可能不足以让显示平滑更新，需要打开设置界面（open settings GUI），将更新间隔设为例如 1 秒。

![](https://www.zrips.net/wp-content/uploads/2019/06/jail10.jpg)
