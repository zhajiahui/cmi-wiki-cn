---
title: 自定义别名（CustomAlias.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: CustomAlias/CustomAlias.yml
---

# 自定义别名（CustomAlias.yml）

文件：`plugins/CMI/CustomAlias/CustomAlias.yml`

```yaml title="CustomAlias.yml"
#
# 尽可能在游戏内编辑自定义变量
# 可使用额外变量，例如 [playerName] 自动插入命令发送者的名称
# 支持全部全局变量，完整列表见语言文件
# 可插入以下行，在命令之间添加延迟
# delay! 5
# 后续命令延迟指定秒数后执行
# 别名需要玩家名称等可变参数时，必须指定参数内容及其位置
# 例如：/cmi heal Zrips
# 使用以下别名命令，可将其缩写为 /h zrips
# cmi heal $1
# 需要多个参数时，使用 $1- 格式；数字表示调用别名时的参数位置
# 例如：cmi tppos $1-
# 要在输入错误子命令时显示帮助，可在别名中使用 ?
# 例如：ca ?
# 此时玩家执行 /ca wrongsub 或 /ca anotherwrong
# 就会执行这个别名下的命令，适合显示帮助及正确用法

{}
```
