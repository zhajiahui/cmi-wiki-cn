CMI-API 的源码和 JAR 文件可在 [github.com/Zrips/CMI-API](https://github.com/Zrips/CMI-API) 获取。

在 `pom.yml` 中添加：

```text
<dependency>  <groupId>com.github.Zrips</groupId>  <artifactId>CMI-API</artifactId>  <version>9.8.6.4</version>  <scope>provided</scope></dependency>
```

```text
<repository>  <id>jitpack.io</id>  <url>https://jitpack.io</url></repository>
```

## 长期全息图

全息图分为长期和临时两种。若只需短时间显示简单信息，使用临时全息图会更高效。长期全息图在显示前会计算更多信息，以提高长期运行时的效率。

创建简单全息图的示例：

```text
CMIHologram hologram = new CMIHologram("CustomHoloName", loc); CMIHologramPages pages = hologram.getPages();pages.setLines(Arrays.asList("Line one", "Line Two", "ICON:Stone"));hologram.show();
```

与临时全息图不同，创建长期全息图时只需提供名称和初始位置。名称最好唯一；同名全息图会被替换。若已存在同名记录，取得并修改原记录会更高效。
文本行并非必填，但不添加文本就没有内容可显示。
调用 `show()` 会重新计算全息图的显示范围、更新范围等设置，因此应先设置这些参数，再调用 `show()`。
这种方式创建的全息图默认保存到文件。如果只想保留到服务器重启，需要关闭文件保存：

```text
hologram.getSettings().setSaveToFile(false);
```

## 临时全息图

如果只需为一名玩家显示一段时间的全息图，可以使用：

```text
new CMIHologram(@Player, @Location, @List<String>, @long);
```

或：

```text
CMIHologram.quickShow(playerReference, loc, lines, 50);
```

例如：

```text
List<String> lines = Arrays.asList("Line one", "Line Two", "ICON:Stone");CMIHologram.quickShow(playerReference, loc, lines, 50);
```

该示例显示三行内容，最后一行为图标。全息图在指定位置向指定玩家显示，并在 50 ticks 后自动消失。调用该方法或构造器后，后续处理会自动完成，无需额外调用。

## 基础设置

```text
CMIHologramSettings baseSettings = hologram.getSettings();
```

控制全息图的行为、外观、位置、可见性和持久化。

### 朝向模式

```text
baseSettings.setBillboard(@CMIBillboard);
```

设置全息图相对于观察玩家的旋转方式。默认 `CENTER`。

### 缩放

```text
baseSettings.setScale(@CMIVector2D);
```

设置全息图 X、Y 轴的显示比例。默认 `1, 1`。

### 水平角度

```text
baseSettings.setYaw(double);
```

设置水平旋转角度，单位为度。数值会归一化到 `0–360`。

### 俯仰角度

```text
baseSettings.setPitch(double);
```

设置垂直旋转角度，单位为度。数值限制在 `-90` 到 `90` 之间。

### 方向

```text
baseSettings.setDirection(@CMIVector3D);
```

通过 X、Y、Z 设置完整的旋转方向。

### 亮度

```text
baseSettings.setLightLevel(@CMIVector2D);
```

设置天空光照与方块光照等级。默认 `15, 15`。

### 天空光照

```text
baseSettings.setSkyLevel(int);
```

单独设置天空光照等级，对应亮度向量的 X 分量。

### 方块光照

```text
baseSettings.setBlockLevel(int);
```

单独设置方块光照等级，对应亮度向量的 Y 分量。

### 偏移

```text
baseSettings.setOffset(@CMIVector3D);
```

相对于全息图的中心位置移动。默认 `0, 0, 0`。

### 分组

```text
baseSettings.setGroup(String);
```

将全息图加入一个分组，便于关联或统一管理同组全息图。

### 权限要求

```text
baseSettings.setPermissionRequirement(boolean);
```

设置查看全息图是否需要对应权限。默认 `false`。

### 保存到文件

```text
baseSettings.setSaveToFile(boolean);
```

设置是否将全息图保存到数据文件。默认 `true`。

### 视线检查

```text
baseSettings.setCheckLineOfSight(boolean);
```

设置是否仅在玩家能直接看见全息图时显示。默认 `false`。

### 可见范围

```text
baseSettings.setVisibilityRange(int);
```

设置玩家能看见全息图的最大距离。

该值不得小于更新范围。

### 更新范围

```text
baseSettings.setUpdateRange(int);
```

设置全息图主动更新的最大距离。

该值不得大于可见范围。

### 更新间隔

```text
baseSettings.setUpdateIntervalTicks(int);
```

设置全息图的更新间隔，单位为 Minecraft ticks。

`20` ticks 约为 `1` 秒。设为 `0` 时，更新不受间隔延迟限制。

## 文本设置

```text
CMIHologramTextSettings textSettings = hologram.getTextSettings();
```

控制文本全息图的外观和渲染方式。

### 文本对齐

```text
baseSettings.setTextAlignment(@CMITextAlignment);
```

设置文本的水平对齐方式。默认 `CENTER`。

### 背景颜色

```text
baseSettings.setBackgroundColor(@CMIChatColor);
```

设置文本背景颜色。默认 `BLACK`。

### 背景透明度

```text
baseSettings.setBackgroundAlpha(int);
```

设置文本背景的透明度。

取值范围为 `0` 到 `255`：

- `0`：完全透明。
- `255`：完全不透明。

默认 `125`。

### 文本透明度

```text
baseSettings.setTextAlpha(int);
```

设置文本本身的透明度。

取值范围为 `0` 到 `255`：

- `0`：完全透明。
- `255`：完全不透明。

默认 `255`。

### 双面显示

```text
baseSettings.setDoubleSided(boolean);
```

设置是否从正面和背面都渲染文本。默认 `false`。

### 阴影

```text
baseSettings.setShadowed(boolean);
```

设置文本是否带阴影。默认 `true`。

### 穿透显示

```text
baseSettings.setSeeThrough(boolean);
```

设置文本是否能透过方块等物体显示。默认 `false`。

### 行宽

```text
baseSettings.setLineWidth(int);
```

设置文本换行前的最大宽度。

数值限制在 `1` 到 `10000` 之间。默认 `1000`。

### 填充量

```text
baseSettings.setFillerAmount(int);
```

设置渲染文本行时使用的填充间距。

数值限制在 `1` 到 `10000` 之间。默认 `245`。

## 图标设置

```text
CMIHologramIconSettings iconSettings = hologram.getIconSettings();
```

控制图标全息图的外观、旋转、位置和朝向模式。

### 朝向模式

```text
baseSettings.setBillboard(@CMIBillboard);
```

设置图标相对于观察玩家的旋转方式。默认 `null`，继承基础设置的朝向模式。

### 偏移

```text
baseSettings.setOffset(@CMIVector3D);
```

相对于全息图位置移动图标。默认 `0, 0, 0`。

### 缩放

```text
baseSettings.setScale(double);
```

统一设置图标 X、Y、Z 轴的缩放比例。默认 `1, 1, 1`。

```text
baseSettings.setScale(@CMIVector3D);
```

分别设置图标 X、Y、Z 轴的缩放比例。默认 `1, 1, 1`。

### 方向

```text
baseSettings.setDirection(@CMIVector3D);
```

通过 X、Y、Z 设置图标完整的旋转方向。

### 俯仰角度

```text
baseSettings.setPitch(int);
```

设置图标的垂直旋转角度，单位为度。

### 水平角度

```text
baseSettings.setYaw(int);
```

设置图标的水平旋转角度，单位为度。

### 滚转角度

```text
baseSettings.setRoll(int);
```

设置图标绕自身前向轴的旋转角度，单位为度。

## 交互设置

```text
CMIHologramInteraction interactionSettings = hologram.getInteractionSettings();
```

控制交互区域、指令、悬停和点击效果、粒子效果，以及交互相关的文本前缀。

### 指令

```text
baseSettings.setCommands(@List<String>);
```

向全息图的全局交互指令列表添加指令，与全息图交互时可以执行这些指令。

传入的指令会追加到现有列表中，而不会替换原列表。

### 可交互

```text
baseSettings.setInteractable(boolean);
```

设置玩家是否能与全息图交互。默认 `false`。

### 交互区域尺寸

```text
baseSettings.setDimensions(@CMIVector2D);
```

设置交互区域额外的宽度和高度。默认 `0, 0`。

### 交互区域偏移

```text
baseSettings.setOffset(@CMIVector3D);
```

相对于全息图位置移动交互区域。默认 `0, 0, 0`。

### 粒子区域尺寸

```text
baseSettings.setParticleDimensions(@CMIVector2D);
```

设置交互粒子显示区域的宽度和高度。默认 `0, 0`。

### 粒子位置

```text
baseSettings.setParticlePosition(short);
```

设置粒子效果使用的位置。默认 `0`。

### 粒子间距

```text
baseSettings.setParticleSpacing(double);
```

设置交互粒子效果中各粒子之间的间距。默认 `0.1`。

### 粒子数量

```text
baseSettings.setParticleCount(int);
```

设置交互效果显示的粒子数量。

数值限制在 `0` 到 `2000` 之间。默认 `1`。

### 悬停效果

```text
baseSettings.setHoverEffect(@CMIEffect);
```

设置玩家指向全息图时显示的完整粒子效果。

```text
baseSettings.setHoverEffect(@CMIParticle);
```

设置悬停效果的粒子类型。初始化时粒子数量为 `0`，速度为 `1`。

默认 `SMALL_SMOKE`。

### 显示悬停粒子

```text
baseSettings.setShowHoverParticle(boolean);
```

设置玩家指向全息图时是否显示粒子。默认 `true`。

### 粒子偏移

```text
baseSettings.setParticleOffset(@CMIVector3D);
```

相对于全息图位置移动交互粒子。默认 `0, 0, 0`。

### 显示点击粒子

```text
baseSettings.setShowClickParticle(boolean);
```

设置点击全息图时是否显示粒子。默认 `true`。

### 普通前缀

```text
baseSettings.setBasePrefix(String);
```

设置全息图在普通、未被指向状态下的文本前缀。默认空字符串。

### 悬停前缀

```text
baseSettings.setHoverPrefix(String);
```

设置玩家指向全息图时使用的文本前缀。默认空字符串。

## 动画设置

```text
CMIHologramAnimationSettings animationSettings = hologram.getAnimationSettings();
```

控制全息图的淡入淡出动画和自动旋转。

### 淡入动画

```text
baseSettings.setFadeInAnimation(int);
```

启用淡入动画并设置速度。

数值限制在 `0` 到 `600` 之间；`0` 表示关闭动画。默认 `0`。

### 淡出动画

```text
baseSettings.setFadeOutAnimation(int);
```

启用淡出动画并设置速度。

数值限制在 `0` 到 `600` 之间；`0` 表示关闭动画。默认 `0`。

### 自动旋转

```text
baseSettings.setAutoRotate(int);
```

启用自动旋转并设置速度。

数值按 `1080` 度取模归一化；`0` 表示关闭自动旋转。默认 `0`。

## 背板设置

```text
CMIHologramBoardSettings boardSettings = hologram.getBoardSettings();
```

控制全息图后方可选背板的尺寸、位置、旋转和材质。

### 启用

```text
baseSettings.setEnabled(boolean);
```

启用或关闭全息图背板。默认 `false`。

### 额外尺寸

```text
baseSettings.setExtraDimensions(@CMIVector3D);
```

设置背板相对于全息图额外增加的宽、高、深。基础尺寸根据文本自动计算，这里的设置在计算结果上增加偏移。

向量各分量的含义：

- `X`：额外宽度。
- `Y`：额外高度。
- `Z`：额外深度。

默认 `0, 0, 0.01`。

### 偏移

```text
baseSettings.setOffset(@CMIVector3D);
```

相对于全息图位置移动背板。默认 `0, 0, 0`。

### 方向

```text
baseSettings.setDirection(@CMIVector3D);
```

通过 X、Y、Z 设置背板旋转。默认 `0, 0, 0`，只支持以 90 度为增量旋转。

### 材质

```text
baseSettings.setMaterial(@CMIMaterial);
```

设置背板使用的 Minecraft 材质。默认 `ACACIA_LOG`。

也可以使用 `AIR`，让背板没有可见材质。

## 分页设置

```text
CMIHologramPageSettings pageSettings = hologram.getPageSettings();
```

控制全息图的页面轮换和自动翻页。

### 自动翻页

```text
baseSettings.setAutoPagination(boolean);
```

启用或关闭自动切换页面。默认 `false`。

### 翻页间隔

```text
baseSettings.setPageChangeIntervalTicks(int);
```

设置自动切换到下一页的间隔，单位为 Minecraft ticks。

数值限制在 `0` 到 `20000` 之间。

`20` ticks 约为 `1` 秒。

默认使用 `HologramManager.getDefaultpageChangeInterval()` 配置的间隔。
