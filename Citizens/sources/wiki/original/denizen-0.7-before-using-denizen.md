For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

<s><div style="font-family:camingodos-web;">
<div style="float:right;margin-left:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
</div>
<div style="margin-right:2.0em; margin-top:35px; padding:10px; font-family:camingodos-web; font-size:110%;">
<p><span style="font-family:natalya-alternate-one; font-size:650%; margin-right:-7px; margin-left:-10px;">W</span>elcome to Denizen! Grand adventure awaits, but let's get the basics out of the way first. On this page you will find instructions for installing Denizen, description of what the various files are used for, and a brief overview of what this is all about.
</p>
</div>
<div class="mw-heading mw-heading3"><h3 id="Getting_Started">Getting Started</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">Denizen is in BETA! Expect a few bugs here and there! If you are having problems, <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Debug_Mode" title="Denizen/0.7/In Game Commands"><code>/denizen debug</code></a> is your friend! We're always willing to help out in <a class="external text" href="irc://irc.esper.net" rel="nofollow">#denizen-dev on EsperNET</a> as well. If you do come across any errors beyond bad command syntax, please  report them to the <a class="external text" href="http://www.github.com/aufdemrand/Denizen/issues" rel="nofollow">Github Issues page for Denizens</a>.
<p>Denizen is not a drag-and-go type of plugin. In fact, Denizen won't do anything unless you assign and define scripts to NPCs. It's highly customizable. With the new <a class="external text" href="http://scripts.citizensnpcs.com%7CScript" rel="nofollow">Repository</a> in development, we hope there will be a wide array of par-baked scripts that you can easily download and customize to your server, but perhaps the most exciting part of Denizen is the ability to write your own scripts. In order to write awesome scripts, you will probably need to read the entirety of this wiki page and think outside the box! Someone is always around IRC to help out and provide suggestions, but please don't ask about the basics unless you have consulted here first.
</p><p>Some Denizen commands and requirements <b>REQUIRE</b> you to have other plugins, such as <a class="external text" href="http://dev.bukkit.org/server-mods/vault/" rel="nofollow">Vault</a>, installed with a compatible Permissions System and and Economy System. If the commands deals with money or permissions, chances are you will need Vault in order to utilize it. We're also getting ready to release command/requirement packs for Heroes and mcMMO, so stay tuned!
</p><p>The easiest way to use Denizen for the first time is to download the <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Start-up_kit" title="Denizen/0.7/Start-up kit">Start-up Kit</a>. This includes the default config file, sample scripts, and sample assignments to get you started. It is still recommended that you read as much of the wiki as you can take in to properly utilize Denizen's power and flexibility.
</p>
</div>
<p><br/>
</p>
<div class="mw-heading mw-heading3"><h3 id="Down_and_dirty">Down and dirty</h3></div>
<div style="margin-right:2.0em; padding:10px; font-family:camingodos-web; font-size:110%;">
<p>By now, you probably just want to see how to add custom content, right? Here's a quick, down-and-dirty walk-through to get your first custom NPC up and going. First you should have the <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Start-up_kit" title="Denizen/0.7/Start-up kit">Start-up Kit</a>, or at least an existing assignments.yml and script.yml. These are the files that you will be adding to in this walkthrough. Remember: The files should be placed in your server folder so that it resembles the format mentioned in <a href="#File_Structure">File Structure</a>. Once everything is in place, start up your server.
</p><p><br/>
<b>1:</b> Make a NPC by using C2 commands to create a new NPC, and assign a trait. We will use Notch in this example. See also: <a href="https://wiki.citizensnpcs.co/Commands" title="Commands">/NPC Commands</a>. 
</p>
<pre>/npc create Notch --trait denizen</pre>
<p>Note: You could alternatively use <tt>/trait denizen</tt> if working with an existing NPC.
</p><p><br/>
<b>2:</b> Create a script for Notch. See also: <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Writing_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Writing Scripts (page does not exist)">Writing Denizen Scripts</a>. <br/>
Create a new file in <tt>plugins/Denizen/scripts/</tt> named <tt>Notch Cookies.yml</tt>. Next, copy the contents of the small script below. This script gives a small random greeting to Notch with an 'easter egg' surprise if you know the secret word.
</p>
<pre>'Notch Greeting':
  Type: Interact
  Requirements:
    Mode: None
  Steps:
    1:
      Click Trigger:
        Script:
        - RANDOM 3
        - CHAT 'I Like Cookies!'
        - CHAT 'MMmm.. cookies are my favorite!'
        - CHAT 'Cocoa and Wheat make me freak!'
      Chat Trigger:
        1:
          Trigger: 'I love /cookie/s!'
          Script: 
          - CHAT 'Me too!'
          - EMOTE 'gives &lt;PLAYER&gt; some cookies.'
          - GIVE COOKIE QTY:6
          - ZAP 2
    2:
      Click Trigger:
        Script:
        - CHAT 'How were the cookies?'
