---
title: "盔甲纹理与光影模组不兼容"
source_url: "https://wiki.itemsadder.com/faq/armors-issues/armors-textures-not-working-with-shaders-mod"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 盔甲纹理与光影模组不兼容

如果服务器和客户端均为 1.21.2 或更高版本，你可以使用新的盔甲创建方法。它不使用任何原版着色器来创建自定义盔甲，因此兼容光影模组。

更多信息见[此处](../../adding-content/items/armors.md)。

![](../../assets/b3986188399b05a58b17.png)

![](../../assets/4540133f798f61bb8019.png)


## 这个问题的原因是什么？

### Optifine 问题

Optifine 有一个限制，如果你安装了任何自定义 Optifine 光影，自定义盔甲将无法正常工作。

你必须暂时禁用 **Optifine** 光影或暂时忍受这个问题。

我已经联系了 Optifine 开发者：[https://github.com/sp614x/optifine/issues/6391](https://github.com/sp614x/optifine/issues/6391)

### Iris Shaders 问题

Iris 有一个限制，如果你安装了任何自定义 Iris 光影，自定义盔甲将无法正常工作。

我已经联系了 Iris 开发者：[https://github.com/IrisShaders/Iris/issues/1042](https://github.com/IrisShaders/Iris/issues/1042)
