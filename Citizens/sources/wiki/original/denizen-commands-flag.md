For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

## Introduction

Flags are variables that can be checked anywhere in a script and in other scripts by using flag replaceable tags or the flagged requirement.
A flag can be placed on the player, the NPC or globally. Flags placed on a player only apply to that player, and flags placed on an NPC only apply to that individual NPC based on its ID, so NPCs with the same name have different flags because they have different IDs. However, a global flag applies to the entire server and can easily be read from any script.

Once you set a flag, you can call it back at any time with one of the [replaceable tags](https://wiki.citizensnpcs.co/Denizen/Replaceable_Tags#Flags "Denizen/Replaceable Tags").

# The flag command

To begin, you need to actually set a flag. You can do this by using

|  |
| --- |
| - flag ({player}|npc|global) [name([#])](:action)[:value] (duration:#) |

If a flag's type (player, npc or global) is not specified, the flag is placed on the player by default, and if a value for the flag is not specified, the value is "true" by default.

...Too much for you? Let's slow it down.

### The Basics

To start using flags, you must first understand the basics. This means learning the 4 types of flags you can use: booleans, strings, integers/doubles, and lists.

#### Boolean

The first, most used, most basic flag you need (besides a default flag) is a boolean flag. A boolean is a variable that represents either true or false.

You can set a boolean flag to true by using

```
- flag "RandomFlag"
```

...That's it. That automatically sets the flag named RandomFlag attached to the player interacting with the script as 'true'.
You can set it to false by simply doing

```
- flag "RandomFlag:false"
```

This type of flag is helpful for 'if' statements. More information on that can be found [here](https://wiki.citizensnpcs.co/index.php?title=Denizen/Commands/If&action=edit&redlink=1 "Denizen/Commands/If (page does not exist)").

#### String

Let's move forward. Probably the second most important flag you'll need on your journey is the string flag. Strings are variables that represent words or phrases that you can change at any time.

For example,

```
- flag "RandomFlag:Blah something whatever"
```

would set the flag 'RandomFlag' on the player who's interacting with the script as 'Blah something whatever'.

Remember, you can also attach the flag to the NPC that the script is being run by, or the server itself by specifying 'npc' or 'global'. That will be covered in the advanced section.

#### Integer/Doubles

Onto the next step... Integers and doubles! If you know a little about math, you probably already know that integers are just a fancy way of saying 'whole numbers'. In that sense, doubles are simply just numbers with decimals. (Non-whole numbers.)

Flags can hold numbers such as these by using something along the lines of...

```
- flag "IntegerFlag:3"
- flag "DoubleFlag:5.2"
```

#### Lists

If you want to store a lot of objects in one place, a flag list is the way to go.

To do this, you can use the Flag command's add and remove functions, like so:

```
### To add to a Flag list...
- flag "FlagList:->:<player>"
### To remove from a Flag list...
- flag "FlagList:<-:<player>"
```

# Usage inside scripts

## Checking if a flag exists

With the new 0.9 Development release you can now check if a flag exists.

### With the If command

To do this with an If command, just check a flag against null like in the following example:

```
- if <player.flag[flag_to_check]> == null narrate 'flag is null!'
  else narrate "<player.flag[flag_to_check]>"
```

### With Requirements

**Note: Requirements have been deprecated in favor of the If command.**

To do this with Requirements, you can use any of the following:

```
### To check if the flag EXISTS (Whether or not it has no value doesn't matter.)
- flagged FlagName
### To check if the flag DOES NOT EXIST (The flag must not have had a value at any point in time.)
- -flagged FlagName
### To check if the flag is NULL (If the flag has no value or doesn't exist.)
- flagged FlagName:null
```

## Mathematical calculations

Number flags (Integer, Double, ...) can be used in calculations. You can either use the <m: > tag or add the operation directly behind the flag (examples in the different kinds of operations).

### Addition

To add a flag and a number together, just use `add[]`.
Example:

```
<player.flag[money].add[2]>
```

### Subtraction

To subtract the flag's value, just use `sub[]`.
Example:

```
<player.flag[money].sub[10]>
```

### Multiplication

To multiply the value of a flag, just use `mul[]`.
Example:

```
<player.flag[money].mul[1.25]>
```

### Multiplication

To divide a flag by something use `div[]`.
Example:

```
<player.flag[money].div[1.25]>
```

### Mod

Denizen allows you to mod two numbers as well! Just use `mod[]`.
Example:

```
<player.flag[money].mod[3]>
```
