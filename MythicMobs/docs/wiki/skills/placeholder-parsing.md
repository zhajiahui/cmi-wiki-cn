---
title: 占位符解析
source_url: https://wiki.mythiccraft.io/mythicmobs/Skills/Placeholder-Parsing
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# 占位符解析 {#placeholder-parsing}

## 介绍 {#introduction}

某些属性的值不仅可以是静态值，还可以是包含占位符的值。

> 虽然文档中未包含此信息，但你可以使用 [MythicScribe](https://marketplace.visualstudio.com/items?itemName=Lxlp.mythicscribe) 扩展并将鼠标悬停在属性或机制上来检查它

那些值中可以有占位符的属性总是在执行相关机制时被解析，这样它们的值总是可以更好地反映生物、目标、[SkillTree](skilltrees.md)等的当前状态

## Mythic 占位符识别 {#mythic-placeholder-recognition}

Mythic 占位符具有 `<placeholder.segment1{attribute=value;attribute2=value2}.segment2.segment3{}>` 的通用语法

在文本中发现 `<` 字符后，如果

- 找到的`<`将开始一个新的占位符
- `<` 后面的字符**不是**
  - 另一个`<`
  - 空格
  - 等号`=`

从此处起，只要尚未找到数量相匹配的 `>`，这段文本就会被视为可能的 Mythic 占位符。如果找不到对应占位符，则原样返回占位符文本。

### 示例 {#examples}

- `<skill.var.example>`：将返回变量的值
- `<red>`：不是 Mythic 占位符，因此将返回 `<red>` 字符串
- `<<skill.var.amount>`：第一个 `<` 后面紧接着另一个 `<`，后者属于“黑名单”字符，因此第一个 `<` 会被当作普通字符串处理。而第二个 `<` 可以作为占位符的起始字符，所以 `<skill.var.amount>` 能被正确识别为占位符。假设这个技能作用域变量的值是 `N`，最终解析结果就是 `<N`。

## 解析顺序 {#parsing-order}

解析占位符时，*始终*按顺序执行以下步骤

- 将 Mythic 占位符替换为其值
- 将 Papi 占位符替换为其值
  - 如果目标实体是玩家，则针对该玩家解析 Papi 占位符
- 解析数学运算。
  - 在这一步中，也会解析并使用[数学运算](https://git.lumine.io/mythiccraft/MythicMobs/-/wikis/Skills/Math) Wiki 页面中列出的函数和运算符
  - 只有当该属性使用的占位符类型（PlaceholderInteger、PlaceholderFloat 等）支持数学运算，且字符串中出现特定字符（`*`、`-`、`+` 等）时，才会执行此步骤
    - PlaceholderString 占位符不会解析数学运算
    - PlaceholderInt 占位符会解析数学运算

## 复合解析 {#compound-parsing}

请**注意**，每一步处理的都是前面步骤已经解析过的内容。例如，可以使用下面的写法

```yaml
  - setvariable{var=skill.somevar;val=1}
  - setvariable{var=skill.example;type=STRING;val=%some_papi_placeholder_<skill.var.somevar>%}
```

其中，按顺序执行以下步骤

- 将 `<skill.var.somevar>` 替换为其值，也就是字面值 `1`
- 解析 papi 占位符 `%some_papi_placeholder_{string}%` 时，使用的是已经解析出的值 `1`，而不是字面字符串 `<skill.var.somevar>`

这样就能在 papi 占位符中使用 `<skill.var.somevar>` 存储的值。

> 同时务必注意解析顺序：虽然可以让 papi 占位符返回能被 Mythic 解析的占位符，例如让 `%some_other_papi_placeholder%` 返回 `<skill.var.test>` 之类的内容，但返回的这些占位符**不会**再被解析，因为对应的处理步骤已经结束了

将同样的思路用于数学运算，也可以得到下面的写法

```yaml
  - setvariable{var=skill.example;val=(1<skill.var.operation>3) + 4}
```

其中，`<skill.var.operation>` 的值会插入到 1 和 2 之间。因此

- 如果 `<skill.var.operation>` 为 +，则该值将是 (1+3)+4 数学运算的结果
- 如果 `<skill.var.operation>` 为 -，则该值为 (1-3)+4 数学运算的结果
- 如果 `<skill.var.operation>` 是 2，则该值将是 (123)+4 数学运算的结果
- 如果`<skill.var.operation>`是-2，则该值将是(1-23)+4数学运算的结果
