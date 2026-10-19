Vault is a Permissions, Chat, & Economy API to give plugins easy hooks into these systems without needing to hook or depend on each individual plugin themselves. It was born out of a distaste for how both Register and the current Permissions API are run, and their lack of features or over-complicated implementations. Vault attempts to solve these issues by being intuitive and providing plugins with support for any system that they may use.

**Config:**

- update-check
  - turns the update checker on/off

**Permissions:**

- vault.admin
  - allows access to vault info and conversion commands
  - defaults to OP
- vault.update
  - Anyone with this permission will be notified when Vault is out-dated
  - defaults to OP
  - **setting to false in permissions.yml will disable version check messages for console**

**Vault currently Supports:**

---

- **Perms:** Permissions 3, [bPermissions](http://dev.bukkit.org/server-mods/bpermissions/), [PEX](http://dev.bukkit.org/server-mods/permissionsex), [GroupManager](http://dev.bukkit.org/server-mods/groupmanager), [PermissionsBukkit](http://dev.bukkit.org/server-mods/permbukkit), [zPermission](http://dev.bukkit.org/server-mods/zpermissions), SimplyPerms, [Privileges](http://dev.bukkit.org/server-mods/Privileges), [DroxPerms](http://dev.bukkit.org/server-mods/DroxPerms), xPerms
- **Econ:** [iConomy](http://dev.bukkit.org/server-mods/iconomy) 4,5,6, [BOSEconomy](http://dev.bukkit.org/server-mods/boseconomy) 6 & 7, EssentialsEcon, 3Co, [MultiCurrency](http://dev.bukkit.org/server-mods/multicurrency), [MineConomy](http://dev.bukkit.org/server-mods/mineconomy), [eWallet](http://dev.bukkit.org/server-mods/ewallet), [EconXP](http://dev.bukkit.org/server-mods/econxp/), [CurrencyCore](http://dev.bukkit.org/server-mods/currency/), [CraftConomy](http://dev.bukkit.org/server-mods/craftconomy/), AEco, [Gringotts](http://dev.bukkit.org/server-mods/gringotts/)
  - Bank support in CraftConomy, CurrencyCore, BOSE & iCo6 only
  - iCo6/CurrencyCore use merged player/bank accounts. It's suggested to use BOSE for full featured banks.
  - iCo6 flatfile has SEVERE bugs, USE AT YOUR OWN RISK
- **Chat:** [mChat](http://dev.bukkit.org/server-mods/mchat), iChat, [bPermissions](http://dev.bukkit.org/server-mods/bpermissions/), [PEX](http://dev.bukkit.org/server-mods/permissionsex), P3, [DroxPerms](http://dev.bukkit.org/server-mods/DroxPerms)
- Other economies/permissions systems may have built-in support for Vault, check with them to be sure.

---

- JavaDocs: [http://milkbowl.github.io/VaultAPI](/linkout?remoteUrl=http%253a%252f%252fmilkbowl.github.io%252fVaultAPI)
- GitHub (SourceCode): <https://github.com/MilkBowl/Vault/>
- GitHub (SourceCode): <https://github.com/MilkBowl/VaultAPI/>

---

This plugin utilizes Hidendra's plugin metrics system. the following information is collected and sent to bstats.org unless opted out:

- A unique identifier
- The server's version of Java
- Whether the server is in offline or online mode
- Plugin's version
- Server's version
- OS version/name and architecture
- core count for the CPU
- number of players online
- Metrics version
- Which Chat, Economy, and Permission hook is in use.

Opting out of this service can be done by editing plugins/bstats/config.yml and changing opt-out to true.

---

### Linking Vault

**There's a slightly longer/more detailed example on the Vault github page on how you might link to vault in a plugin. See: <https://github.com/MilkBowl/VaultAPI>**

The following 3 methods can be used along with the 3 variables to load both the permission, economy, and chat systems from Vault. Make sure to add **depend: [Vault]** to your plugin.yml - You don't need to use all 3 if you don't want to in your plugin! If you only want one or two of the three APIs only use those ones you need!

**NOTICE: Vault automatically logs what Plugins it found and hooks to, there is no need to display this information in your plugin.**

**NOTICE: Don't Forget To add softdepend: [Vault] or depend: [Vault] to your plugin.yml**

```
    public static Permission permission = null;
    public static Economy economy = null;
    public static Chat chat = null;

    private boolean setupPermissions()
    {
        RegisteredServiceProvider<Permission> permissionProvider = getServer().getServicesManager().getRegistration(net.milkbowl.vault.permission.Permission.class);
        if (permissionProvider != null) {
            permission = permissionProvider.getProvider();
        }
        return (permission != null);
    }

    private boolean setupChat()
    {
        RegisteredServiceProvider<Chat> chatProvider = getServer().getServicesManager().getRegistration(net.milkbowl.vault.chat.Chat.class);
        if (chatProvider != null) {
            chat = chatProvider.getProvider();
        }

        return (chat != null);
    }

    private boolean setupEconomy()
    {
        RegisteredServiceProvider<Economy> economyProvider = getServer().getServicesManager().getRegistration(net.milkbowl.vault.economy.Economy.class);
        if (economyProvider != null) {
            economy = economyProvider.getProvider();
        }

        return (economy != null);
    }
```

---

## Repository Information for Maven Projects

```
<repository>
	<id>vault-repo</id>
	<url>http://nexus.hc.to/content/repositories/pub_releases</url>
</repository>
```

---
