---
title: "不兼容"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/not-compatible"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 不兼容

_**是否与插件X兼容?**_

作者无法了解世界上每一个插件的代码实现，因此无法肯定回答此问题。以下是可能造成问题的插件列表：

* 所有使用**自定义资源包**的插件（如果你具备手动合并资源包的基本知识，就可以使它们兼容；只需确保不替换 ItemsAdder 的文件）
* [CraftEnhance](https://www.spigotmc.org/resources/custom-recipes-and-crafting-craftenhance.65058/)，此插件会扰乱 ItemsAdder 自定义配方的逻辑，并造成物品复制漏洞，因此请勿使用
* 自定义工作台行为和配方的插件
* 目前**不兼容**通过**生成具有不同面的蘑菇方块**来创建自定义纹理的**插件**和世界生成器。我会在未来添加兼容支持。
