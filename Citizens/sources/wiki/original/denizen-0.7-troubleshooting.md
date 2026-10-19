For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="font-family:camingodos-web; font-size:100%;">
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">D</span>enizen can seem a bit complicated at first, especially when you don't know what to look for when something isn't working exactly like you want. Luckily, if you are having problems, there are several tools available to help you.
</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Assignments_not_working?"><span id="Assignments_not_working.3F"></span>Assignments not working?</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>To check assignments on a Denizen use <tt>/denizen info</tt> with the NPC selected to make sure assignments have taken. This also shows other great information, such as bookmarks and activities. If you are the NPC's owner you can also sneak and right click to view this info. See: <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Info-Click" title="Denizen/0.7/In Game Commands">Info-Click</a>
</p><p>If assignments are not showing up, ensure that your <tt>assignments.yml</tt> is properly formatted, you've saved your assignments.yml, and you've used <tt>/denizen reload</tt>. Also check spelling of the Denizen NPCs name. This is case-sensitive! See: <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Denizen_Reload" title="Denizen/0.7/In Game Commands">Reload Command</a>
</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Trigger_not_working?"><span id="Trigger_not_working.3F"></span>Trigger not working?</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">Denizen NPCs, by default, have only their Click Trigger and Chat Triggers enabled. Use <tt>/denizen trigger list</tt> to see the status of the triggers for your NPC. Red means disabled. See:  <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Trigger_Toggles" title="Denizen/0.7/In Game Commands">Trigger Command</a>
<p><br/>
You may also have a plugin conflict. If you suspect this, try disabling all plugins except Permissions, Citizens2, and Denizen to see if the problem persists.
</p>
</div>
<div class="mw-heading mw-heading3"><h3 id="Script_not_working_as_intended?"><span id="Script_not_working_as_intended.3F"></span>Script not working as intended?</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">Turn on <tt>/denizen debug</tt> and check the information being sent to the console when your script runs. There's likely some information in there that can be used to track down the problem, whether it be failed requirements, incorrect flow logic, syntax, or simply a spelling mistake. See:  <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/In_Game_Commands&amp;action=edit&amp;redlink=1" title="Denizen/In Game Commands (page does not exist)">Debug Mode Command</a>
</div>
<div class="mw-heading mw-heading3"><h3 id="Still_having_problems,_what_now?"><span id="Still_having_problems.2C_what_now.3F"></span>Still having problems, what now?</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">If you are still having problems check your console messages for errors, especially at start up. Any kind of error, from any plugin, may lead to problems. Take this opportunity again to triple-check spacing in your script. If all else fails join us on <a class="external text" href="http://webchat.esper.net/?channels=denizen-dev" rel="nofollow">EsperNet in #denizen-dev</a>.
</div>
</div></s>
