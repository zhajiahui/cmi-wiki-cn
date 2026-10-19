---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 1.6.0.1
---

# config.yml

文件：`config.yml`。版本：`1.6.0.1`。

主配置。

## `Language` { #language }

```yaml title="config.yml · Language"
# 要使用的语言文件。
Language: EN
```

## `LanguageDownload` { #languagedownload }

```yaml title="config.yml · LanguageDownload"
# 是否从 GitHub 仓库自动下载默认语言文件。
# 如果使用 EN，或已经配置好所用语言且无需下载其他语言，可以禁用此项。
LanguageDownload: true
```

## `AutoUpdate` { #autoupdate }

```yaml title="config.yml · AutoUpdate"
# 启用后，插件会尝试自动将 CMILib 更新到最新版本。
AutoUpdate: false
```

## `ExploitPatcher` { #exploitpatcher }

```yaml title="config.yml · ExploitPatcher"
ExploitPatcher:
  Placeholders:
    blocked:
      # 默认屏蔽 PAPI 的 %checkitem_...% 占位符，以避免其可能引发的严重问题。
      # 仅在已有专门的防护措施时才关闭此项。
      checkItem: true
```

## `Skins` { #skins }

```yaml title="config.yml · Skins"
Skins:
  # 从 Mojang 在线服务器更新皮肤信息的间隔，单位：分钟。
  # 请注意，服务器每分钟只能发送 1 次请求，因此应设置合理的间隔，例如一小时或更久。
  # 例如，设为 1 小时后，只有玩家已有皮肤信息超过 1 小时，才会更新该玩家的皮肤信息。
  # 此操作仅在玩家加入服务器或手动更换皮肤时触发。
  SkinUpdateTimer: 1320
  # 向 Mojang 服务器发送请求的间隔，单位：分钟。
  # 此项用于限制一定时间内的请求数量，避免可能出现的请求过于密集。
  SkinRequestFrequency: 10
```

## `GlobalGui` { #globalgui }

```yaml title="config.yml · GlobalGui"
GlobalGui:
  # GUI 的空白格需要填充时使用的物品类型。
  EmptyField: BLACK_STAINED_GLASS_PANE
  Pages:
    # 界面中“上一页”按钮的图标。
    Previous: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMzdhZWU5YTc1YmYwZGY3ODk3MTgzMDE1Y2NhMGIyYTdkNzU1YzYzMzg4ZmYwMTc1MmQ1ZjQ0MTlmYzY0NSJ9fX0=
    # 界面中“下一页”按钮的图标。
    Next: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjgyYWQxYjljYjRkZDIxMjU5YzBkNzVhYTMxNWZmMzg5YzNjZWY3NTJiZTM5NDkzMzgxNjRiYWM4NGE5NmUifX19
    # 界面中“信息”按钮的图标。
    Middle: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvZmEyYWZhN2JiMDYzYWMxZmYzYmJlMDhkMmM1NThhN2RmMmUyYmFjZGYxNWRhYzJhNjQ2NjJkYzQwZjhmZGJhZCJ9fX0=
  # 界面中“关闭”按钮的图标。
  Close: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzM4YWIxNDU3NDdiNGJkMDljZTAzNTQzNTQ5NDhjZTY5ZmY2ZjQxZDllMDk4YzY4NDhiODBlMTg3ZTkxOSJ9fX0=
  # 界面中“信息”按钮的图标。
  Info: head:eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMjcwNWZkOTRhMGM0MzE5MjdmYjRlNjM5YjBmY2ZiNDk3MTdlNDEyMjg1YTAyYjQzOWUwMTEyZGEyMmIyZTJlYyJ9fX0=
```

## `Spawners` { #spawners }

```yaml title="config.yml · Spawners"
Spawners:
  # 使用 spawner:random 变量时可供选择的刷怪笼列表。
  mysterySpawners:
  - skeleton
  - zombie
  - silverfish
  - panda
  - fox
```

## `RMCCommands` { #rmccommands }

```yaml title="config.yml · RMCCommands"
RMCCommands:
  # 启用后，使用 rmc 命令时会(在可行的情况下)附上所执行的具体命令。
  ConsoleLog: true
```

## `Images` { #images }

```yaml title="config.yml · Images"
Images:
  # 用于构成图像区域的字符。
  # 此处不支持颜色代码。
  # 由于部分图像已经缓存，此设置在服务器重启后才会完全生效。
  Filler: ⬛
  # 用于填充图像空白区域的字符。
  # 此处支持颜色代码。
  EmptyFiller: '&7_|'
```

## `Colors` { #colors }

```yaml title="config.yml · Colors"
Colors:
  # 启用后，除 {#f6f6f6} 和 {#red} 外，插件还会尝试识别 #f6f6f6 或 #ff6 等简写的十六进制颜色代码。
  # 请注意，这会增加额外的检查；简写格式不支持渐变或颜色名称，这两种情况仍需使用较完整的格式。
  OfficialHex: true
  # 启用后，除 {#f6f6f6} 和 {#red} 外，插件还会尝试识别 &#f6f6f6 或 &#ff6 等特殊格式的十六进制颜色代码。
  # 请注意，这会增加额外的检查；特殊格式不支持渐变或颜色名称，这两种情况仍需使用较完整的格式。
  QuirkyHex: true
  # 定义语言文件使用的全局聊天颜色。
  # 此项可让你同时修改多处颜色。
  Global:
    # 使用 {gcp} 引用此颜色。默认值：{#gold}
    # 普通文本使用的主要颜色。
    Primary: '{#gold}'
    # 使用 {gcs} 引用此颜色。默认值：{#yellow}
    # 通常用于变量和占位符。
    Secondary: '{#yellow}'
    # 使用 {gcw} 引用此颜色。默认值：{#FF7357}
    # 用于提示命令用法有误，通常不如错误提示重要。
    Warning: '{#FF7357}'
    # 使用 {gcn} 引用此颜色。默认值：{#gray}
    # 较为中性的颜色，用于无需引起过多注意的文本。
    Neutral: '{#gray}'
    # 使用 {gcu} 引用此颜色。默认值：{#59C959}
    # 表示正面结果的颜色，例如创建家传送点记录。
    Uplift: '{#59C959}'
    # 使用 {gcd} 引用此颜色。默认值：{#E89280}
    # 表示负面结果的颜色，例如移除家传送点记录。
    Downlift: '{#E89280}'
    # 使用 {gce} 引用此颜色。默认值：{#red}
    # 用于提示严重错误。
    Error: '{#red}'
```
