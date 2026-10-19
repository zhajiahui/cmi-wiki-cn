---
title: custom-stats.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: custom-stats.yml
source_version: 6.10.1-SNAPSHOT
---

# custom-stats.yml

文件：`custom-stats.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `CUSTOM_MYLUCK` { #custom_myluck }

```yaml title="custom-stats.yml · CUSTOM_MYLUCK"
# 可在下方添加任意数量的自定义属性。
#
# 每添加一个自定义属性，都必须同时添加对应的
# 条目到 lore-format.yml 和 stats.yml 文件中。
#
# 执行 /mi reload 不会重载物品属性。修改这些属性后，
# 请重启服务器以应用更改。

CUSTOM_MYLUCK:
  # 在编辑界面中使用的名称
  name: "我的幸运"

  # 允许的属性类型：
  # - double(数值)
  # - text
  type: double

  # 描述必须是字符串列表
  lore:
    - "这是测试行 #1"
    - "这是测试行 #2"
```
