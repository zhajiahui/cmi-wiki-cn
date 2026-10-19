---
title: "自定义动作示例"
source_url: "https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/Expansions/CustomAction.js"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "1.22.0 @ 8791487eeec1866b30f45c34a60fbc0e738c9ecf"
source_material: "official-repository-bundled-example"
scope_note: "公开随包材料全文；付费 Wiki 未取得，本页不代表完整 Wiki"
---

# 自定义动作示例

```javascript
// // 文件名不重要, 写成啥都行
// // enable函数会自动执行
// function enable() {
//     // 插入新的自定义动作
//     ActionManager.addConsumer(
//         // 动作名称
//         "test",
//         // 动作内容(有可能异步调用, 所以需要同步执行的内容需要自行同步)
//         function (context, string) {
//             const player = context.player
//             if (player == null) return
//             player.sendMessage(SectionUtils.parseSection("<number::0_10_2>"))
//         })
// }
```
