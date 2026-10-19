---
title: Model Engine 模型消失
source_url: https://wiki.mythiccraft.io/mythicmobs/Troubleshooting/ModelEngine-Model-Vanishes
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Model Engine 模型消失 {#model-engine-model-vanishes}

如果 ModelEngine 模型在服务器重启后，或离开生物所在区域后消失，请检查 Model 的 `save` 属性是否设为   true  

当前生物文件中可能有如下配置行：

```yaml
Skills:
- model{m=Duck;n=name} @self ~onSpawn
```

添加以下内容即可解决问题：

```yaml
Skills:
- model{m=Duck;n=name;save=true} @self ~onSpawn
```
