---
title: "手动编辑方块状态"
source_url: "https://wiki.itemsadder.com/adding-content/blocks/manual-editing-blockstates"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 手动编辑方块状态

这违背了 ItemsAdder 避免手动修改特定文件的初衷。\
后果自负。

你可以手动编辑 blockstates json 文件。为此，创建一个自定义内容文件夹，并将编辑后的 blockstates 放入其中。

**ItemsAdder** 会将各个内容文件夹中找到的 blockstate `.json` 文件与 **ItemsAdder** 的自定义方块自动合并（如果你创建了自定义方块）。

例如 `contents/my_custom_blockstates/assets/minecraft/blockstates/note_block.json`
