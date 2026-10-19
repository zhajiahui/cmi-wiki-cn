
# Player Emotes

## Emotes / Gestures

Emotes allow you to express yourself with some particular player animations.\
They integrate perfectly with the game and look like an official update.


Thanks so much to **Misieur** (**Thomas**) which helped me to implement this new method with his ideas 🩷

```yaml
emotes:
  1_21_4_plus_modern_method: true
```

#### Main features

* [Blockbench](https://www.blockbench.net/) extension to animate the Minecraft player model
* Completely Async, no TPS drops
* Optimized for big servers
* Play sounds and particles in animations
* Shows items in player hands and helmet
* Doesn't overwrite any vanilla shader
* Compatible with shader mods (Optifine, Iris, etc.)
* Supports slim arms
* Doesn't cause any issue with placed player heads (skulls)

#### Limitations

* Requires Minecraft 1.21.4 or greater
* More info about emotes issues [here](/faq/emotes-issues.md)

```yaml
emotes:
  legacy_shaders: true
  1_21_5_to_1_21_9_shaders: true
```

#### Main features

* [Blockbench](https://www.blockbench.net/) extension to animate the Minecraft player model
* Completely Async, no TPS drops
* Optimized for big servers
* Play sounds and particles in animations
* Shows items in player hands and helmet

#### Limitations

* Won't show the player armor equipment, only mainhand, offhand and helmet.
* Works only on 1.17 to 1.21.3 clients
* More info about emotes issues [here](/faq/emotes-issues.md)

## Installing the Blockbench extension

**Before continuing:**

* Make sure you're running **Blockbench 4.7.4** or **greater**
* Make sure you're running the latest ItemsAdder and latest ItemsAdder Blockbench extension

[Download Blockbench](https://www.blockbench.net/) (don't use the web app).

![](<../../.gitbook/assets/entities_004.png>)

\
[Download](https://github.com/LoneDev6/itemsadder-entity/releases) the extension file.

<figure><img src="../../.gitbook/assets/player-emotes_006.png" alt=""><figcaption></figcaption></figure>

Then open **Blockbench** and click on File -> Plugins.

![](<../../.gitbook/assets/player-emotes_005.png>)

Click on the icon to load plugins from file, then select the file `iaentitymodel.js`.

![](<../../.gitbook/assets/player-emotes_004.png>)

Press OK

![](<../../.gitbook/assets/player-emotes_003.png>)

## Enabling emotes

Open `config.yml` of ItemsAdder and enable these two options, then run `/iazip` command.

```yaml
entities:
  custom-entitites:
    enabled: true
    emotes: true
```
