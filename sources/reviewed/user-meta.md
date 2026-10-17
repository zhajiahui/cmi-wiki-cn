命令的基本用法：  
`/cmi usermeta [playerName] [add/remove/clear/list/increment] (key) (value) (-s)`

**Add** – 添加指定的键和值。如果已有同名键，则用新值覆盖。

**Remove** – 移除指定的键及其值。

**Clear** – 清除指定玩家记录的所有键和值。

**List** – 列出所有已记录的键及其值。

**Increment** – 已有值时修改当前值，否则创建一个新值。它会尝试将指定值加到现有值上，两者都必须是数字。

这条命令可以为玩家添加独立的数据值，并在需要时通过 **%cmi_user_meta_[key]%** 占位符再次使用。

可以保存希望附加到玩家身上的一般信息，也可以保存死亡次数等数据。

下面为玩家创建一个死亡计数器。初始命令为 **/cmi usermeta Zrips add deaths 0 -s**：**Zrips** 是目标玩家的名称，**add** 表示添加一项独立数据，**deaths** 是自定义名称，可以任意命名，**0** 是初始值，**-s** 则表示执行时不向玩家发送提示。

现在可以用 **%cmi_user_meta_[key]%** 占位符读取数据，返回值为 0.0，也就是带有小数。这里改用 **%cmi_user_metaint_[key]%**，完整占位符应为 **%cmi_user_metaint_deaths%**，返回值就是 0。

接下来修改这个值，让它在玩家死亡时增加。

在 eventCommands.yml 文件的 playerDeath 类别下添加一条命令。

命令为 **/cmi usermeta [playerName] increment deaths +1 -s**，会将当前值增加 1，且不显示反馈消息。

也可以使用 **-1** 或其他数值，按指定数值修改当前值（如果可以修改）。

执行这条命令后，**%cmi_user_metaint_deaths%** 将返回 1，而不是 **0**；第二次执行后返回 **2**，以此类推。
