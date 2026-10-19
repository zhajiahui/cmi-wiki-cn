For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

By default, Denizen comes as a clean install. One easy way to get up and going is to install the start-up-kit as explained here. You may want to first check out the step-by-step the [Getting Started: Down and Dirty](https://wiki.citizensnpcs.co/Denizen/0.7/Before_Using_Denizen#Down_and_dirty "Denizen/0.7/Before Using Denizen") section, which walks through installing a sample script and assignment. This start-up kit attempts to go into a little bit more detail with some pre-loaded content.

### Download the Kit

The start-up contains everything you need to get going with Denizen quickly. Inside the zip file you will find a folder called 'Denizen'. Extract this folder to your /plugins/ directory. Make sure you have the latest Denizen jar installed, then start your server or call

```
/denizen reload
```

The kit contains:

- A pre-configured [config.yml](https://wiki.citizensnpcs.co/Denizen/0.7/config.yml "Denizen/0.7/config.yml")
- A pre-configured assignments.yml for 2 NPCs (Steve and Jill)
- A file with 2 Interact Scripts (Steve Scripts.yml)
- A file with 2 Activity Scripts (Activity Scripts.yml)

## Download

**[Download Here](https://github.com/downloads/jrbudda/Denizen/Start-up%20Kit%200.74.zip)**

## How to use

The kit defines assignments for 2 NPCs. One named 'Steve' and one named 'Jill'.
To make an NPC use the /npc create command.

```
/npc create Steve --trait denizen
```

Steve is now ready to go. Likewise to make Jill:

```
 /npc create Jill --trait denizen
```

The assignments are done by Name so these Denizens are now fully functional. To test, call /denizen info. You should see the assigned scripts and activities as defined in the assignments.yml.

To begin learning, open the scripts or assignments file in a good text editor like notepad++ see [YAML](https://wiki.citizensnpcs.co/YAML "YAML")
The files are commented to help you get started.
