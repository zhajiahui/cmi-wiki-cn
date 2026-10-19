---
title: "ChatControl-Red"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/chatcontrol-red"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# ChatControl-Red

[此处下载](https://www.mc-market.org/resources/18217/)

ItemsAdder 表情兼容性:\
查看详情: [https://github.com/kangarko/ChatControl-Red/issues/853#issuecomment-818497610](https://github.com/kangarko/ChatControl-Red/issues/853#issuecomment-818497610)

## 添加自定义频道前缀

如果你想设置一个在聊天中显示的图片频道前缀，请跟随此指引.

![示例：Arcade 频道的 ARCADE 前缀](../../assets/d0660d60cd8a857eb90d.png)

你只需要在格式配置中设置如下内容，(比如在 ChatControl Red 的 `format/arcade.yml` 中)：

```yaml
  prefix:
    Message: ':arcade:'
```

当然，你需要使用自己的 [font\_image ](../../adding-content/font-images/font-images.md)名称替换 `arcade`，这里只是示例。

## 文本效果

通常 ItemsAdder 的文本效果不会在 ChatControl Red 中生效。\
但如果将以下内容添加到 ChatControl Red 的 `rules` 文件夹中，它们就能正常使用。（我将其放在 `global.rs` 中。）

```
match <r\s([^>]+)>
require perm ia.user.text_effect.use.r
strip colors false
then replace #FFFFFE$1&r
    
match <w\s([^>]+)>
require perm ia.user.text_effect.use.w
strip colors false
then replace #FFFFFD$1&r
    
match <j\s([^>]+)>
require perm ia.user.text_effect.use.j
strip colors false
then replace #FFFFFB$1&r
    
match <rw\s([^>]+)>
require perm ia.user.text_effect.use.rw
strip colors false
then replace #FFFFFC$1&r
    
match <rj\s([^>]+)>
require perm ia.user.text_effect.use.rj
strip colors false
then replace #FFFEFE$1&r
```
