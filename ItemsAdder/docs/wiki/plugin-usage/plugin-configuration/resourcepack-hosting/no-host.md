---
title: "不托管"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/resourcepack-hosting/no-host"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 不托管

### 仅限高级用户！

如果想自行处理资源包上传和托管，请启用此选项。

这样做的原因：

* 你可能通过某种自定义插件来处理
* 你的 Bungeecord 群组服已由其他服务器（例如大厅）应用资源包。

```yaml
resource-pack:
# ...
  hosting:
    no-host:
      enabled: false
```
