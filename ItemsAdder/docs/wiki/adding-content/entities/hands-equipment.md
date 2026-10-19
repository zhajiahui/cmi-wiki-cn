---
title: "手持装备"
source_url: "https://wiki.itemsadder.com/adding-content/entities/hands-equipment"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 手持装备

## 显示自定义实体的手持装备


## 如何配置手部位置

使用 **Blockbench** 打开你的 `.iaentitymodel` 模型文件。

选择实体手部的基础骨骼。

![](../../assets/398b9a8f2916a8e3cb77.png)

创建一个新的组，该组将成为手部骨骼的子组。

![](../../assets/42e13a4196bed16c2ea1.png)

右键点击骨骼并选择“**Bone Config**”，本例中的骨骼是 `left_hand_slot`

![](../../assets/c1c61f72de5ffa7dccfb.png)

勾选 "**Left hand pivot**" 选项并按 "**Confirm**"。

![](../../assets/8418e71fb85272a51741.png)

如你所见，手部枢轴骨骼现在有了一个新图标。

![](../../assets/a1ca4d306032dcd45cbd.png)

![](../../assets/984d74dde6f7e8cd7ff9.png)

![](../../assets/a06897c299cb81c5e5b3.png)

按相同步骤设置右手，然后照常导出模型。

[advanced-method.md](advanced-method.md)
