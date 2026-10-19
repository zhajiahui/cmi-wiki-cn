For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~==Triggers==~~

<s><ul><li>0.7 introduces several new core triggers: Damage, Proximity, and Location</li>
<li>Not all triggers are turned on by default for performance reasons. see <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands" title="Denizen/0.7/In Game Commands">Denizen/0.7/In_Game_Commands</a> for more info.</li></ul></s>

<s><div class="mw-heading mw-heading2"><h2 id="Commands">Commands</h2></div></s>

~~All text-type commands (CHAT, NARRATE, etc) must have the text in quotes. Single or double is fine.~~

<s><pre> Example: - CHAT "Use double quotes if your text has an apostrophe, y'all." </pre></s>

~~EXECUTE must also have the command and arguments in single- or double- quotes~~

<s><pre> Example: - EXECUTE ASSERVER "warp someplace" </pre></s>

~~GIVE and TAKE must specify the quantity with QTY:# or qty:#~~

<s><pre> Example: - GIVE DIAMOND QTY:10</pre></s>

~~RESPAWN no longer exists. Use TELEPORT instead with the DENIZEN argument, this will spawn the Denizen at the specified location.~~

<s><pre> Example: - TELEPORT DENIZEN 'BOOKMARK:name' </pre></s>

~~PLAYERTASK no longer exists. Use a Location Trigger

PRESS no longer exists. Use SWITCH for buttons and levers.

Any command that takes a bookmark must specify BOOKMARK:. Also any command that takes a bookmark can use bookmarks from other Denizens by specifying 'BOOKMARK:Denizen Name:BookmarkName'~~~~:   If the Denizen name has a space in it the quotes are **required**~~

<s><pre> Example: - TELEPORT DENIZEN 'BOOKMARK:bob jones:bobshouse' </pre></s>
