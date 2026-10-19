---
title: "书与笔"
source_url: "https://wiki.itemsadder.com/adding-content/items/writable-book"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 书与笔

此功能仍处于实验阶段，教程可能随后续插件版本而变化。

创建自定义书与笔时，先声明成书物品。

```yaml
info:
  namespace: test
items:
  written_letter:
    name: Written Letter
    material: WRITTEN_BOOK
    graphics:
      texture: item/other/written_letter
```

然后声明书与笔，指定需要从成书复制的属性。本例为 `item_model`，让书写后仍保留纹理。

```yaml
  letter:
    name: Letter
    material: WRITABLE_BOOK
    graphics:
      texture: item/other/letter
    events:
      book_write:
        replace_properties:
          item_model:
            copy_from_item: test:written_letter
```

创建自定义书与笔时，先声明成书物品。

```yaml
info:
  namespace: test
items:
  letter_written_letter:
    name: Written Letter
    resource:
      material: WRITTEN_BOOK
      generate: true
      textures:
        - item/other/written_letter
```

然后声明书与笔，指定需要从成书复制的属性。本例为 `custom_model_data`，让书写后仍保留纹理。

```yaml
  letter:
    name: Letter
    resource:
      material: WRITABLE_BOOK
      generate: true
      textures:
        - item/other/letter
    events:
      book_write:
        replace_properties:
          custom_model_data:
            copy_from_item: test:letter_written_letter
```

<div><figure><img src="../../assets/4c5f00e697bf59a3fcb8.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../assets/4351e7133dcd7c1f08c3.png" alt=""><figcaption></figcaption></figure></div>
