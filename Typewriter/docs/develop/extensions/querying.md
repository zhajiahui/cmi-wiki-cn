---
title: 查询条目（Query Entries）
source: https://docs.typewritermc.com/develop/extensions/querying
source_version: 0.8.0
---

# 查询条目（Query Entries）

有时你需要按任何字段或按类型查找条目。这可以通过`Query`类来完成。

如果你需要查找特定类型的所有条目：

QueryExample.kt

```kotlin
    val entries = Query.find<MyEntry>()
```

有时你需要通过特定的过滤器来获取它：

QueryExample.kt

```kotlin
    val entries = Query.findWhere<MyEntry> {
        it.someField == "some value"
    }
```

有时你需要通过 id 查找条目：

QueryExample.kt

```kotlin
    val id = "some_id"
    val entry = Query.findById<MyEntry>(id)
```

其他时候，你需要按页面查找条目：

QueryExample.kt

```kotlin
    val pageId = "some_page_id"
    val entries = Query.findWhereFromPage<MyEntry>(pageId) {
        it.someField == "some value"
    }
```

---

原文：[Query Entries](https://docs.typewritermc.com/develop/extensions/querying) · 文档版本：0.8.0
