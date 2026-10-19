> Native Major MC Version:
> :   1.21
>
> Tested Major MC Versions:
> :   - 1.8
>     - 1.9
>     - 1.10
>     - 1.11
>     - 1.12
>     - 1.13
>     - 1.14
>     - 1.15
>     - 1.16
>     - 1.17
>     - 1.18
>     - 1.19
>     - 1.20
>     - 1.20.6
>     - 1.21
>
> Source Code:
> :   <https://github.com/dmulloy2/ProtocolLib/>
>
> Contributors:
> :   dmulloy2 and aadnk
>
> Donation Link:
> :   <https://github.com/sponsors/dmulloy2>
>
> ProtocolLib  
> **Use the [dev build](https://github.com/dmulloy2/ProtocolLib/releases/tag/dev-build) for 1.8 through 26.2**  
>   
> *Thanks for over 3 million downloads everyone!*  
>   
> If you love ProtocolLib or it has made your life significantly easier, consider a one-time **[donation](https://paypal.me/dmulloy2), [sponsoring](https://github.com/sponsors/dmulloy2)** the project or leaving a positive review below. It really means a lot!  
>   
> Certain tasks are impossible to perform with the standard Bukkit API and may require working with and even modifying Minecraft directly. A common technique is to modify incoming and outgoing packets or to inject custom packets into the stream. This is quite cumbersome to do, however, and most implementations will break as soon as a new version of Minecraft has been released, mostly due to obfuscation.  
>   
> ProtocolLib is a library that allows read and write access to the Minecraft protocol. It handles most of the overhead required with reflection and channel injection and provides wrappers to simplify packet modification. It is updated with most Minecraft updates so, ideally, individual plugins don't have to. ProtocolLib often doesn't need to be updated for minor updates, especially if there are few code changes (i.e. the 1.8 security updates)  
>   
> Useful Links  
>
> - [Releases](https://github.com/dmulloy2/ProtocolLib/releases)
> - [Source Code](https://github.com/dmulloy2/ProtocolLib)
> - [Issue Tracker](https://github.com/dmulloy2/ProtocolLib/issues)
> - [JavaDoc](https://dmulloy2.net/ProtocolLib/javadoc/)
>
> Support  
> Before reporting a bug:  
>
> - Look for an update for ProtocolLib, there's a good chance your error or bug has already been fixed.
> - [**Read the stack trace**](https://bukkit.org/threads/how-to-read-stack-traces-and-troubleshoot-your-own-plugins-by-yourself.32457/) and make sure it's an error with ProtocolLib. ProtocolLib's package is com.comphenix.protocol. If you don't see that anywhere, it's *not* ProtocolLib.
> - **[Check the common errors wiki page](https://github.com/dmulloy2/ProtocolLib/wiki/Common-Errors).**
>
> When reporting a bug:  
>
> - Use the [**issue tracker**](https://github.com/dmulloy2/ProtocolLib/issues)! *Don't report bugs in the reviews*. Please search for duplicates before reporting a new issue!
> - Provide as much information as possible. Provide your ProtocolLib version and Spigot version.
> - Provide any stack traces or "errors" using **[pastebin](http://pastebin.com/)**.
>
> For server operators  
> Just download ProtocolLib from the link above. It doesn't do anything on its own, it simply allows other plugins to function.  
>   
> For developers  
> A somewhat dated tutorial can be found [here](https://dev.bukkit.org/projects/protocollib/pages/tutorial). A new tutorial is in progress [on the wiki](https://github.com/dmulloy2/ProtocolLib/wiki).  
>   
> TinyProtocol  
> There is a lightweight alternative to ProtocolLib called TinyProtocol. It is essentially a mechanism to send and receive raw packets without structure modifiers or wrappers. It can be found [here](https://github.com/dmulloy2/ProtocolLib/tree/master/TinyProtocol/src/main/java/com/comphenix/tinyprotocol).  
>   
> Maven repository  
> If you're using Maven, you'll be able to automatically download the jar, JavaDoc and associated sources from Maven Central. This repository is included by default if you're using Maven, but you must declare it explicitly in Gradle:  
>
> ```
> repositories {
>     mavenCentral()
> }
> ```
>
> Then add it as a dependency like so:  
>
> ```
> <dependencies>
>   <dependency>
>     <groupId>net.dmulloy2</groupId>
>     <artifactId>ProtocolLib</artifactId>
>     <version>5.4.0</version>
>   </dependency>
>   <!-- And so on -->
> </dependencies>
> ```
>
> Gradle:  
>
> ```
> dependencies {
>    compileOnly 'net.dmulloy2:ProtocolLib:5.4.0'
> }
> ```
>
> **NOTE:** Previously the groupId was com.comphenix.protocol, but it was recently changed to net.dmulloy2 due to the Maven Central migration.  
>   
> Commands  
> Protocol  
> Main administrative command. Supports the following sub-commands:  
>
> - *config*: Reload the configuration file.
> - *check*: Check for new versions on BukkitDev.
> - *version*: Displays the currently running version of ProtocolLib.
> - *timings*: Toggle measuring the amount of CPU time spent by each plugin.
> - *listeners*: Display what plugins are using ProtocolLib, and the packet types they are intercepting.
>
> PacketLog  
> Logs hex representations of the provided packets to a file or to console  
> Syntax: /packetlog <protocol> <sender> <packet> [file/console]  
> Accepted packets can be found [here](https://github.com/dmulloy2/ProtocolLib/blob/master/src/main/java/com/comphenix/protocol/PacketType.java).  
>   
> All of these commands require the permission *protocol.admin*.  
>   
> Configuration  
> A small set of configuration options are available:  
> Global section  
>
> ```
> auto updater.notify: true #Inform any player with the permission protocol.info when a new version of ProtocolLib is out.
> auto updater.download: false #Automatically download and install the newest version of ProtocolLib. The installation will take effect when the server restarts.
> auto updater.delay: 43200 #The number of seconds between each check for a new update.
> auto updater.last: 0 #This simply records the last time (in seconds since 01.01.1970) an update check was performed. Set it to 0 to force a new update check.
> metrics: true #If TRUE, ProtocolLib will publish anonymous usage data to mcstats.org. Set it to FALSE to opt-out.
> background compiler: true #If TRUE, ProtocolLib will try and improve performance by replacing reflection with compiled code on-the-fly.
> ignore version check: None #Force ProtocolLib to start for a specified Minecraft version, even if it is incompatible.
> ```
>
> Compatibility  
> One of the main goals of this project was to achieve maximum compatibility with different versions of Minecraft. And the end result is quite flexible. Aside from package changes, it should be resilient against future changes. It's likely that I won't have to update ProtocolLib for anything but bug fixes and new features.  
>   
> How is this possible? It all comes down to reflection in the end. Essentially, no name is hard coded - every field, method and class is deduced by looking at field types, package names or parameter types. It's remarkably consistent across different versions.  
>   
> Example Plugins  
> Some well-made plugins that do interesting things with ProtocolLib. Check out their source (if available) for some inspiration.  
>
> - [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays)
> - [Advanced Anti Cheat](https://www.spigotmc.org/resources/aac-advanced-anti-cheat-hack-kill-aura-blocker.6442/)
> - [Server List Plus](https://www.spigotmc.org/resources/serverlistplus.241/)
> - [FurnitureLib](https://www.spigotmc.org/resources/furniturelibary-protectionlib.9368/)
> - [AntiAura](https://www.spigotmc.org/resources/antiaura-premium-anti-cheat-plugin.1368/)
> - [PremiumVanish](https://www.spigotmc.org/resources/14404/)
>
> *DM me if you also use ProtocolLib and want to be on the list*  
>   
> Statistics  
> ProtocolLib collects statistics anonymously through BStats. Participation is completely optional and you can opt-out at any time, although it is really helpful in figuring out what environments the plugin is running in (i.e. versions of Spigot, Java, and ProtocolLib), so I can adjust development accordingly.  
>   
> Sponsors  
> If ProtocolLib has made your life significantly easier or you're feeling particularly generous, consider sponsoring the project! It's a great way to support the many hours I've spent maintaining this plugin and keeps me motivated. Please don't sponsor if you can't afford it.  
>   
> <https://github.com/sponsors/dmulloy2>  
>   
> Huge thanks to my sponsors:  
>
> - Fanfaryy
> - SimplyVanilla
> - PebbleHost
> - RaenCallisto
> - Aternos
>
>   
> Donations  
> You can also make a one-time donation via PayPal (or sponsors, see above)  
>   
> [![[​IMG]](//proxy.spigotmc.org/9c91d77a0b024afc1d12d1caa95038bcb209d4b8/68747470733a2f2f7777772e70617970616c6f626a656374732e636f6d2f656e5f55532f692f62746e2f62746e5f646f6e61746543435f4c472e676966)](https://paypal.me/dmulloy2)   
>   
> Huge thanks to those who have donated! ![:)](styles/default/xenforo/clear.png "Smile    :)")  
> *(If I missed you or you want to remain anonymous, shoot me a PM)*  
>
> - nathan818 - $1000
> - InstaAE - $150
> - MineCove - $100
> - Lael - $100
> - joehot200 - $75
> - Techcable - $30
> - VintageDon - $25
> - games647 - $25
> - Photon - $15
> - Ltd-Net - $11
> - CultivateMC - $10
> - Axzial - $10
> - snapsi - $5
> - Aberzhulan - $5
> - Art in the Shade - $5
>
> Please don't leave bug reports in the reviews section. It's the **worst** place to get support and I won't respond. Use the **[issue tracker](https://github.com/dmulloy2/ProtocolLib/issues) (after checking the [common errors page](https://github.com/dmulloy2/ProtocolLib/wiki/Common-Errors) and searching for duplicates)**, where I can actually diagnose and fix your issue.
