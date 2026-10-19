For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>WANDER
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">(RADIUS:#) (DELAY:#) (SPEED:#) (FILTER:#:#,#:#..) (BOOKMARK:BookmarkName)
</th></tr>
<tr>
<td colspan="3">Causes the Denizen to wander aimlessly. Many options to dictate range and area.
<p>Modifiers:
</p>
<ul><li>RADIUS: Radius within which to wander.</li>
<li>DELAY: The time, in seconds, between movements.</li>
<li>SPEED: The walking speed while wandering.</li>
<li>FILTER: The block ids or names the Denizen is allowed to wander to</li>
<li>BOOKMARK: A location bookmark around which to wander</li></ul>
<p><b>Example Usages</b>
</p>
<pre>   - 1 WANDER DELAY:12 RADIUS:10 SPEED:.75 FILTER:COBBLESTONE,GRAVEL,5
</pre>
</td></tr></tbody></table>

<table align="left" class="wikitable collapsible collapsed" style="background:aliceblue;font-family:museo-sans;" width="100%">
<tbody><tr>
<th align="left" scope="col" width="0">
</th>
<th align="left" scope="col">
<p>TASK 
</p>
</th>
<th align="left" scope="col" style="font-family:courier new;" width="90%">[SCRIPT:ScriptNAme] (REPEATS:#) (DELAY:#) (DURATION:#)
</th></tr>
<tr>
<td colspan="3">Runs a <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Task_Scripts" title="Denizen/0.7/Task Scripts">Task Script</a> repeatedly.
<p>Modifiers:
</p>
<ul><li>SCRIPT: The Task script to run. Note that there will be no "player" associated with this script so some commands will not work.</li>
<li>REPEATS: The number of times to repeat the TASK. By default the scripts runs repeatedly until a new activity is assigned.</li>
<li>DELAY: The number of seconds to wait between repeats.</li>
<li>DURATION: The number of seconds to pause other activities while the task runs.</li></ul>
<p><b>Example Usages</b>
</p>
<pre>  - 1 TASK SCRIPT:WalkHome REPEATS:0
  - 1 TASK SCRIPT:ComplainAboutThings DELAY:10 DURATION:1

</pre>
</td></tr></tbody></table>