</pre>
<p><br/>
<b>3:</b> Assign notch some scripts. See also: <a class="new" href="https://wiki.citizensnpcs.co/index.php?title=Denizen/0.7/Assigning_Scripts&amp;action=edit&amp;redlink=1" title="Denizen/0.7/Assigning Scripts (page does not exist)">Assigning Denizen Scripts</a>. <br/>
Open your assignments.yml. If none exists, create it in your <tt>/plugins/Denizen</tt> folder. Insert the following into your YML file. If <tt>Denizens:</tt> is not at the top of this document, create it.
</p>
<pre>Denizens:
  # ...
    # ...
  Notch:
    Interact Scripts:
    - 10 Notch Greeting
    Texts:
      No Click Trigger: Stop poking me!
      Denizen Unavailable: Sorry! Busy eating cookies!
      No Chat Trigger: I only understand cookies.
</pre>
<p>This text gives Notch some simple messages for specified circumstances. It also assigns the Notch Cookies script that we just wrote in the section above.
</p><p><br/>
<b>4:</b> Reload Denizen. See also: <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Denizen_Reload" title="Denizen/0.7/In Game Commands">Denizen Reload</a>. <br/>
This will ensure that the information has taken. First, in the console or your minecraft client, type <tt>/denizen reload</tt>. This will reload assignments.yml, config.yml, saves.yml, re-concantenate scripts, and perform some cleaning up of objects and such. This is a good time to check the console for any errors. If found, head on over to <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Troubleshooting" title="Denizen/0.7/Troubleshooting">Troubleshooting</a>.
</p><p><br/>
<b>5:</b> Check Denizen NPC status. See also: <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands#Info-Click" title="Denizen/0.7/In Game Commands">Info-Click</a>. <br/>
Info-Click your Denizen NPC by crouching and right-clicking it. This will output a couple of pages of information showing Citizens2 NPC stats, current Interact scripts, Trigger status, Bookmarks, and more. In the case of our example, Notch should have a single entry under Interact Scripts for <tt>Notch Cookies</tt>.
</p><p><br/>
<b>6:</b> Click on Notch! Play out the script. It's that easy! Go up to Notch and chat 'cookie' for the super secret special surprise.
</p><p><br/>
<i>Note:</i> This seems like as good of time as any to mention that if any interact script you are using have a 'proximity', 'location', or 'damage trigger', these must be turned on, per NPC. They are off by default as to keep performance as high as possible. See <a href="https://wiki.citizensnpcs.co/Denizen/0.7/In_Game_Commands" title="Denizen/0.7/In Game Commands">In Game Commands</a> for more info.
</p><p>Ready to dive deeper? start with either <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Interact_Scripts" title="Denizen/0.7/Interact Scripts">Denizen/0.7/Interact_Scripts</a> or <a href="https://wiki.citizensnpcs.co/Denizen/0.7/Activity_Scripts" title="Denizen/0.7/Activity Scripts">Denizen/0.7/Activity_Scripts</a>
</p>
</div>
</div></s>
