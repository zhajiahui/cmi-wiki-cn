For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~You can add even further Denizen features by enabling various traits.~~

~~You can add traits by simply selecting the NPC and doing doing~~

<s><pre>/trait &lt;traitname&gt;</pre></s>

~~EG~~

<s><pre>/trait mobprox</pre></s>

~~And use the same command again to remove them~~

<s><div class="mw-heading mw-heading1"><h1 id="Mobprox_Trait">Mobprox Trait</h1></div></s>

~~Mobprox is short for "Mob Proximity". It enables a [proximity trigger](http://wiki.citizensnpcs.com/Denizen/Triggers#Proximity_Trigger)-like functionality, but for mobs instead of players.

When the trait is assigned, it is assumed the NPC has a Denizen script assigned.~~

<s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Actions">Mobprox Actions</h2></div></s>

~~The mobprox trait will fire the following actions on the Denizen script:~~

<s><pre>on mob enter proximity:
on mob exit proximity:
on mob move proximity:
on &lt;mobname&gt; enter proximity:
on &lt;mobname&gt; exit proximity:
on &lt;mobname&gt; move proximity:
</pre></s>

~~"mob" actions fire whenever **any** mob does the action.

<mobname> actions fire whenever **a specific mob** does the action.

<mobname> is the name of the mob, EG "zombie" or "creeper".

"enter" actions fire when a mob walks into range. It will fire again if the mob walks out and back in.

"exit" actions fire when a mob leaves range. It will fire again if the mob walks in and back out.

"move" actions fire whenever a mob has been in range and continues to be in range. It doesn't necessarily mean the mob actually moved.

Note that the actions don't run instantly, it can take up to 2 seconds before they are called. (Usually a bit faster)

Also note that sometimes several actions will be called all at almost the same time, if there are multiple entities in range.~~

<s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Tags">Mobprox Tags</h2></div></s>

~~In each action, you can use the [Replaceable Tag](http://wiki.citizensnpcs.com/Denizen/Replaceable_Tags) "<context.entity>" (With the <> included, quotes aren't needed) to refer to the mob in question.

You can check for matching details with an if command using the tag, like~~

<s><pre>- if &lt;context.entity.entity_type&gt; == "creeper" CommandHere
</pre></s>

~~or similar.

One tag that's very useful with the mobprox trait is <entity.can_see[<entity>]> - you can use this to check if the entity is visible to the NPC by doing:~~

<s><pre>- if &lt;npc.can_see[&lt;context.entity&gt;]&gt; CommandHere
</pre></s>

<s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Flags">Mobprox Flags</h2></div></s>

~~Additionally, you can modify the mobprox behavior using NPC flags:

MobProx Range:~~

<s><ul><li>Flag name is "mobprox_range"</li>
<li>Set to 10 by default</li>
<li>Can be any integer number, but it's recommended you don't exceed 100</li>
<li>Keep in mind, this is cubic range, not spherical range. Meaning, if the range is 10, and the mob is 9 blocks left and 9 blocks forward, it's still considered to be in range.</li></ul></s>

~~Whether to accept NPC mobs as mobprox triggers:~~

<s><ul><li>flag name is "mobprox_acceptnpcs"</li>
<li>Set to false by default</li>
<li>Can be true or false. True means NPC mobs or real mobs will fire the mobprox actions, false means only real non-NPC mobs will fire the mobprox actions.</li>
<li>Keep in mind, if you want NPCs to interact when they get near each other, there's better ways to do it than mobprox actions. Only set this true if you want NPC mobs treated exactly the same as real mobs.</li></ul></s>

~~MobProx action fire timing:~~

<s><ul><li>Flag name is "mobprox_timer"</li>
<li>Set to 4 by default</li>
<li>Can be any integer number, but between 1 and 10 is recommended.</li>
<li>Keep in mind, 1 means fire actions every half second, 2 means every second, 4 means every two seconds, and so on.</li></ul></s>

<s><div class="mw-heading mw-heading2"><h2 id="Mobprox_Example">Mobprox Example</h2></div></s>

~~For an example, create an NPC and assign the script below using "/npc assign --set mobproxexample" then enable the trait with "/trait mobprox"~~

<s><pre>'mobproxexample':
    type: assignment
    actions:
        on assignment:
        - flag npc mobprox_range:20
        - flag npc mobprox_acceptnpcs:false
        - trigger name:click state:true
        on mob enter proximity:
        - if &lt;context.entity.entity_type&gt; != "creeper" {
          - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Here's a mob! It's a &lt;context.entity.entity_type&gt;!"
          - if &lt;context.entity.can_see[&lt;npc&gt;]&gt; == false
            announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; I can't see it though &lt;&amp;co&gt;("
          }
        on mob exit proximity:
        - if &lt;context.entity.entity_type&gt; != "creeper"
          announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Goodbye, &lt;context.entity.entity_type&gt;!"
        on creeper enter proximity:
        - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Aahh! Creeper! Die creeper!"
        on creeper exit proximity:
        - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; Oh good, the creeper's gone!"
        on creeper move proximity:
        # Note: don't use player-type npc. or player. can_see, always use context.entity.can_see
        # Due to a bug in Bukkit
        - if &lt;context.entity.can_see[&lt;npc&gt;]&gt; == true {
          - announce "&lt;&amp;7&gt;[&lt;npc.name&gt;]&lt;&amp;2&gt; I cast lightning on you, creeper!"
          - strike &lt;context.entity.location&gt;
          }
    interact scripts:
    - 10 mobproxexample_interact

mobproxexample_interact:
    type: interact
    steps:
        1:
            click trigger:
                script:
                - chat target:&lt;player&gt; "Hello, I'm a mob researcher! I'm looking for interesting mobs to classify!"
                - chat target:&lt;player&gt; "But I'm deathly afraid of creepers! Luckily a wizard taught me a spell to cast lightning!"</pre></s>
