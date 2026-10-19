All Citizens 2.0 behavior is dictated by Traits.

Traits can be applied to the NPCs and will handle events and interaction in specific ways.

The cool thing is a NPC can have multiple traits assigned to it. Including multiple [Character](https://wiki.citizensnpcs.co/Characters "Characters") Traits.

An example is the [Wallet](https://wiki.citizensnpcs.co/index.php?title=Wallet&action=edit&redlink=1 "Wallet (page does not exist)") Trait. This trait allows the NPC to have and use economy money. This Trait is useless by itself but works when the NPC is also assigned the [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen") or [Trader](https://wiki.citizensnpcs.co/Trader "Trader") trait.

[Characters](https://wiki.citizensnpcs.co/Characters "Characters") are really just complicated Traits.

Assigning multiple [Characters](https://wiki.citizensnpcs.co/Characters "Characters") traits can lead to powerful results, but also potential conflicts.

NPCs with the [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen") trait should use the commands for that trait to turn on and off specific interactions that may cause conflict.

For example if you want to make a [Blacksmith](https://wiki.citizensnpcs.co/Blacksmith "Blacksmith") that wanders throughout the town using Denizen [Activities](https://wiki.citizensnpcs.co/index.php?title=Activities&action=edit&redlink=1 "Activities (page does not exist)") to dictate his movement, you would want to turn off [Click Triggers](https://wiki.citizensnpcs.co/index.php?title=Click_Triggers&action=edit&redlink=1 "Click Triggers (page does not exist)") in the [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen") Trait so that right-clicking the [Blacksmith](https://wiki.citizensnpcs.co/Blacksmith "Blacksmith") would perform the proper [Blacksmith](https://wiki.citizensnpcs.co/Blacksmith "Blacksmith") commands and not trigger any [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen") scripts.

Using the command

:   **/trait [traitname]**

Will toggle the trait on and off for the selected NPC.
