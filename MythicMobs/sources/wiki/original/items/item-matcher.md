# Item Matcher

Some features inside of MythicMobs supports matching items or blocks via a specific syntax:

##  {#section}

Writing the internal name of a Mythic Item/[Mythic (Crucible) Custom Block](https://wiki.mythiccraft.io/mythiccrucible/Custom-Blocks) will match

- that specific Mythic Item
- that specific Mythic Custom Block

##  {#section-2}

Writing the [Spigot material type](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) will match

- items with that material type
- blocks with that material type

##  {#section-3}

Using `#` at the start of an entry will match against

- items with that [Item Tag](https://minecraft.wiki/w/Item_tag_(Java_Edition))
  - `#arrows`, `#axes` and so on
- blocks with that [Block Tag](https://minecraft.wiki/w/Block_tag_(Java_Edition))
  - `#air`, `#animals_spawnable_on` and so on

##  {#section-4}

Using `*` at any point in the entry will make it so any * present will match against any number of characters. For those familiar with Regex syntax, `*` is equal to `.*`

- `netherite_*` will match any item/block whose type stars with "netherite_"
- `*_log` will match any item/block whose type ends in "_log"
- `*a*` will match any item/block whose type has the letter "a" somewhere in it
- `*` will match anything

##  {#section-5}

For blocks only, it is possible to specify some specific [block states](https://minecraft.wiki/w/Block_states) to be matched by specifying them inside of a pair of square brackets `[]` after the entry

- redstone_torch[lit=true;facing=north]
