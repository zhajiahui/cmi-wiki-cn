---
title: Functions/ExampleFunction.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: Functions/ExampleFunction.yml
source_version: 1.22.0
---

# Functions/ExampleFunction.yml

文件：`Functions/ExampleFunction.yml`。版本：`1.22.0`。

随包配置。

## `test0` { #test0 }

```yaml title="Functions/ExampleFunction.yml · test0"
test0: 'tell: 触发test动作组'
```

## `test1` { #test1 }

```yaml title="Functions/ExampleFunction.yml · test1"
test1:
  - 'tell: 触发test动作组'
```

## `test2` { #test2 }

```yaml title="Functions/ExampleFunction.yml · test2"
test2:
  condition: chance(0.5)
  actions: 'tell: 触发test动作组'
```

## `test3` { #test3 }

```yaml title="Functions/ExampleFunction.yml · test3"
test3:
  - condition: chance(0.5)
    actions: 'tell: 触发test动作组'
```
