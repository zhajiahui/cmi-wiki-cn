---
title: "脚本示例"
source_url: "https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/src/main/resources/Scripts/ExampleScript.js"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "1.22.0 @ 8791487eeec1866b30f45c34a60fbc0e738c9ecf"
source_material: "official-repository-bundled-example"
scope_note: "公开随包材料全文；付费 Wiki 未取得，本页不代表完整 Wiki"
---

# 脚本示例

```javascript
function main() {
    if (typeof this.player != "undefined") {
        return this.vars("<strings-1>") + this.player.getName()
    } else {
        return this.vars("<strings-1>")
    }
}
```
