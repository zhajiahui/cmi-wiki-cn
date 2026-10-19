---
title: "收纳袋"
source_url: "https://wiki.itemsadder.com/adding-content/items/bundle"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 收纳袋
收纳袋可以根据当前状态使用不同的纹理或模型。

自定义收纳袋可以有四种外观状态：

- `normal` —— 空收纳袋。
- `filled` —— 至少装有一个物品的收纳袋。
- `open_back` —— 选中袋内物品时，渲染在物品后方的图层。
- `open_front` —— 渲染在选中物品前方的图层。

Minecraft 用三层内容组成打开状态的收纳袋：

1. `open_back`
2. 当前选中的物品
3. `open_front`

ItemsAdder 保留了原版 Minecraft 的渲染逻辑。

## 创建纹理

创建四张带透明通道的 PNG 纹理：

``` text
contents/my_bundle_tutorial/textures/item/bundles/ruby_bundle.png
contents/my_bundle_tutorial/textures/item/bundles/ruby_bundle_filled.png
contents/my_bundle_tutorial/textures/item/bundles/ruby_bundle_open_back.png
contents/my_bundle_tutorial/textures/item/bundles/ruby_bundle_open_front.png
```

文件夹结构应如下所示：

``` text
contents/
└── my_bundle_tutorial/
    ├── bundles.yml
    └── textures/
        └── item/
            └── bundles/
                ├── ruby_bundle.png
                ├── ruby_bundle_filled.png
                ├── ruby_bundle_open_back.png
                └── ruby_bundle_open_front.png
```

四张纹理应使用相同的分辨率和画布尺寸。

`open_back` 和 `open_front` 的透明区域很重要，因为 Minecraft 会在两者之间渲染选中的物品。

### 空收纳袋纹理

`ruby_bundle.png` 是收纳袋内没有物品时显示的纹理。

### 装有物品的收纳袋纹理

至少装有一个物品时显示 `ruby_bundle_filled.png`。

### 打开状态的后层纹理

`ruby_bundle_open_back.png` 包含收纳袋打开后的后半部分。

此图层渲染在选中的物品后方。

### 打开状态的前层纹理

`ruby_bundle_open_front.png` 包含收纳袋打开后的前半部分。

此图层渲染在选中的物品前方。

## 物品配置

在 `bundles.yml` 中添加以下配置：

``` yaml
info:
  namespace: my_bundle_tutorial
items:
  ruby_bundle:
    name: Ruby Bundle
    material: BUNDLE
    graphics:
      textures:
        normal: item/bundles/ruby_bundle
        filled: item/bundles/ruby_bundle_filled
        open_back: item/bundles/ruby_bundle_open_back
        open_front: item/bundles/ruby_bundle_open_front
```

配置中不要包含 `.png` 扩展名。

## 纹理属性

### `normal`

``` yaml
normal: item/bundles/ruby_bundle
```

此属性为必填项，用来定义空收纳袋纹理。

### `filled`

``` yaml
filled: item/bundles/ruby_bundle_filled
```

此属性为可选项。

省略时，ItemsAdder 会让空袋和装有物品的收纳袋都使用 `normal` 模型。

### `open_back`

``` yaml
open_back: item/bundles/ruby_bundle_open_back
```

此属性定义在选中物品后方渲染的图层。

使用纹理方式时，ItemsAdder 会自动生成使用以下父模型的模型：

``` text
minecraft:item/template_bundle_open_back
```

### `open_front`

``` yaml
open_front: item/bundles/ruby_bundle_open_front
```

此属性定义在选中物品前方渲染的图层。

使用纹理方式时，ItemsAdder 会自动生成使用以下父模型的模型：

``` text
minecraft:item/template_bundle_open_front
```

`open_back` 和 `open_front` 都是可选项，但建议同时提供。

缺少其中之一时，对应图层可能回退到原版收纳袋图层。

## 测试收纳袋

重新生成资源包：

``` text
/iazip
```

获取自定义收纳袋：

``` text
/iaget my_bundle_tutorial:ruby_bundle
```

往袋内放入一个或多个物品。

查看打开状态纹理的方法：

1. 打开背包。
2. 将鼠标移到装有物品的收纳袋上。
3. 滚动鼠标滚轮，选中袋内的某个物品。
4. Minecraft 会在 `open_back` 与 `open_front` 之间渲染选中的物品。

只有在背包界面中选中袋内物品时，才会渲染打开状态的图层。

手持、掉落在地面或放入物品展示框时，收纳袋使用 `normal` 或 `filled` 状态。

## 使用自定义模型

也可以提供 JSON 模型，不让 ItemsAdder 根据纹理生成模型。

``` yaml
info:
  namespace: my_bundle_tutorial

items:
  ruby_bundle:
    name: Ruby Bundle
    material: BUNDLE
    graphics:
      models:
        normal: item/bundles/ruby_bundle
        filled: item/bundles/ruby_bundle_filled
        open_back: item/bundles/ruby_bundle_open_back
        open_front: item/bundles/ruby_bundle_open_front
```

将模型文件放入：

``` text
contents/my_bundle_tutorial/models/item/bundles/
```

结构应如下所示：

``` text
contents/
└── my_bundle_tutorial/
    ├── bundles.yml
    ├── models/
    │   └── item/
    │       └── bundles/
    │           ├── ruby_bundle.json
    │           ├── ruby_bundle_filled.json
    │           ├── ruby_bundle_open_back.json
    │           └── ruby_bundle_open_front.json
    └── textures/
        └── item/
            └── bundles/
                ├── ruby_bundle.png
                ├── ruby_bundle_filled.png
                ├── ruby_bundle_open_back.png
                └── ruby_bundle_open_front.png
```

使用 `graphics.models` 时，ItemsAdder 不会生成或修改提供的模型文件。

打开状态的模型必须使用正确的原版模板父模型。

### 打开状态的后层模型

```json
{
  "parent": "minecraft:item/template_bundle_open_back",
  "textures": {
    "layer0": "my_bundle_tutorial:item/bundles/ruby_bundle_open_back"
  }
}
```

### 打开状态的前层模型

```json
{
  "parent": "minecraft:item/template_bundle_open_front",
  "textures": {
    "layer0": "my_bundle_tutorial:item/bundles/ruby_bundle_open_front"
  }
}
```

## 故障排查

### 只能看到空袋和装有物品两种状态

收纳袋装有物品本身并不会让外观变成打开状态。

打开背包，将鼠标移到收纳袋上，用滚轮选择袋内某个物品。

### 打开状态显示原版纹理

请确认同时配置了以下两个属性：

``` yaml
open_back: item/bundles/ruby_bundle_open_back
open_front: item/bundles/ruby_bundle_open_front
```

然后重新执行 `/iazip`，并接受更新后的资源包。

### 选中的物品位置不正确

请确保打开状态模型准确使用以下父模型：

``` text
minecraft:item/template_bundle_open_back
minecraft:item/template_bundle_open_front
```

同时确保前后两张纹理的画布尺寸和对齐方式一致。

### 出现纹理缺失

请检查：

- 纹理路径与实际文件一致。
- YAML 配置中的纹理路径未包含 `.png` 扩展名。
- 命名空间正确。
- 所有文件名均使用小写字符。
- 添加文件后已经重新生成资源包。

## 完成

现在自定义收纳袋已支持空袋、装有物品和打开状态，同时保留原版选中物品的渲染行为。

