---
title: Scripts/ItemTime.js
source_kind: imported-configuration
translation_review: reviewed
source_file: Scripts/ItemTime.js
source_version: 1.22.0
---

# Scripts/ItemTime.js

文件：`Scripts/ItemTime.js`。版本：`1.22.0`。

随包脚本。

```javascript title="Scripts/ItemTime.js"
function main(time) {
    const date = new Date()
    date.setTime(date.getTime() + (Number(time) * 1000))
    return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日" + date.getHours() + "时" + date.getMinutes() + "分" + date.getSeconds() + "秒"
}
```
