---
title: 示例对话一（ExampleFirst.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Dialogs/ExampleFirst.yml
---

# 示例对话一（ExampleFirst.yml）

文件：`plugins/CMI/Dialogs/ExampleFirst.yml`

## `welcome` { #welcome }

```yaml title="ExampleFirst.yml · welcome"
welcome:
  Enabled: true
  Label: "{#white}欢迎 {#gray}%cmi_user_display_name% {#white}来到 {#edward}%cmi_user_world_formatted%"
  Description:
    Width: 300
    Lines:
    - "{#green}地球上最棒的 Minecraft 服务器！"
    - ''
    - "{#white}很高兴你能加入，%cmi_user_display_name%{#white}！"
    - "有任何问题都可以询问管理团队"
  VisualFields:
  - Width: 300
    Lines:
    - "{#brown}额外信息行！"
  Buttons:
    Columns: 3
    List:
    - Label: "{#red}阅读规则"
      Width: 100
      OpenDialog: license
      Tooltip:
      - "{#red}开始游戏前请先阅读！"
    - Label: "{#green>}看个笑话{#darkgreen<}"
      Width: 100
      OpenDialog: 'randomtext'
    - Label: "{#edward>}开始游戏{#darkgreen<}"
      Width: 100
      Commands:
      - closeinv!
    - Label: "{#blue}选择一项"
      Width: 100
      OpenDialog: inputexample
    - Label: ''
      Width: 1
    - Label: "{#yellow}显示效果示例"
      Width: 100
      OpenDialog: visualexample
    - Label: "{#yellow}访问我们的网站，%cmi_user_display_name%"
      Width: 304
      Url: www.zrips.net
  Close:
    Label: "{#pink>}离开！{#edward<}"
    Tooltip:
    - "{#pink>}出发吧，%cmi_user_display_name%！{#edward<}"
    Commands:
    - 'cmi feed [playerName]'
    Width: 150
```

## `visualexample` { #visualexample }

```yaml title="ExampleFirst.yml · visualexample"
visualexample:
  Enabled: true
  Label: "{#white}显示效果示例"
  Description:
    Width: 300
    Lines:
    - "{#green}顶部的说明文字！"
  VisualFields:
  - Width: 300
    Lines:
    - "{#brown}额外信息行！"
  - Item: "Stone;n{{#red}自定义名称};e{sharpness:2}"
    Text:
      Width: 150
      Lines:
      - "{#green}物品说明文字，支持自动换行和"
      - ''
      - "{#white}多行显示"
    Width: 16
    Height: 16
    ShowTooltip: true
    ShowDecorations: false
  - Item: potato
    Text:
      Width: 150
      Lines:
      - "{#green}物品不显示悬停提示"
    Width: 16
    Height: 16
    ShowTooltip: false
  - Item: '[ItemInHand]'
    Text:
      Lines:
      - "{#green}%cmi_iteminhand_displayname% {#white}就是你手中拿着的物品！"
  Close:
    Label: "{#edward}返回！"
    OpenDialog: welcome
    Width: 250
```

## `inputexample` { #inputexample }

```yaml title="ExampleFirst.yml · inputexample"
inputexample:
  Enabled: true
  Label: "{#white}输入控件示例"
  Inputs:
  - Label: "{#brown}选择一项"
    Width: 150
    Options:
    - Label: "选项 A"
      OpenDialog: 'randomtext'
    - Label: "{#red}选项 B"
      Default: true
      Commands:
      - 'cmi heal [playerName]'
    - Label: "选项 C"
  - Label: "勾选后保存，即可恢复生命值！"
    OnTrue:
      Commands:
      - cmi heal [playerName]
    OnFalse:
      Commands:
      - "msg! [playerName] 这次不给你免费治疗！"
  Buttons:
    Columns: 1
    List:
    - Label: "{#yellow}保存"
      Width: 150
      Save: true
  Close:
    Label: "{#pink}返回"
    OpenDialog: welcome
```

## `license` { #license }

```yaml title="ExampleFirst.yml · license"
license:
  Enabled: true
  Label: "{#white}用户协议"
  VisualFields:
  - Width: 350
    Lines:
    - "点击“同意条款”或继续在本服游玩，即表示你郑重承诺："
    - ''
    - ''
    - ''
    - "{#white}1. 不破坏、不偷窃，也不炸毁别人的房子，除非对方真的求你这么做。（就算这样，也请录像留证，以备法律需要。）"
    - "{#nobel}2. 不开挂、不违规飞行、不使用 X-ray，也不学闹鬼的 AI 穿墙。幽灵就该是死的，墙就该是实心的。"
    - "{#white}3. 同意管理员永远是对的，尤其是在他们犯错的时候。有争议可以去岩浆坑里解决。"
    - "{#nobel}4. 不在聊天栏刷屏，除非刷的是“傻方块部™”批准的梗图。"
    - "{#white}5. 好好造东西，别只在地上挖出形状不雅的洞。"
    - "{#nobel}6. 不在出生点里召唤凋灵。说真的，这样做只会换来封禁。"
    - "{#white}7. 接受卡顿、苦力怕爆炸，以及宠物狗莫名消失的可能。这里是 Minecraft，不是心理诊所。"
    - "{#nobel}8. 保证不索要 op 权限、创造模式、免费钻石，或管理员的信用卡号。"
    - "{#white}9. 接受这只是一款游戏，不能代替现实中的掌控欲、复仇或恋爱。"
    - "{#nobel}10. 知道自己盖的建筑如果是个泥土方块，可能会被温柔又善意地吐槽。"
    - ''
    - ''
    - "{#white}接受协议，就表示你同意友善相处、开心游玩，别成为我们再次禁用 TNT 的原因。"
    - ''
    - "{#yellow}点击进入方块乐园。"
    - "点错了就会像不听话的鹦鹉一样，被温柔地踢出去。"
  Inputs:
  - Type: Boolean
    Label: "同意条款"
    OnTrue:
      Commands:
      - asConsole! cmi heal [playerName]
      - closeinv!
    OnFalse:
      Commands:
      - "asConsole! cmi kick [playerName] 你没有同意条款！"
  Close:
    Label: "更新！"
    Save: true
    Width: 150
```
