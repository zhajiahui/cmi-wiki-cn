---
title: "我看不到表情、自定义界面、HUD等"
source_url: "https://wiki.itemsadder.com/faq/i-cant-see-emoji-guis-huds-etc."
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 我看不到表情、自定义界面、HUD等

* 打开 **ItemsAdder** 的 `config.yml`
*   启用此选项：

    ```yaml
    fix_force_unicode_font_images: true
    ```
* 运行 `/iazip` 重新生成资源包
* 按照安装插件时选定的[托管方法教程](../plugin-usage/plugin-configuration/resourcepack-hosting.md)操作
