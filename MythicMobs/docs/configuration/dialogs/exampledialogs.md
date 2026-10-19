---
title: dialogs/ExampleDialogs.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: dialogs/ExampleDialogs.yml
source_version: 5.13.0-SNAPSHOT-1abf9862
---

# dialogs/ExampleDialogs.yml

文件：`dialogs/ExampleDialogs.yml`。版本：`5.13.0-SNAPSHOT-1abf9862`。

随包示例配置。

## `WelcomeNotice` { #welcomenotice }

```yaml title="dialogs/ExampleDialogs.yml · WelcomeNotice"
# ========================================
#  对话框定义示例
# ========================================
#
#  对话框使用 Paper Dialog API（1.21.6+）。
#  使用 showDialog 机制向玩家显示对话框：
#    - showDialog{dialog=WelcomeNotice} @trigger
#
#  所有文本字段均支持 MiniMessage 格式与 MythicMobs 占位符。
#  每个正文、输入项和按钮元素均支持可选 Conditions，
#  可按玩家分别判断是否显示。
#
# ========================================

# 带有单个按钮的简单提示对话框。
WelcomeNotice:
  Title: "<gold>欢迎！"
  Body:
    - Type: text
      Message: "<gray>欢迎来到服务器，<target.name>！"
    - Type: text
      Message: "<yellow>祝你玩得愉快。"
  Buttons:
    - Label: "<green>知道了！"
      Width: 150
```

## `QuestOffer` { #questoffer }

```yaml title="dialogs/ExampleDialogs.yml · QuestOffer"
# 确认对话框，会根据玩家点击的按钮
# 触发不同技能。
QuestOffer:
  Title: "<gold>有新任务可接取"
  CanClose: true
  Pause: false
  AfterAction: CLOSE
  Body:
    - Type: text
      Message: "<gray>一位神秘的陌生人需要你的帮助。"
    - Type: text
      Message: "<yellow>奖励：<green>50 金币"
  Buttons:
    - Label: "<green>接受"
      Tooltip: "接受此任务"
      Width: 150
      Skill: ExampleQuestAccepted
    - Label: "<red>拒绝"
      Tooltip: "拒绝此任务"
      Width: 150
      Skill: ExampleQuestDeclined
```

## `CharacterSetup` { #charactersetup }

```yaml title="dialogs/ExampleDialogs.yml · CharacterSetup"
# 包含输入项和条件按钮的多操作对话框。
# 演示全部输入类型与基于条件的显示方式。
CharacterSetup:
  Title: "<blue>角色设置"
  ExternalTitle: "设置"
  CanClose: false
  Pause: false
  AfterAction: WAIT_FOR_RESPONSE
  Body:
    - Type: text
      Message: "<gray>配置你的角色设置。"
      Width: 300
  Inputs:
    - Type: text
      Key: nickname
      Label: "显示名称"
      MaxLength: 16
    - Type: bool
      Key: pvpEnabled
      Label: "开启 PvP？"
    - Type: range
      Key: difficulty
      Label: "难度"
      Start: 1
      End: 10
      Initial: 5
      Step: 1
    - Type: option
      Key: classChoice
      Label: "选择职业"
      Options:
        warrior: "战士"
        mage: "法师"
        ranger: "游侠"
  Buttons:
    - Label: "<green>确认"
      Tooltip: "保存设置"
      Width: 150
      Skill: ExampleCharacterConfirmed
    - Label: "<red>取消"
      Width: 150
  ExitButton:
    Label: "关闭"
    Width: 100
  Columns: 2
```
