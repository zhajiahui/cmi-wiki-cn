For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

Samples will go here, maybe!

## Checkpoint NPC

~~View script with dScript highlighting: <http://mcmonkey.org/paste/91>~~

<s><pre># Simply spawn an NPC and do
# /npc assign --set respawnmaster
# and now you have a checkpoint NPC :D

# NPC Assignment script
respawnmaster:
    # Obligatory type
    type: assignment
    # Actions = script run when NPC-related events occur
    actions:
        # This one is when the NPC is assigned
        on assignment:
        # Enable the trigger 'Proximity' with a radius of 10 blocks
        - trigger name:proximity state:true radius:10
    # interact script list
    interact scripts:
    # The interact below
    - 10 respawnmaster_interact

# The interact script
respawnmaster_interact:
    # Obligatory type
    type: interact
    # List the steps below
    steps:
        # First (Default) step
        1:
            # Triggers that fire when a player moves around near an NPC
            proximity trigger:
                # Specifically, when a player enters the radius of 10 blocks mentioned above
                entry:
                    # Run this script...
                    script:
                    # If the player's last set checkpoint was set by this NPC,
                    # cancel the current script queue (Clear it) (Meaning, the the flag/narrate won't happen)
                    - if &lt;player.flag[respawner]&gt; == &lt;npc.id&gt; queue clear
                    # Add a flag on the player, named respawnpoint, set to the player's current location at the time he entered the radius
                    - flag player respawnpoint:&lt;player.location&gt;
                    # Add a flag on the player, named respawner, set to the ID of the NPC that set this checkpoint.
                    - flag player respawner:&lt;npc.id&gt;
                    # Tell the player that he has reached the checkpoint, in green
                    - narrate "&lt;&amp;2&gt;You reached a checkpoint!"

# World script to handle respawning
respawnhandler:
    # Obligatory type
    type: world
    # List of world events (events not related to an NPC) that we want to run scripts for
    events:
        # The event that fires when a player dies and respawns
        on player respawns:
        # If the player doesn't have a respawn point, clear the scriptqueue, same as above, preventing the determine
        - if &lt;player.flag[respawnpoint]&gt; == null queue clear
        # Run the task script 'respawnnomercy' with a delay of one second
        - run respawnnomercy delay:2s
        # Tell the event that we want to change the outcome to the player's flagged respawn point...
        # in this event, that changes where the player respawns
        # Thus, the player respawns at the checkpoint set in the prox trigger above
        - determine &lt;player.flag[respawnpoint]&gt;

# A task script to prevent errors on Multiverse/whatever servers
respawnnomercy:
    # Obligatory type
    type: task
    # Script below is the only script in a task
    script:
    # Teleport the player to the respawn point, in case the determine above didn't do it
    - teleport &lt;player&gt; &lt;player.flag[respawnpoint]&gt;

# Remember, when whatever quest is completed, to run this command:
# - flag player respawnpoint:!
# To remove the respawnpoint and allow them to respawn normally
</pre></s>
