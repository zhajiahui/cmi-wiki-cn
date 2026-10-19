---
title: "修复方块问题"
source_url: "https://wiki.itemsadder.com/compatibility-with-other-plugins/compatible/mmoitems/fix-blocks-problem"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 修复方块问题

**MMOItems** 方块与 **ItemsAdder** 不兼容，反之亦然。

## 如何使用MMOItems方块？

你需要打开 **ItemsAdder** 的 `config.yml` 并禁用 **REAL** 方块（蘑菇块）。

```yaml
blocks:
  # ....
  custom:
    # ....
    mushroom: false
```

应用该改变后，你将无法创建带有 type：REAL 的 ItemsAdder 方块。

其他的 ItemsAdder 自定义方块类型仍然会生效(如 REAL\_NOTE)。
