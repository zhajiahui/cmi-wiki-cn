For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~Triggers are what allow NPCs to react to player actions such as chatting to the NPC, clicking the NPC, attacking the NPC, or just walking near the NPC.~~

<s><div class="mw-heading mw-heading1"><h1 id="How_To_Make_A_trigger">How To Make A trigger</h1></div></s>

~~First, you must enable the trigger:

You can enable them just by running the command [- Trigger](http://wiki.citizensnpcs.co/Denizen/Commands#trigger)~~

<s><pre>- trigger [name:chat/click/damage/proximity] (state:true/false) (cooldown:&lt;#.#&gt;) (radius:&lt;#&gt;)</pre></s>

~~This is usually done in the [assignment script - on assignment](http://wiki.citizensnpcs.co/Denizen/Types_of_Scripts#Assignment_Script), but it can be done anywhere else as well.

Then you must make an [Interact Script](http://wiki.citizensnpcs.co/Denizen/Types_of_Scripts#Interact_Scripts) and include the trigger to react however.

You can also use Assignment script actions "on click", "on enter proximity", and "on exit proximity".~~

<s><div class="mw-heading mw-heading1"><h1 id="Chat_Trigger">Chat Trigger</h1></div></s>

~~A Chat trigger is written like so:~~

<s><pre>            chat Trigger:
                '1':
                    Trigger: "/Hello/ there npc!"
                    Script:
                    - CHAT "Hello, &lt;player.name&gt;!"
                '2':
                    Trigger: "/Bye/ npc!"
                    Script:
                    - CHAT "Goodbye, &lt;player.name&gt;!"
                '3':
                    Trigger: /REGEX:.+/
                    Script:
                    - CHAT "I don't know what &lt;player.chat_history&gt; is!"</pre></s>

~~Any message that contains the /Message/ will activate that part of the trigger.

You can also include any [RegEx](http://en.wikipedia.org/wiki/Regular_expression) by prefixing it with REGEX:~~

<s><div class="mw-heading mw-heading1"><h1 id="Click_Trigger">Click Trigger</h1></div></s>

<s><pre>            click Trigger:
                Script:
                - CHAT "Hehe, that tickles!"</pre></s>

~~Click triggers happen when a player right-clicks an NPC.~~

<s><div class="mw-heading mw-heading1"><h1 id="Damage_Trigger">Damage Trigger</h1></div></s>

<s><pre>            Damage Trigger:
                Script:
                - CHAT "Ow! That hurt, &lt;player.name&gt;!"</pre></s>

~~Click triggers happen when a player right-clicks an NPC.~~

<s><div class="mw-heading mw-heading1"><h1 id="Proximity_Trigger">Proximity Trigger</h1></div></s>

<s><pre>            Proximity Trigger:
                entry:
                    Script:
                    - CHAT "Hello there, &lt;player.name&gt;!
                exit:
                    Script:
                    - CHAT "Goodbye, &lt;player.name&gt;!"
                move:
                    Script:
                    - CHAT "This is optional and will spam you =D"
</pre></s>

~~Proximity triggers fire when a player enters or leaves the radius defined by the - trigger command.~~
