## Plugins

A lot of errors that seem to be caused by ProtocolLib are caused by a plugin that uses it. Removing ProtocolLib will seem to fix the error because those plugins won't function without it. A relatively quick way to figure out which plugin is causing the issue is to manually perform a [binary search](https://www.geeksforgeeks.org/binary-search/). First, run `/protocol dump` and check the bottom section to see which plugins are using it. Then, remove half of the plugins and see if the issue is still happening. If so, remove the other half. If not, do your binary search again on that subset because the other half is likely fine. Continue doing this with smaller subsets of your plugins until you find the culprit.
***

## FieldAccessException

This error generally means that a plugin hasn't updated for a new Minecraft version. Report this to the plugin author. If you are a plugin author and are confused or there is no plugin in the stack trace, feel free to open an issue.
***

## IllegalAccessError/NoSuchMethodError for ProtocolLogger

One of your plugins is misbehaving and including part of ProtocolLib in its own jar. Your best bet is to go through the largest jars in your plugins folder as it will contain a lot more classes than it should. Search for `com/comphenix/protocol` folders in the jars using a tool like 7-zip, WinRar, or Vim.
***

## NoClassDefFoundError for BaseComponent

Use the [latest dev build](https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/) or switch to Spigot
***

## IllegalArgumentException: Unable to find findStatistic

Update to either the [latest release](https://github.com/dmulloy2/ProtocolLib/releases) or [dev build](https://ci.dmulloy2.net/job/ProtocolLib/lastSuccessfulBuild/)