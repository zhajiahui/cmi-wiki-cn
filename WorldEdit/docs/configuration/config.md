---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 7.4.6+7648-00664b0
---

# config.yml

文件：`config.yml`。版本：`7.4.6+7648-00664b0`。

主配置。

## `limits` { #limits }

```yaml title="config.yml · limits"
#
# WorldEdit 配置文件
#
# 编辑本文件时请注意：
# - 不要使用制表符。必须使用空格，否则 Bukkit 会报告
#   错误。如果使用 Notepad++ 等编辑器（推荐 Windows
#   用户使用），必须将其设为 "replace tabs with spaces"（用空格替换制表符）。
#   可在 Settings > Preferences > Language Menu 中修改此设置。
# - 不要删除缩进。缩进用于将某些配置项归入对应的
#   分类，例如将 "max-blocks-changed" 放在 "limits"
#   分类中。
# - 如果想在将此文件交给 WorldEdit 使用前检查格式，
#   请将其内容粘贴到 http://yaml-online-parser.appspot.com/
#   并检查是否出现 "ERROR:"。
# - 以 # 开头的行是注释，会被忽略。
# - 如果想允许使用方块，请将 "disallowed-blocks" 改为 []。
#

limits:
    max-blocks-changed:
        default: -1
        maximum: -1
    vertical-height:
        default: 256
    max-polygonal-points:
        default: -1
        maximum: 20
    max-radius: -1
    max-super-pickaxe-size: 5
    max-brush-radius: 5
    butcher-radius:
        default: -1
        maximum: -1
    disallowed-blocks:
    - "minecraft:oak_sapling"
    - "minecraft:jungle_sapling"
    - "minecraft:dark_oak_sapling"
    - "minecraft:spruce_sapling"
    - "minecraft:birch_sapling"
    - "minecraft:acacia_sapling"
    - "minecraft:black_bed"
    - "minecraft:blue_bed"
    - "minecraft:brown_bed"
    - "minecraft:cyan_bed"
    - "minecraft:gray_bed"
    - "minecraft:green_bed"
    - "minecraft:light_blue_bed"
    - "minecraft:light_gray_bed"
    - "minecraft:lime_bed"
    - "minecraft:magenta_bed"
    - "minecraft:orange_bed"
    - "minecraft:pink_bed"
    - "minecraft:purple_bed"
    - "minecraft:red_bed"
    - "minecraft:white_bed"
    - "minecraft:yellow_bed"
    - "minecraft:powered_rail"
    - "minecraft:detector_rail"
    - "minecraft:short_grass"
    - "minecraft:dead_bush"
    - "minecraft:moving_piston"
    - "minecraft:piston_head"
    - "minecraft:sunflower"
    - "minecraft:rose_bush"
    - "minecraft:dandelion"
    - "minecraft:poppy"
    - "minecraft:brown_mushroom"
    - "minecraft:red_mushroom"
    - "minecraft:tnt"
    - "minecraft:torch"
    - "minecraft:fire"
    - "minecraft:redstone_wire"
    - "minecraft:wheat"
    - "minecraft:potatoes"
    - "minecraft:carrots"
    - "minecraft:melon_stem"
    - "minecraft:pumpkin_stem"
    - "minecraft:beetroots"
    - "minecraft:rail"
    - "minecraft:lever"
    - "minecraft:redstone_torch"
    - "minecraft:redstone_wall_torch"
    - "minecraft:repeater"
    - "minecraft:comparator"
    - "minecraft:stone_button"
    - "minecraft:birch_button"
    - "minecraft:acacia_button"
    - "minecraft:dark_oak_button"
    - "minecraft:jungle_button"
    - "minecraft:oak_button"
    - "minecraft:spruce_button"
    - "minecraft:cactus"
    - "minecraft:sugar_cane"
    - "minecraft:bedrock"
```

## `use-inventory` { #use-inventory }

```yaml title="config.yml · use-inventory"
use-inventory:
    enable: false
    allow-override: true
    creative-mode-overrides: false
```

## `logging` { #logging }

```yaml title="config.yml · logging"
logging:
    log-commands: false
    file: worldedit.log
    # 自定义日志消息的格式。使用 Java 通用格式字符串（java.util.Formatter），参数如下：
    #   1$ : date - 表示日志记录中事件发生时间的 Date 对象。
    #   2$ : source - 表示调用者的字符串；若无法获取，则使用日志记录器的名称。
    #   3$ : logger - 日志记录器的名称。
    #   4$ : level - 日志级别。
    #   5$ : message - Formatter.formatMessage(LogRecord) 方法返回的格式化日志消息。它使用 java.text 格式，而不使用 java.util.Formatter 的格式参数。
    #   6$ : thrown - 表示与日志记录关联的 throwable 及其堆栈回溯的字符串，回溯以换行符开头；若不存在，则为空字符串。
    # 详情参见：
    #   https://docs.oracle.com/javase/8/docs/api/java/util/Formatter.html
    #   https://docs.oracle.com/javase/8/docs/api/java/util/logging/SimpleFormatter.html#format-java.util.logging.LogRecord-
    format: "[%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS %4$s]: %5$s%6$s%n"
```

## `super-pickaxe` { #super-pickaxe }

```yaml title="config.yml · super-pickaxe"
super-pickaxe:
    drop-items: true
    many-drop-items: false
```

## `snapshots` { #snapshots }

```yaml title="config.yml · snapshots"
snapshots:
    directory:
```

## `navigation-wand` { #navigation-wand }

```yaml title="config.yml · navigation-wand"
navigation-wand:
    item: minecraft:compass
    max-distance: 100
```

## `scripting` { #scripting }

```yaml title="config.yml · scripting"
scripting:
    timeout: 3000
    dir: craftscripts
```

## `saving` { #saving }

```yaml title="config.yml · saving"
saving:
    dir: schematics
```

## `files` { #files }

```yaml title="config.yml · files"
files:
    allow-symbolic-links: false
```

## `history` { #history }

```yaml title="config.yml · history"
history:
    size: 15
    expiration: 10
```

## `calculation` { #calculation }

```yaml title="config.yml · calculation"
calculation:
    timeout: 100
```

## `debugging` { #debugging }

```yaml title="config.yml · debugging"
debugging:
    trace-unflushed-sessions: false
```

## `wand-item` { #wand-item }

```yaml title="config.yml · wand-item"
wand-item: minecraft:wooden_axe
```

## `shell-save-type` { #shell-save-type }

```yaml title="config.yml · shell-save-type"
shell-save-type:
```

## `no-op-permissions` { #no-op-permissions }

```yaml title="config.yml · no-op-permissions"
no-op-permissions: false
```

## `debug` { #debug }

```yaml title="config.yml · debug"
debug: false
```

## `show-help-on-first-use` { #show-help-on-first-use }

```yaml title="config.yml · show-help-on-first-use"
show-help-on-first-use: true
```

## `server-side-cui` { #server-side-cui }

```yaml title="config.yml · server-side-cui"
server-side-cui: true
```

## `command-block-support` { #command-block-support }

```yaml title="config.yml · command-block-support"
command-block-support: false
```
