## 有没有能实现某项功能的指令？

可能有，通常已经有了。

截至 9.2.x，CMI 大约有 300 条指令，因此你需要的功能很可能已经包含在内。

不想提交工单或等待 GitHub、Discord 上的回复时，可以执行 `/cmi checkcommand [keyWord]`，查找与关键词相关的指令。

## 玩家能使用指令，怎么回事？

默认情况下，玩家没有任何具体指令的使用权限。你需要逐条分配权限节点。将鼠标悬停在游戏聊天中的错误消息上，或查看控制台输出，都可以找到缺少的权限。

如果悬停后看不到权限信息，检查是否缺少 `cmi.permisiononerror`。该权限默认分配给所有玩家；出现这种情况，通常是因为你明确移除了它。

指令权限的基本格式为 `cmi.command.[commandName]`，例如 `cmi.command.heal`。

## 如何从 Essentials 导入旧玩家数据？

从 Essentials 迁移到 CMI 时，可以使用专门的导入指令。导入时无需安装 Essentials 插件。

```text
/cmi importfrom essentials [home/warp/nick/logoutlocation/money/mail]
```

- `home`：导入家的位置。
- `nick`：导入玩家昵称。
- `logoutlocation`：导入玩家上次退出的位置。
- `money`：导入玩家余额。
- `mail`：导入玩家邮件。
- `warp`：导入传送点。

一次可以指定多个参数，也可以全部导入，例如：

```text
/cmi importfrom essentials home warp nick logoutlocation money mail
```

导入可能需要一些时间。原文给出的处理速度约为每秒 200 名玩家，过程中会显示进度消息。

若要沿用旧的 `worth.yml`，将其从 Essentials 文件夹复制到 CMI 文件夹即可。

## 如何使用短指令？

默认只启用了少量指令别名，大部分指令仍需使用完整格式，例如 `/cmi heal Zrips`。启用短指令有两种方式：修改 `alias.yml`，或自己创建别名。

在 `alias.yml` 中找到对应指令，将其设为 `true`。例如，要启用 `/heal`：

```text
  /heal: true
```

也可以用 `/cmi aliaseditor` 创建自定义别名，有两种操作方式：

1. 执行 `/cmi aliaseditor new heal-cmi heal $1-`，直接创建 `/heal`。
2. 在聊天窗口点击 `+`，输入 `heal` 并回车；再次点击 `+`，输入 `cmi heal $1-` 并回车。

这样就能使用 `/heal`。别名可以依次执行多条指令，也支持 CMI 的[特殊指令格式](https://www.spigotmc.org/wiki/cmi-specialized-commands/)。

别名中的 `$1` 表示第一个参数。例如，创建 `/cmi aliaseditor new heal-cmi heal $1` 后，执行 `/heal Zrips` 会把 `Zrips` 替换到原指令中，实际执行 `/cmi heal Zrips`。

参数也可以调换顺序。例如，创建 `/cmi aliaseditor new tps-cmi tp $2 $1` 后，执行 `/tps Zrips Zhax`，实际执行的是 `/cmi tp Zhax Zrips`。

若要从某个位置开始取全部剩余参数，使用 `$1-` 这样的格式。例如，创建 `/cmi aliaseditor new ms-cmi msg $1 $2-` 后，执行 `/ms Zrips Hello World!`，实际执行 `/cmi msg Zrips Hello World!`。

## 如何重置指定字段或整个数据库？

使用 `/cmi resetfields [collumnName] (-w:[worldName]) (-p:[playerName])`。

你可以把所有玩家的某一列重置为默认值，也可以重置指定世界中的家，或重置某名玩家的指定字段。

该命令一次只重置一列。如果要开新服并清空所有数据，使用 MySQL 时可删除 CMI 的数据表；使用 SQLite 时可重命名数据库文件。如果不熟悉 MySQL 删表操作，或没有相应权限，也可以修改配置文件中的表前缀，让插件创建空的新表。

## 玩家一直处于飞行状态怎么办？

如果玩家切换世界或重新登录后仍在飞行，可能是飞行状态没有正确关闭。可以尝试以下处理。

在 `eventcommands.yml` 的加入和传送事件中添加指令，强制关闭生存模式玩家的飞行，例如：

`perm:cmi.command.fly@! check:%cmi_user_gamemode%==Survival! asConsole! cmi fly [playerName] false -s`

也可以继续排查原因：移除其他插件后是否仍会发生？如果怀疑是插件错误，可以提交错误报告。

检查 `config.yml` 中的 `WorldLimits` 设置是否正确，同时检查玩家或权限组是否有通配符权限或 OP，因为这些权限也可能赋予 `.bypass` 节点。

还可以参考[这篇非官方文章](https://faq.cmi.support/mode-stuck)，检查是否遗漏了其他原因。
