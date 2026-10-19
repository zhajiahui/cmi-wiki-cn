If you were sent to this page, you are:

- Having trouble getting Citizens to run
- Asking for help while being on an unsupported Minecraft version
- Asking for help related to a possible bug, but are on an unsupported or limited supported Minecraft version
- Unable to update because of a plugin that does not support the latest patch version

This page explains what you can and should do, while also providing other helpful tools, to help you maintain your server.

### Running a server requires maintenance

We know that running a Minecraft server can be rewarding and fun, but unfortunately it also requires work to maintain, even if you purchase a setup.
It's crucial to keep your server updated, because new versions come with security patches, bugfixes, and features for players.

For instance, the [Log4Shell](https://en.wikipedia.org/wiki/Log4Shell) exploit demonstrates how outdated versions can leave servers vulnerable to severe security threats.

Regular backups are essential to ensure the safety of your Minecraft server's data.
A simple way to make them is to .zip or .tar your Minecraft server and download it with a FTP client from your servers host. If you’re looking for more advanced tools, you might consider using BorgBackup. It allows you to make backups automatically for free.

### Which Versions does Citizens support?

Citizens supports multiple versions of Minecraft, but due to Spigot file size limits, limited development time, and security risks and bugs that come with older Minecraft versions, the actively supported versions change over time.

As a general rule of thumb, only the latest patch version of each of the three most recent Minecraft major releases is fully supported. For example in Minecraft 1.20, the latest patch version is 1.20.6 and so the latest version of Citizens will only work with Minecraft Version 1.20.6, not 1.20 or 1.20.4.

However, the exact versions may vary based on their usage data from bStats or Spigot file size limitations. This means that in some cases, a version may be skipped. For example, Citizens may support versions 1.19.4, 1.21.4, 1.22.1 and dropping support for 1.20.6 instead of 1.19.4, due to low usage or technical constraints.

Some versions receive only limited support, meaning we will answer basic questions but cannot fix bugs or add feature requests on these specific versions, and the latest Citizens version will not run on them. On older versions that are not supported, we won't provide any assistance until you move to a supported version. If you are on 1.8 see [Minecraft 1.8](https://wiki.citizensnpcs.co/Minecraft_1.8 "Minecraft 1.8").

When Minecraft releases a new update, we provide limited support for the previous version for a short period. For example, if the latest version is 1.21.4, we may still offer limited support for 1.21.3.

You can find the latest Citizens dev build [here](https://ci.citizensnpcs.co/job/citizens2/). If you are looking for older builds you can find links to them in the #news channel on our [Discord](https://discord.gg/Q6pZGSR). Be aware that you might be end up entirely on your own and lose the chance of getting support.

## What to do?

### Having trouble getting Citizens to run

If you have trouble getting Citizens to run, you probably noticed a line like

```
Error occurred while enabling Citizens v2.0.37-SNAPSHOT (build 3648) (Is it up to date?)
```

in your latest.log file. This line usually means that either your Minecraft version or Citizens is not up to date.
In this case you need to [update your Minecraft server](https://wiki.citizensnpcs.co/Supported_Versions#How_to_update_a_Minecraft_server). We know that this can be difficult, especially if you just set your server up or purchased a setup. However, server maintenance is critical as explained above.

If you host your server on a free host and have trouble updating your server, please see [this](https://wiki.citizensnpcs.co/Frequently_Asked_Questions#I_have_a_free_server_(Aternos,_Minehut,_...)_but_there's_problems).

### Unable to update because of a plugin that does not support the latest patch version

Sometimes, a plugin you rely on may prevent you from updating your server. This can happen when the plugin is not maintained anymore, a Minecraft update happened with complex changes that require more time and work for the plugins developer, or the maintenance of the plugin is community driven.

Verify if the plugin is still being maintained. The plugin's author may have discontinued development. Look for updates on the plugin's official website, official Discord, or Spigot/Hangar page. If the plugin has not been updated in the past year, it's likely no longer maintained. If the plugin is no longer maintained, consider finding an alternative that offers similar functionality and is actively supported and update your server.

### Asking for help on an unsupported Minecraft version

As earlier explained Citizens does not support all versions of Minecraft. If you are on an outdated version, we unfortunately cannot provide support for it.

Please update your Minecraft server to a version that we fully support.
Once you’ve updated your server, feel free to reach out to us for help!

### Reporting a potential bug, but on an unsupported Minecraft version

If you're encountering a bug on an unsupported or limited supported version, especially on the latest Minecraft major release, the issue may have already been fixed in the latest Citizens version. So please update your Minecraft server to a patch version that we support.

If you cannot update because a Plugin prevents you from it because it does not support this version yet or you are using Paper and the latest version is not stable yet, it's not a problem!

Please help us by attempting to replicate the behavior on a local test server on the latest patch version. If you can successfully replicate the issue, provide your latest.log from the updated server and tell us the steps to reproduce this issue, so we can troubleshoot further.

## How to update a Minecraft server

Updating a Minecraft server is a simple straightforward process, but it’s crucial to approach it carefully to avoid running into issues. The following explanation covers the basic process.

#### Have a backup on hand

Before making any changes, make sure you have a working backup of your server. Just in case something unpredictable happens and you need to restore it.

#### Test the update locally on your computer

Perform a dry run by downloading and running your server locally on your computer and updating it. To do that, you need to:

- Replace the server's .jar file and any plugin .jar file with the updated version you have downloaded from the related plugins page.
- Start your server and check the logs for errors and warnings.
- Log in to your local server and test important things that must work.

If you don’t see issues coming up, you are likely good to update.

If you encounter issues:

- Check the related plugin's official page or support channels for news.
- Look for help on the plugin's Discord server, if any exists.

#### Proceed to update your production server

Once you're confident with your local tests, proceed with updating your production server.
