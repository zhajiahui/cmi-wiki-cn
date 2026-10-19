---
title: "文本格式"
source_url: "https://wiki.itemsadder.com/plugin-usage/beginners/text-formatting"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 文本格式

由于 Minecraft 的限制，此功能不适用于 [Minecraft 语言文件](../plugin-configuration/languages.md)。

## 如何使用多彩文本

你可以使用特殊写法更改文字颜色，并指定自定义十六进制颜色。

### Minimessage



```yaml
info:
  namespace: git_2224
  dictionary-lang: en
dictionary:
  display-name-test_gradient_dictionary: <#57ff5c><bold>test</bold><gradient:#ff00ee:#f79459>Amogus
items:
  test_gradient_dictionary:
    display_name: display-name-test_gradient_dictionary
    lore:
      - "<gold>yo0"
      - "<dark_green>yo1"
    resource:
      generate: false
      model_path: minecraft:item/emerald
      material: PAPER
  test_font:
    display_name: <gradient:#ff00ee:#f79459><font:alt>Alt font used for this item
    lore:
      - "<gradient:#ff00ee:#f79459><font:alt>Alt font used for this item"
      - "<gradient:#ff00ee:#f79459><font:alt>Alt font used for this item<"
    resource:
      generate: false
      model_path: minecraft:item/emerald
      material: PAPER
```

```
<#FE5A00>Magic Fuel
<red>Magic <green>Fuel
<gradient:#ff00ee:#f79459>Here is a gradient example text!
```

<div><figure><img src="../../assets/eb6de510aafd835c8564.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../assets/2c89a675ddc5887533a7.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../assets/c2a9cc94188e7f8fab01.png" alt=""><figcaption></figcaption></figure></div>

<div><figure><img src="../../assets/252f8aca563c4dbb219e.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../assets/d700e8cb21ce834275f3.png" alt=""><figcaption></figcaption></figure></div>

### 组件


```yaml
items:
  test_emerald:
    display_name: '{"text\":"TEST", "font": "alt"}'
    resource:
      generate: false
      model_path: minecraft:item/emerald
      material: PAPER
```

### 旧版写法

`display_name: '&6TEST'`

```yaml
items:
  test_emerald:
    enabled: true
    display_name: '&6TEST'
    resource:
      generate: false
      model_path: minecraft:item/emerald
      material: PAPER
```
