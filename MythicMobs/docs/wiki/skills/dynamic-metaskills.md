---
title: 动态元技能
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Dynamic-Metaskills
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 动态元技能

通常，执行技能机制或元技能前，需要先将它们写入配置文件。动态元技能则允许：

- 通过动态构建它们来执行单个机制或整个元技能，即使它们以前从未存在过。
- 绕过机制/内联条件中缺少的占位符支持
- 将整个元技能存储到变量或NBTs中，使你能够稍后动态调用它们

1. [免责声明](dynamic-metaskills.md#disclaimer)
2. [这是如何工作的？](dynamic-metaskills.md#how-does-this-work)
3. [发生什么事了？](dynamic-metaskills.md#what-is-happening)
4. [动态创建元技能](dynamic-metaskills.md#dynamic-creation-of-metaskills)
5. [绕过占位符支持限制](dynamic-metaskills.md#bypassing-placeholder-support-limits)
6. [存储动态元技能](dynamic-metaskills.md#storing-dynamic-metaskills)
7. [限制](dynamic-metaskills.md#limitations)

# 免责声明 {#disclaimer}

这并非预期功能，而是 `vskill` 机制的工作方式带来的副作用，一直以来都能使用。

这种用法仍有许多未知之处。如果有可用于完善本页、帮助其他 MythicMobs 用户的信息，请联系 [Lxlp 的 Discord 个人资料](https://discord.com/users/353257382811533322)。

后文还会再次提醒，但这里必须强调：若把此功能与来自玩家的*任何*字符串结合，玩家就*能*轻易执行*任何* Mythic 机制，**包括命令机制**。因此，最终传入动态元技能的内容应由开发者编写，避免依赖玩家输入或玩家可控的值；否则必须验证并清理这些值。

# 工作原理 {#how-does-this-work}

基本上，这一切都可以归结为两件事：

- [可变技能机制](mechanics/variableskill.md)的使用
- [内联元技能](metaskills.md#inline-metaskills)的存在。

通过结合这两件事，现在可以做这样的事情

```yaml
Testmob:
  Type: pig
  Skills:
  - skill{s=
    [
      - setvariable{var=skill.temp;type=STRING;val=glow} @self
      - setvariable{var=skill.testskill;type=STRING;
        val=
        [
          - message{m=hello} @World
          - message{m=world} @World
          - message{m=<skill.var.temp>} @World
        ]} @self
      - vskill{s=<skill.var.testskill>}
      - vskill{s=
        [
          - particle{p=<skill.var.temp>} @selflocation{y=2}
        ]} @self
    ]} @self ~onInteract
```

![2024-08-17_17.54.14](../assets/cf84bae283a60f.png)

# 这里发生了什么？ {#what-is-happening}

Variableskill 会先解析 `skill` 属性，再执行其中指定的元技能。通常用它按生物或环境的具体情况动态确定元技能名称，很适合模板。但结合内联元技能后，还能产生其他效果：只要内容写成内联元技能，variableskill 就能解析并执行。

# 动态创建元技能 {#dynamic-creation-of-metaskills}

这样就可以即时创建全新的元技能，无需预先写入配置文件。

```yaml
Testmob:
  Type: pig
  Skills:
  - skill{s=
    [
      - setvariable{var=skill.temp;type=STRING;val=glow} @self
      
      - setvariable{var=skill.testskill2;type=STRING;val="["}
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2> - message{m=aaa} @World} @self
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2> - message{m=bbb} @World} @self
      - setvariable{var=skill.testskill2;type=STRING;val=<skill.var.testskill2>]} @self
      
      - vskill{s=<skill.var.testskill2>}
      - vskill{s=
        [
          - particle{p=<skill.var.temp>} @selflocation{y=2}
        ]} @self
    ]} @self ~onInteract
```

# 绕过占位符支持限制 {#bypassing-placeholder-support-limits}

并非每个机制、条件或目标选择器的每项属性都支持占位符。上述方法可以绕过这种限制。例如撰写本文时，粒子机制的粒子属性尚不支持占位符，但这种写法仍有效，因为 vskill 会*先解析占位符*；调用粒子机制时，内容已经解析完成。

这种方式不限于机制属性。构建字符串中的*任何字符*都可以使用占位符，只要解析结果是有效的内联元技能，就能执行。

# 存储动态元技能 {#storing-dynamic-metaskills}

新建的元技能保存在变量中，可以按需要选择作用域、保留时间，并使用变量的其他功能。也可以保存在 NBT 中，让制作的物品拥有完全自定义的技能。

> 如果玩家能控制物品，在 NBT 中存储这些内容可能有危险。例如允许创造模式的服务器中，玩家可以从保存的物品中取得带有自定义 NBT 的物品，任意执行代码。

# 限制 {#limitations}

由于这不是计划中的功能，因此其实现确实存在一些问题。

- 直接内联使用 skill、sudoskills 等技能机制时，若不加延迟，会出现控制台错误，机制也不会执行。可以通过以下两种方式之一解决：
- 继续使用 vskill 机制来代替其他机制。对于技能机制，一个简单的替换就可以了，但是要使用 sudoskill，你需要让 vskill 机制调用一个元技能来执行所述 sudoskill 机制本身
- 执行其他元机制前，加入约 15 游戏刻的延迟。

```yaml
ExampleWorkaround:
  Skills:
  - vskill{s=
    [
      - vskill{s=YourOtherMetaskill}
      - vskill{s=SudoskillWrapper;run=TheMetaskillToBeSudoed}
    ]}

SudoskillWrapper:
  Skills:
  - sudoskill{s=
    [
    - vskill{s=<skill.run>}
    ]} 

AnotherWorkaround:
  Skills:
  - vskill{s=
    [
      - vskill{s=YourOtherMetaskill}
      - vskill{s=SudoskillWrapper;run=
        [
        - message{m=<caster.name>} @World
        ]}
    ]}
```

```yaml
DelayWorkaround:
  Skills:
  - setvariable{var=skill.test;type=string;value=message} @self
  - vskill{
      skill=[
        - delay 15
        - randomskill{
            skills=[
              - <skill.var.test>{m=1}
            ],
            [
              - <skill.var.test>{m=2}
            ]} @self
      ]} @self
```
