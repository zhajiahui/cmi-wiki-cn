For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://one.denizenscript.com/denizen/cmds/).

If you want a full tutorial to help get you set up, check out the [Tutorial Videos](https://one.denizenscript.com/denizen/cmds/denizen/vids) on youtube or the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

~~In Denizen, there are multiple different types of scripts each made to fill a different purpose. When writing a script, you will need to use several of these, so they're important to know!~~

~~(Note: Page under construction! There's a lot more than just what's listed here!)~~

~~Types: interact, book, item, entity, task, assignment, procedure, world, format, inventory~~

~~Also: All the example scripts on this page work together...~~

~~To see them all work, add them all to your server and assign "MyAssignmentScript" to an NPC, then right-click it.~~

<s><div class="mw-heading mw-heading1"><h1 id="Assignment_Script">Assignment Script</h1></div></s>

<s><pre>MyAssignmentScript:
    type: assignment
    actions:
        on assignment:
        - chat "I has been assigned!"
        - trigger name:proximity state:true</pre></s>

~~The assignment script is the first script any NPC needs - it lists everything the NPC does!

One of the most important uses is the "on assignment:" action, which is run when the script is assigned to an NPC, in which you normally enable triggers, and run other important commands.

You can link interact scripts by adding:~~

<s><pre>    Interact Scripts:
    - 10 MyInteractScript
</pre></s>

<s><div class="mw-heading mw-heading1"><h1 id="Interact_Scripts">Interact Scripts</h1></div></s>

<s><pre>MyInteractScript:
    type: Interact
    Steps:
        '1':
            Proximity trigger:
                Entry:
                    Script:
                    - chat "Hi there, &lt;player.name&gt;!"
                    - run mytask
</pre></s>

~~Interact scripts control what the NPC does when a player fires triggers such as proximity, click, chat, or damage.~~

<s><div class="mw-heading mw-heading1"><h1 id="Item_Scripts">Item Scripts</h1></div></s>

<s><pre>myitem:
    type: item
    material: wool:3
    recipe:
    - air|air|air
    - dirt|wool|dirt
    - air|air|air
</pre></s>

~~Item scripts hold data on custom items.~~

<s><div class="mw-heading mw-heading1"><h1 id="World_Scripts">World Scripts</h1></div></s>

<s><pre>formatybit:
  type: world
  events:
    on formattybit command:
    - narrate format:formatdemo "Hello, I'm a well-formatted narrate, caused by a world event '/formattybit' command!"
    - determine fulfilled
</pre></s>

~~World scripts run world events.~~

<s><div class="mw-heading mw-heading1"><h1 id="Task_Scripts">Task Scripts</h1></div></s>

<s><pre>mytask:
    type: task
    script:
    - chat "Here, a book for you!"
    - give myfancybook
</pre></s>

~~Task scripts contain random scripts to be run by other scripts using the command - run (taskscriptname)~~

<s><div class="mw-heading mw-heading1"><h1 id="Book_Scripts">Book Scripts</h1></div></s>

<s><pre>myfancybook:
    type: book
    title: My Fancy Book
    author: NotNotch
    text:
    - This is my book. There are many like it, but this one is mine!
    - Many &lt;n&gt;new &lt;n&gt; lines!
    - &lt;p&gt;Paragraphs, &lt;p&gt;too!
</pre></s>

~~Book scripts hold information on a complex book item.

Each - line in the text: category is a new page.

After defining a book in a script, you can give it to a player in any runnable script using - give (bookname)~~

<s><div class="mw-heading mw-heading1"><h1 id="Format_Scripts">Format Scripts</h1></div></s>

<s><pre>formatdemo:
  type: format
  format: "&lt;&amp;f&gt;[&lt;&amp;b&gt;Message&lt;&amp;f&gt;- &lt;&amp;2&gt;&lt;text&gt;&lt;&amp;f&gt;]"
</pre></s>

<s><div class="mw-heading mw-heading1"><h1 id="CommandScripts">CommandScripts</h1></div></s>

<s><pre>my custom command:
  type: command
  name: formatbit
  script:
  - narrate format:formatdemo "Hello, I'm a well-formatted narrate, caused by a command script '/formatbit' command!"
</pre></s>

~~World scripts run world events.~~
