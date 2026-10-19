---
title: "1.21.3 及更旧版本上的 graphics 和 item\\_model"
source_url: "https://wiki.itemsadder.com/faq/graphics-and-item_model-on-1.21.3-and-lower"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 1.21.3 及更旧版本上的 graphics 和 item\_model

请勿报告与此有关的纹理缺失或其他问题。

`'PLAYER' won't be able to see modern items 'graphics'.`

当你使用不支持新物品图形的客户端加入服务器时，就会出现此错误（新图形通过 `graphics` 属性自动生成，或通过 `item_model` 使用）。

考虑将客户端版本限制为 1.21.4+，或停止使用新的 `graphics` 或 `item_model` 属性。

<figure><img src="../assets/553e2ed84b4afc15bf0f.png" alt=""><figcaption></figcaption></figure>
