---
title: "声音"
source_url: "https://wiki.itemsadder.com/adding-content/adding-sounds"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 声音

## 将文件从 `MP3` 转换为 `OGG`

使用[此网站](https://misieur.me/audio-converter/)将文件（`mp3`、`wav` 等）转换为 `ogg`（也可使用[这个网站](https://audio.online-convert.com/convert-to-ogg)）。

**重要**

记得将“Channels”设为 `Mono`，否则会出现[音频问题](https://bugs.mojang.com/browse/MC-146721)

## 创建声音

### 新方法

**需要 ItemsAdder 4.0.12 或更高版本。旧版方法见下方。**

#### 普通声音

将声音文件放入 `contents/my_sounds/sounds/sound_1.ogg`。

```yaml
info:
  namespace: my_sounds
minecraft_lang_overwrite:
  my_lang_overwrite:
    entries:
      sound.sound_1: "Sound 1"
    languages:
    - ALL
sounds:
  sound_1:
    path: bruh
    settings:
      subtitle: sound.sound_1
```

#### 唱片机歌曲（Minecraft 1.21.1 及以上版本）

指南

### 旧方法（ItemsAdder 4.0.10 及以下版本）

<details>

<summary>点击查看旧方法</summary>

### 步骤 1

* 新建文件夹 `ItemsAdder/contents/my_sounds/resourcepack/my_sounds/sounds/`\
  （已有文件夹时也可使用现有的）
* 将 **`.ogg`** 文件放入其中。\
  还可以在 `sounds` 中创建更多文件夹来整理声音。\
  例如 `effects`、`music` 等。

本例将名为 **`song_1.ogg`** 的文件放入新建的 `music` 文件夹。\
因此，文件现在位于 `contents/my_sounds/resourcepack/my_sounds/sounds/music/song_1.ogg`

### 步骤 2

* 打开文件夹 `contents/my_sounds/resourcepack/my_sounds/`
* 新建名为 `sounds.json` 的文件（已有时打开现有文件）
* 这是一个 `.json` 文件，必须按正确格式编写，否则不会生效。

按以下方式将声音添加到文件中：

<p class="code-title"><code>contents/my_sounds/resourcepack/my_sounds/sounds.json</code></p>

```json
{
	"music.song_1":{
		"sounds":[
			"my_sounds:music/song_1"
		]
	}
}
```


**下面说明各部分代码的含义**

这是声音名称。你将在插件的每个部分以及 Minecraft 原版的 [/playsound ](https://www.digminecraft.com/game_commands/playsound_command.php)命令中使用它。

```
"music.song_1":{
```

这是当你调用声音名称时 Minecraft 将播放的声音文件列表。\
Minecraft 将随机播放其中一个声音（仅当你设置了多个声音时）。

<div class="admonition warning" markdown="1">
请记住，如果你的命名空间名称不同，你必须将 `my_sounds` 更改为你自己的命名空间名称！
</div>

<pre class="language-javascript"><code class="lang-javascript">"sounds":[
<strong>    "my_sounds:music/song_1"
</strong>]
</code></pre>

例如，如果你想为同一个声音名称设置随机声音，只需创建多个 `.ogg` 文件并像这样放置它们：

```
"sounds":[
    "my_sounds:music/song_1_variant_1",
    "my_sounds:music/song_1_variant_2",
    "my_sounds:music/song_1_variant_3"
]
```

**如何在 `sounds.json` 文件中添加多个声音？**

很简单，下次你想添加声音时，只需在末尾添加一个逗号，如下所示。\
（我指的是第 6 行的逗号）

```json
{
    "music.song_1":{
        "sounds":[
            "my_sounds:music/song_1"
        ]
    },
    "music.song_2":{
        "sounds":[
            "my_sounds:music/song_2"
        ]
    }
}
```

<div class="admonition warning" markdown="1">
可使用此网站检查 `sounds.json` 文件是否存在错误：[https://jsonformatter.curiousconcept.com/](https://jsonformatter.curiousconcept.com/)
</div>

</details>
