---
title: "全局节点示例"
source_url: "https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/GlobalSections/ExampleSection.yml"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "1.22.0 @ 8791487eeec1866b30f45c34a60fbc0e738c9ecf"
source_material: "official-repository-bundled-example"
scope_note: "公开随包材料全文；付费 Wiki 未取得，本页不代表完整 Wiki"
---

# 全局节点示例

```yaml
global-strings-1:
  # 随机字符节点
  type: strings
  values:
    - test1
    - test2
global-number-1:
  # 随机数节点
  type: number
  # 随机数最小值
  min: 1
  # 随机数最大值
  max: 2
  # 小数保留位数
  fixed: 3
global-calculation-1:
  # 公式节点
  type: calculation
  # 计算公式
  formula: 1+2+3<global-number-1>
  # 公式结果最小值
  min: 1
  # 公式结果最大值
  max: 100
  # 小数保留位数
  fixed: 3
global-weight-1:
  # 权重字符串节点
  type: weight
  values:
    # 权重::字符串内容
    - 5::第一行
    - 1::第二行
global-js-1:
  # JavaScript节点
  type: js
  # 脚本路径
  path: ExampleScript.js::main
```
