---
title: "动作组示例"
source_url: "https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/Functions/ExampleFunction.yml"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "1.22.0 @ 8791487eeec1866b30f45c34a60fbc0e738c9ecf"
source_material: "official-repository-bundled-example"
scope_note: "公开随包材料全文；付费 Wiki 未取得，本页不代表完整 Wiki"
---

# 动作组示例

```yaml
test0: 'tell: 触发test动作组'
test1:
  - 'tell: 触发test动作组'
test2:
  condition: chance(0.5)
  actions: 'tell: 触发test动作组'
test3:
  - condition: chance(0.5)
    actions: 'tell: 触发test动作组'
```
