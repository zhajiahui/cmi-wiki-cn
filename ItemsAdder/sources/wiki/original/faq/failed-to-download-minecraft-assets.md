
# Failed to download Minecraft assets

ItemsAdder needs some Minecraft assets to work, it automatically downloads them for you, but some server setups might have issues downloading (blocking firewall, network error, etc.).

You can manually download the assets to fix this.

#### Delete the folder

Delete the folder `ItemsAdder/storage/cache/vanilla_assets`

#### Download the assets


<div align="left"><figure><img src="../.gitbook/assets/failed-to-download-minecraft-assets_003.png" alt=""><figcaption></figcaption></figure></div>

#### Extract the `vanilla_assets` folder

Extract the `vanilla_assets` folder into `ItemsAdder/storage/`

<div align="left"><figure><img src="../.gitbook/assets/failed-to-download-minecraft-assets_002.png" alt=""><figcaption></figcaption></figure></div>

#### Done

Start the server and run `/iazip` to regenerate your pack.
