---
title: Scripts/ExampleScript.js
source_kind: imported-configuration
translation_review: reviewed
source_file: Scripts/ExampleScript.js
source_version: 1.22.0
---

# Scripts/ExampleScript.js

文件：`Scripts/ExampleScript.js`。版本：`1.22.0`。

随包脚本。

```javascript title="Scripts/ExampleScript.js"
function main() {
    if (typeof this.player != "undefined") {
        return this.vars("<strings-1>") + this.player.getName()
    } else {
        return this.vars("<strings-1>")
    }
}
```
