MythicMobs has a very powerful pack system to organize ALL your files better, and also get packs from Vendors through sources like MCModels installed very easily.

Simply make a folder inside the MythicMobs/Packs folder (name it whatever you want for your pack), and then inside of it you can make folders for Items, Mobs, Skills, RandomSpawns, etc just like you can in the base MythicMobs directory. Inside these folders you can treat it just like the base folders as well putting as many files for the respective type as you want. Easy to zip up and then hand out!

# Folders and Files {#folders-and-files}

A pack can contain many folders and files. The following is a (non-comprehensive, for now) list of what you might use

## Pack Info {#pack-info}

When making a Pack, you might want to embed a bit more information into it, such as who is the author, the Pack name and so on. This is possible via the creation of a `packinfo.yml` file inside the pack's main directory.

```yaml
Name: The name of the pack
Version: 0.1.0
Author: The name of the author
Icon:
  Material: The bukkit name of the item you want to use
  Model: The CustomModelData of the material
URL: The link to your site, if any
Description:
- This is a list
- of things that will appear
- as the pack's description
- &aYou can also use color codes!&r
```

This will be visible when a user hovers over the pack icon by accessing the MythicMobs menu via the `/mm menu` command and going in any of the available section. If the Pack contains items relevant with the selected section, it will be displayed

## Dependencies and Overrides {#dependencies-and-overrides}

`packinfo.yml` can also block the whole pack, or only some of its files, on what else is installed:

```yaml
PackDependencies:
- MythicCrucible
PackOverrides:
- TheRealPack
FileDependencies:
- enchantments/* MythicEnchants
- cosmetics/chat.yml MythicCosmetics
FileOverrides:
- items/armors_vanilla.yml MythicArmors
```

| Key | Effect |
| --- | --- |
| `PackDependencies` | The pack is skipped unless every listed condition is true |
| `PackOverrides` | The pack is skipped if any listed condition is true |
| `FileDependencies` | `<glob> <condition>`: matching files are skipped unless the condition is true |
| `FileOverrides` | `<glob> <condition>`: matching files are skipped if the condition is true |

A condition is the name of a plugin, the folder name of another pack, or `MythicMobsPremium`. Conditions can be combined with `&&`, `||`, `!` and parentheses:

```yaml
PackDependencies:
- ((MythicCrucible && MythicMobsPremium) || Nexo)
FileOverrides:
- armors/** (MythicArmors || TheRealArmors)
```

Globs are relative to the pack folder. `*` matches within one folder, `**` matches any depth, and a path containing spaces must be quoted. An invalid condition logs a warning and is ignored. A skipped pack is not seen by the `mythicpack` condition.

Use it for a lite pack that should turn itself off when the full pack is installed, or for items that should use MythicArmors when it is present and plain armor when it is not.

## Files Folder {#files-folder}

Configurations in this folder will be **parsed based on their name**, regardless of their *location*.  
More specifically, files here should have a name structured like so:

```yaml
filename.identifier.yml
```

And, based on their identifier, they will be parsed as different file types

| Identifier | Aliases | File Parsing Type |
| --- | --- | --- |
| `mob` |  | Mob File |
| `skill` |  | Skill File |
| `item` |  | Item File |
| `droptable` | `drop` | Droptable File |
| `randomspawn` | `rspawn`, `spawn` | RandomSpawn File |
| `spawner` |  | Spawner File |
| `menu` |  | Custom Menu File |
| `placeholder` |  | Custom Placeholder File |
| `stat` |  | Stat File |
| `loretemplate` | `lore-template` | Lore Template File |
| `font` |  | Font File |
| `worldgen` |  | Worldgen File |
| `equipmentset` | `equipment-set` | Equipment Set File |
| `tooltip` |  | Tooltip File |
| `augment` |  | Augment File |

Some files are also recognized only by their extension

```yaml
filename.extension
```

| Extension | File Parsing Type |
| --- | --- |
| `schem` | Schematic File |

```
📦ExamplePack
 ┣ 📂files
 ┃ ┣ 📂aRandomFolder
 ┃ ┃ ┣ 📂aNestedFolder
 ┃ ┃ ┃ ┗ 📜ThisIsADroptableFile.droptable.yml
 ┃ ┃ ┣ 📜ThisIsAMobFile.mob.yml
 ┃ ┃ ┗ 📜ThisIsAPlaceholderFile.placeholder.yml
 ┃ ┣ 📂anotherRandomFolder
 ┃ ┃ ┣ 📜ThisIsAMobFile.mob.yml
 ┃ ┃ ┣ 📜ThisIsASchematic.schem
 ┃ ┃ ┗ 📜ThisIsASkillFile.skill.yml
 ┃ ┗ 📜ThisIsAStatFile.stat.yml
 ┗ 📜packinfo.yml
```
