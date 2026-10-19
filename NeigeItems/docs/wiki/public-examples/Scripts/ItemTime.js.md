---
title: "物品时间脚本"
source_url: "https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/Scripts/ItemTime.js"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "1.22.0 @ 8791487eeec1866b30f45c34a60fbc0e738c9ecf"
source_material: "official-repository-bundled-example"
scope_note: "公开随包材料全文；付费 Wiki 未取得，本页不代表完整 Wiki"
---

# 物品时间脚本

```javascript
function main(time) {
    const date = new Date()
    date.setTime(date.getTime() + (Number(time) * 1000))
    return date.getFullYear() + "年" + (date.getMonth() + 1) + "月" + date.getDate() + "日" + date.getHours() + "时" + date.getMinutes() + "分" + date.getSeconds() + "秒"
}
```
