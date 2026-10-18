---
title: 条件
source: https://docs.phoenixdevt.fr/mmocore/misc/conditions
source_snapshot: '2026-10-19'
---

# 条件 {#✅-conditions}

> **警告**
>
> 此功能将在不久的将来与MythicLib[脚本条件](../../mythiclib/scripts/conditions/intro.md)合并（此更新将向后兼容）。该页面将被删除并移至MythicLibwiki。

每个掉落表都可以受到各种条件的限制。这意味着只有满足删除表所有要求的玩家在执行操作时才会实际访问它。以下是可用条件的列表。

### 条件表（自1.9.5起） {#conditions-tables-since-1-9-5}

你可以在`conditions.yml`中创建条件表。然后，你将能够使用`from`条件立即引用一整套条件。

```yml
#Example
test-condition:
  - 'level{amount=10}'
  #Will load the 2 conditions from test-condition-2.
  - 'from{source=test-condition-2}'

test-condition-2:
  - 'world{name=world}'
  - 'level{profession=mining;amount=3}'
```

## 可用条件 {#available-conditions}

|状况 |格式|
| --- | --- |
| 来自 | `from{source=condition-id}` |
| 主等级 | `level{amount=LEVEL_HERE}` |
| 副职业等级 | `level{profession=PROFESSION_NAME;amount=LEVEL_HERE}` |
| 当前生物群系 | `biome{name=BIOMES}` |
| 当前世界 | `world{name=WORLD_NAME}` |
| 权限 | `permission{node=PERMISSION_NODE}` |

---

原文：[✅ Conditions](https://docs.phoenixdevt.fr/mmocore/misc/conditions) · 原文归档：2026-10-19
