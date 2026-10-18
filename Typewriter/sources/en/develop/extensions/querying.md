# Query Entries

Sometimes you need to find an entry by any of it's fields or by type. This can be done with the `Query` class.

If you need to find all entries of a specific type:

QueryExample.kt

```kotlin
    val entries = Query.find<MyEntry>()
```

Sometimes you need it by a specific filter:

QueryExample.kt

```kotlin
    val entries = Query.findWhere<MyEntry> {
        it.someField == "some value"
    }
```

Sometimes you need to find an entry by it's id:

QueryExample.kt

```kotlin
    val id = "some_id"
    val entry = Query.findById<MyEntry>(id)
```

Other times you need to find entries by their page:

QueryExample.kt

```kotlin
    val pageId = "some_page_id"
    val entries = Query.findWhereFromPage<MyEntry>(pageId) {
        it.someField == "some value"
    }
```
