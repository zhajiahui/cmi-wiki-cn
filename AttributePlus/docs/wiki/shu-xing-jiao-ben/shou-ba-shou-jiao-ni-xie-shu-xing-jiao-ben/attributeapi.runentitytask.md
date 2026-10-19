---
title: "延迟触发任务"
source_url: "https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben/shou-ba-shou-jiao-ni-xie-shu-xing-jiao-ben/attributeapi.runentitytask"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方持续更新 Wiki；2026-10-19 快照；未固定到随包 3.3.3.6"
---

# 延迟触发任务

## 用法

`AttributeAPI.runEntityTask` 这个方法的说明请你前往 `AttributeAPI` 文档页面查看

```javascript
function runAttack(attacker, entity, handle){
  AttributeAPI.runEntityTask(10000, "测试", attacker, function(){
    print("任务开始执行了!")
  })
  return false
}
```
