---
title: 示例对话二（ExampleSecond.yml）
source_kind: configuration-examples
translation_review: reviewed
source_file: Dialogs/ExampleSecond.yml
---

# 示例对话二（ExampleSecond.yml）

文件：`plugins/CMI/Dialogs/ExampleSecond.yml`

## `randomtext` { #randomtext }

```yaml title="ExampleSecond.yml · randomtext"
randomtext:
  Enabled: true
  Description:
    Randomize: true
    Lines:
    - "{#yellow}苦力怕为什么和骷髅分手？\n\n{#green}因为他被炸懵了！"
    - "{#yellow}末影人为什么不喜欢笑话？\n\n{#green}因为他们总把事情看得太重！"
    - "{#yellow}史蒂夫为什么迷路了？\\n\\n{#green}因为他没跟着那些方块面包屑走！"
    - "{#yellow}Minecraft 玩家怎么避免晒伤？\\n\\n{#green}待在阴凉的生物群系里！"
    - "{#yellow}那位 Minecraft 玩家为什么是个好音乐家？\\n\\n{#green}因为他的方块节拍准极了！"
    - "{#yellow}鸡为什么要穿过下界？\\n\\n{#green}为了去另一边的生物群系！"
    - "{#yellow}怎么在 Minecraft 里开派对？\\n\\n{#green}把苦力怕挡在外面就行！"
    - "{#yellow}村民为什么那么会做生意？\\n\\n{#green}因为他有绿宝石级的标准！"
    - "{#yellow}Minecraft 里的庆祝活动叫什么？\\n\\n{#green}方块派对！"
    - "{#yellow}骷髅最不喜欢哪个房间？\\n\\n{#green}起居室！"
  Close:
    Label: "返回"
    OpenDialog: 'welcome'
    Width: 150
```
