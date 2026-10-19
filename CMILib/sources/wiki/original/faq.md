## What is CMI Library (CMILib)?

The plugin helper, or **library**, is a handy tool that helps us easily manage common phrases, hex colors, and more. Instead of each plugin having its own code for these things, the plugin helper allows multiple plugins to share the same code. This reduces the overall size of our plugins and makes updating and maintaining these plugins a lot simpler and more consistent.

## How do I get it?

You can get latest version from <https://www.spigotmc.org/resources/87610/> or <https://www.zrips.net/cmilib/>

## Which plugins use this?

The full list as of June, 2023

- **CMI** version 9.x.x.x and up
- **Selection Visualizer** version 3.x.x.x and up
- **TryMe** version 7.x.x.x and up
- **Mob Farm Manager** version 2.x.x.x and up
- **Residence** version 5.x.x.x and up
- **Jobs-Reborn** version 5.x.x.x ad up
- **BottledExp** version 3.x.x.x and up
- **Recount** version 3.x.x and up
- **TradeMe** version 6.x.x.x and up

These all currently support Spigot-, and Paper server versions 1.20.x and lower, and require the latest CMILib version to properly operate.

## I have updated locale but it did not update?

As CMILib is a separate library by itself, you will need to reload its config file with **/cmil reload** command for changes to take effect

## Do I have to restart?

If you started the server with the latest version, then no, it should be picked even if you have multiple plugin versions. But in case CMILib downloaded the latest version during server operation time, you will need to restart the server for the new version to take effect.

## Backing up and testing?

Yes, I strongly recommend to always backing up your whole server before making changes, such as plugin updates, even if it’s basic minor update, always keep server backup as a good habit. Test the upgrade with CMILib first. If it fails you can at least roll back to your backup as if nothing happened.

## I have multiple versions, what to do?

The plugin should automatically remove the oldest versions, if that fails you can always do it manually, but make sure that you are removing ones that are not currently loaded in, otherwise it will produce errors. The safest way would be to stop the server and then remove older versions.

## OMG, I had CMI with Lib 1.0.0.2 then TryMe with Lib 1.0.1.0 and now Residence with Lib 1.0.2.3?!

No need to panic, only one version is used and it should be the latest one for all supported plugins. Independent which plugin you have, always use the latest version of the library file.

## I keep deleting this CMILib jar and it keeps coming back!

CMILib is required for plugins to work properly, so you can’t use them without this plugin. Only older versions support independent work but those won’t be maintained any longer.

## Can I see the CMILib source code?

You can find the source code in this Github repository. <https://github.com/Zrips/CMILib>
