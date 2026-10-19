
# Hide Scoreboard Background and Numbers

## Hide scoreboard numbers

![With ItemsAdder](<../.gitbook/assets/hide-scoreboard-numbers-1-17_001.png>)

![Without ItemsAdder](<../.gitbook/assets/hide-scoreboard-numbers-1-17_002.png>)

### 1.20.3 and greater clients

* Works only on **Minecraft 1.20.3+** clients
* **Works only on Minecraft 1.20.3+ servers!**
* Doesn't edit the `rendertype_text` shader files and doesn't use any shader

```yaml
effects:
  hide-scoreboard-numbers: true
```

This option doesn't require `/iazip` to be toggled on/off.\
You can change this value and simply run `/iareload` to apply.

### Any client version

* This feature works only on **Minecraft 1.17+** clients
* **Server version doesn't matter**
* Edits the `rendertype_text` shader files

```yaml
effects:
  hide-scoreboard-numbers-old-clients: true
```

**Warning**

This option is permanent and cannot be turned on/off in-game.\
You have to disable it in the `config.yml` and regenerate the pack again to enable/disable it (using `/iazip`).

## Hide background

* **Works in all Minecraft versions**
* **Doesn't edit** `rendertype_text` **shader to work.**

### Plugin: AnimatedScoreboard

[animatedscoreboard.md](/compatibility-with-other-plugins/compatible/animatedscoreboard.md)

### Plugin: Scoreboard-revision <mark style="color:orange;">(Outdated)</mark>

[scoreboard.md](/compatibility-with-other-plugins/compatible/scoreboard.md)
