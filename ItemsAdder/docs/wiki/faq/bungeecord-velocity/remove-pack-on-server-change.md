---
title: "切换服务器时移除资源包"
source_url: "https://wiki.itemsadder.com/faq/bungeecord-velocity/remove-pack-on-server-change"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 切换服务器时移除资源包

## 当玩家切换服务器时移除资源包

如果你有多个服务器，并且希望用户切换服务器时移除 ItemsAdder 资源包，请按照本教程操作。

### 如何操作

1. 下载[空白资源包](http://matteodev.it/spigot/itemsadder/blank_pack.zip)。
2. 将其上传到某处，例如（跳过教程中的 `/iazip` 部分）[DropBox](../../plugin-usage/plugin-configuration/resourcepack-hosting/dropbox.md)、[OneDrive](../../plugin-usage/plugin-configuration/resourcepack-hosting/onedrive.md)、[GoogleDrive](../../plugin-usage/plugin-configuration/resourcepack-hosting/google-drive.md) 等。
3. 获取 URL
4. 打开其他服务器的 `server.properties` 文件并设置 URL

```properties
resource-pack=http://your_url/blank_pack.zip
```

完成！

当玩家加入你的其他服务器时，ItemsAdder 资源包将被默认资源包替换。

