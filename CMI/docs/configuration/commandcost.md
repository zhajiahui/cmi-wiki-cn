---
title: 命令费用（CommandCost.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Settings/CommandCost.yml
---

# 命令费用（CommandCost.yml）

文件：`plugins/CMI/Settings/CommandCost.yml`

## `Enabled` { #enabled }

```yaml title="CommandCost.yml · Enabled"
Enabled: false
```

## `Commands` { #commands }

```yaml title="CommandCost.yml · Commands"
# 示例：- 'cmi heal:100.5:true'
# 设置命令时，使用完整名称，不要使用别名
# 费用可为任意正数
# 费用后的第一个 true/false，决定执行命令扣费时是否提示玩家
# 第二个 true/false 决定执行和扣费前是否需要再次输入命令或点击聊天消息确认；会显示费用，默认要求确认
# 注意！使用完整基础命令，例如不要用 /heal，要用 /cmi heal，否则可能允许玩家免费执行基础命令
# 也可以在此填写自定义别名命令

# CMI 基础命令会检查是否执行成功，再决定扣费；自定义别名则不论成功与否都会扣费
# 例如 /cmi warp 输入错误传送点名称时不扣费，但自定义别名即使执行失败也会收费
Commands:
- cmi heal:100.5:true:true
- cmi feed:100.5:true:true
- cmi home :30:true:true
- cmi warp :10:true:true
```
