## This Page

If you were sent to this page, you are running:

- A **cracked version of Minecraft**
- A server that supports users of Minecraft cracks
- Or a server running in **offline-mode** for any given reason.
- This is also sometimes used as a reference for cracked plugins, and most (though not all) of the contents on this page still apply.

## Common Misunderstandings

### "Premium"

It is important to be aware that there is no such thing as a "**premium**" Minecraft account.

You either have an account (a validly registered and purchased Mojang account) or you don't.

If you do not have an account and are still playing Minecraft, you are running a cracked client.

### "But Offline Is A Built-In Feature"

Some users claim that offline mode can't be illegal because it's a built-in feature.

This is a simple misunderstanding: Offline mode indeed isn't illegal... but using offline mode to allow cracked copies of minecraft to join your server **is**.

The actual purpose of the `online-mode=false` is exactly what it says on the tin and nothing more: when you don't have internet access. Offline mode is so you can play minecraft on LAN while offline.

### "But I Need It To Test Multiple Players"

Some users claim that they've downloaded a crack to test some plugin or script with multiple players.

Downloading cracks is downloading cracks. Running cracked is running cracked. There isn't an excuse. You're still risking malware, you're still committing a crime.

Your options for testing are:

- A: Buy a second account if you really need to test on your own.
- B: Use an NPC or similar where possible.
- C: Just... ask somebody to come help you test. If you're able to find people to play on a server, you should definitely also be able to find people willing to help test. Just poke a friend and ask them to open minecraft and sit idle on your test server.

## Legality

Minecraft cracks are **illegal software piracy**.

Creating, downloading, using, possessing, or distributing a Minecraft crack is a **crime**.

You should never download, use, or distribute illegal software.

## Safety Warning

It is well known that most Minecraft cracks contain **malware** (which, in general, is common for most pirated software).

Your computer may be at risk or have been infected with malware if you install or have installed a Minecraft crack.

## Cracked Servers Are Limited

An important limitation of both cracked clients and offline-mode servers is reduced and/or altered functionality.

Cracked clients and offline-mode servers *cannot access* some functionality of Minecraft that is available in legitimate installations.

As such, *even if* we chose to support offline-mode servers, we would be *unable* to.

Many errors and strange behaviors result from hosting an offline-mode server, and often do not appear on online-mode servers at all.

As a result, issues on offline-mode servers cannot be addressed in the same way we can address issues found on online-mode servers.

## Supportability

While generally **plugins can run and will work** for the most part, **we cannot and will not give support for offline-mode** servers in any issues pages, forum threads, chatrooms, or other support lines.

For Discord, we are explicitly forbidden from providing support to cracked servers per the [Discord Guidelines](https://discord.com/guidelines): `Do not distribute or provide access to content involving the hacking, cracking, or distribution of stolen goods, pirated content, or accounts. This includes sharing or selling game cheats or hacks.` If you run a cracked minecraft server that has a community on Discord, that community may also be violation of this Discord platform rule.

## Consequences Of Offline-Mode

Be aware as well that having a server that was in offline mode even momentarily and then changed to online mode after can have lasting consequences, making it dangerous to do things like "just quickly change to offline to test something".

If you are running an offline mode server and are going to fix that, the best way to reduce risk of trouble here is to delete player data (stored in a folder labeled "playerdata" within each world).

## General Risks of an Offline-Mode Server

Alongside to the technical support warnings, it should be noted that offline-mode servers are open to attacks that aren't possible on online-mode servers, such as fake player flooding attacks and banned users returning under a different username (sometimes with a different IP address as well).

Additionally, attacks that are possible on both offline and online mode servers, such as DDoS attacks, are more common on offline-mode servers(in part due to lower fear of consequences from angry players), and in some cases even more easily done (from the lack of official Minecraft safety systems like the account authenticator, as well as availability of things that simply don't work correctly in offline mode).

## How To Do It Right

Your server should **always** be in online-mode (this is a setting within your `server.properties` file, there should be a line that reads `online-mode=true`).

### Bungee

The only case when offline-mode can be used on a server is when Bungee is in use. Bungee is a proxy that has its own online-mode functionality, which should be enabled, and your server should have all ports other than the Bungee port blocked by a firewall (otherwise the Bungee online-mode functionality can be bypassed and broken). Additionally, ensure the `bungeecord` setting in `spigot.yml` is set to true.

### Velocity

Velocity proxies work the same as Bungee as explained above, only change is instead of 'bungeecord' in 'spigot.yml' you need to enable `velocity: enabled:` in `config/paper-global.yml`

## Historical Geyser Note

~~Special Extra Note on Geyser and "Floodgate"~~

~~Geyser is server software that enables Minecraft: Bedrock Edition players to join Minecraft: Java Edition servers. "Floodgate" is an extension to Geyser that removes the requirement to own a legitimate Java Edition account. Despite both games being "Minecraft", they are two different games sold separately, at different prices, under different license agreements. As such, "Floodgate" is technically a form of cracked software. If you want Bedrock/Java crossplay through Geyser, you must use standard Geyser with its requirement that Bedrock players still use their Java Edition account login.~~

~~See also the [Minecraft Bedrock/Java FAQ Page](https://help.minecraft.net/hc/en-us/articles/360050865492-JAVA-Account-Migration-FAQ) which says "DOES HAVING A MICROSOFT ACCOUNT ENABLE ME TO PLAY WITH MY FRIENDS ON OTHER PLATFORMS? No. If you play Java Edition, you can still only play with other players who have Java Edition."~~

~~Many in the community, us included, really hope that Mojang will one day close the separation and allow both Java and Bedrock players to freely crossplay without restriction. Until they officially enable this, you will have to have specifically a valid Java Edition account to player on Java servers.~~

*EDIT*: While the above still holds true, recent changes to available licensing and continued lack of clear information from Mojang means we will no longer enforce this is a rule in our support channels until/unless Mojang takes action to enforce it themselves, or announces clear intent to.
