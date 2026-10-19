---
title: "粒子"
source_url: "https://wiki.itemsadder.com/adding-content/entities/particles"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 粒子

## 设置

### 配置用于指定粒子位置的特殊骨骼

用 **Blockbench** 打开 `.iaentitymodel` 模型文件。\
新建一个骨骼，名称不限。

![](../../assets/2806e86401b0678f4a55.png)

右键点击骨骼，选择“**Bone Config**”

![](../../assets/cc07576bba86a8033079.png)

勾选“**Locator**”选项，再点击“**Confirm**”。

![](../../assets/09937114f957d29fa3fa.png)

切换到“**Animate**”视图。

![](../../assets/f81138cdb795aaabfcc3.png)

选择一个动画。

![](../../assets/8bd9d23eb61260625a60.png)

选择魔杖图标“**Animate Effects**”

![](../../assets/5c2903c31d4dedd9cd27.png)

点击“**Particle**”效果类型旁的 **+** 图标，创建粒子关键帧。

![](../../assets/800e05aac27985460c61.png)

在“**Keyframe**”面板中编辑数值。

* Name：粒子名称，使用 Minecraft 游戏内粒子名称。
* Bone (locator)：本教程第一部分创建的骨骼名称，作为粒子的位置。
* Speed：粒子发射速度。
* Count：发射的粒子数量。
* XYZ delta：指定粒子效果在各轴方向的范围，单位为方块，以 **x y z** 为中心。各坐标表示粒子距离中心的生成范围，可以使用小数。<br>

![](../../assets/d0b1aece7ca57c373015.png)

## 完成

