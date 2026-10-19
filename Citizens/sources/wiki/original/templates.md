Templates are a simple way to share NPC configuration across NPCs and servers.

## Layout

Templates are stored in the plugins/Citizens/templates folder.

Each template consists of a **namespace** or a folder to group related templates together and a bunch of template files.

## Example

Let's build a quick example.

Make a folder called plugins/Citizens/templates/awesometemplates.

Inside this, create a .yml file. This can have any file name - the file name is just for helping you organise complicated templates. Let's call the first one info.yml.

Inside info.yml, put the following template:

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:200px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="yaml">towninfo:
    yaml_replace:
        replacements:
            name: Town Crier
            traits:
                type: VILLAGER
        override: true
    commands:
        on_spawn:
            - say --range 5 Hello!
</pre>
</div></td></tr></tbody></table>

This creates a template with the namespace *awesometemplates* and the template name *towninfo*. We can reference this in game with the combined key *awesometemplates:towninfo* or by just the template name *towninfo*. If there could be duplicate template names in different namespaces, then use the full reference.

Now, we can create an NPC with our desired template using

```
/npc create NPC --templates awesometemplates:towninfo
```

You should see a new villager NPC called Town Crier appear that broadcasts the message Hello! every time it spawns.

## Other commands

You can generate a copy of another NPC's save data directly using for example /template generate awesometemplates:towninfocopy. This will save it into a file called towninfocopy.yml.

You can apply a template to an existing NPC by using /template apply awesometemplates:towninfo.

## Reference

Command events

- on_spawn (when the NPC spawns)
- on_template_apply (when the template is applied)
