---
title: Expansions/CustomAction.js
source_kind: imported-configuration
translation_review: reviewed
source_file: Expansions/CustomAction.js
source_version: 1.22.0
---

# Expansions/CustomAction.js

文件：`Expansions/CustomAction.js`。版本：`1.22.0`。

随包脚本。

```javascript title="Expansions/CustomAction.js"
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
