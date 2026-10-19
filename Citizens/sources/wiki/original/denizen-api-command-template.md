For more up-to-date information and full details on specific features (individual commands or tags, for example), check the [Meta Documentation](https://meta.denizenscript.com/).

If you want a full tutorial to help get you set up, check out the [Beginner's Guide](https://guide.denizenscript.com/) text website.

If you need quick help, visit our [Discord group](https://discord.gg/Q6pZGSR).

This wiki is outdated, please view the tutorial videos/guide, meta documentation, or Discord group (all linked above) for up-to-date information!

## Custom Commands

Denizen is extensible! In addition to Triggers and Requirements(soon!), an API is being provided to help you make custom Script Commands in your project! Have a neat idea for a command? Have a better way to STRIKE a player? (MEGASTRIKE command, anybody?)

Keep reading!

## YourCommand extends AbstractCommand

The first thing you need is a custom command class that extends the Denizen AbstractTrigger. This contains the method called when it's time for your command to be executed. This is called every-single-time a script contains your command.

#### Example Command

Sometimes the easiest way to work is to see an actual example. View a copy of the STRIKE command on Pastie.org for a very simple command. For examples, you can always check [Core Denizen Commands](https://github.com/aufdemrand/Denizen/tree/master/src/main/java/net/aufdemrand/denizen/commands/core).

#### Command Template

[View a command template copy on Pastie.org](http://pastie.org/4368657) for a copy/paste of the skeleton of a custom denizen commmand.

### The ScriptEntry object

When Denizen reads scripts, each line is turned into a SciptScript object that contains the command, the arguments, and various other data and objects, as described below. Your command is an extension of this AbstractCommand class, and each time your command is called in for execution, it's this class that is executed and handled a ScriptEntry. How your Command uses the ScriptEntry information is of course, up to you.

The Denizen ScriptEngine and Executer construct and fill a ScriptEntry with information that can be used in your command. Below is a list of methods you can use against the scriptEntry sent to your commands execute method.

|  |  |
| --- | --- |
| getCommand() | String value of the name of the command |
| Used by default in alerting the user when denizen is in debug mode, if the template is used. Also could be useful if your command module contains instructions for more than one command. You can register multiple commands to your module, as discussed later in this document. | |

|  |  |
| --- | --- |
| arguments() | String[] value of the arguments used in the script |
| This is the output of Denizen's argBuilder method. It splits the command arguments up with spaces and quotes. For instance: `arg1 arg2 'argument 3' "argument 4" would return a string array with a size of 4.` | |

|  |  |
| --- | --- |
| arguments() | String[] value of the arguments used in the script |
| This is the output of Denizen's argBuilder method. It splits the command arguments up with spaces and quotes. For instance: `arg1 arg2 'this is argument 3' "and that's argument 4" would return a string array with a size of 4. Note argument 4, which handles an argument using a single quote. Hint: Double quotes around the argument, and vice-versa.` | |

|  |  |
| --- | --- |
| sendingQueue() | QueueType of either QueueType.TRIGGER, QueueType.TASK, or QueueType.ACTIVITY |
| Denizen's Script Engine contains a method called runQeues which sends the ScriptEntries off to the executer. During this process, it stores which queue the command was called from. Can be used in advanced situations. Typically, if called by an Interact Script, this contains QueueType.TRIGGER. | |

|  |  |
| --- | --- |
| getScript() | String value of the script name |
| Could be useful if storing information about a Script. For example, Denizen's FINISH command takes this information for granted if no script is otherwise indicated in the arguments. | |

|  |  |
| --- | --- |
| getStep() | Integer value of the script's step |
| Could be used similarly to getScript(). The ZAP command uses this information to know which step to proceed to. | |

|  |  |
| --- | --- |
| getPlayer() | Player object of the script triggerer |
| Pretty straight forward. The bukkit Player object can get all kinds of information about the player. | |

|  |  |
| --- | --- |
| getDenizen() | DenizenNPC object of the script triggeree |
| DenizenNPC makes it easy to work with the Denizen that has been interacted with. Good example: LOOK command. | |

|  |  |
| --- | --- |
| getInitiatedTime() | Long value of System.currentTimeMillis() |
| Contains a `Long System.currentTimeMillis()` of the system time in which it was sent to your Command for processing which you can use to check against. | |

|  |  |
| --- | --- |
| setDelayedTime() | should be a Long value in the format of System.currentTimeMillis() |
| Advanced usage. See the DELAY command for an example. | |

|  |  |
| --- | --- |
| getDelayedTime() | Long value that was set with setDelayedTime() |
| Advanced usage. Again, see the DELAY command for an example. If not set with setDelayedTime(), this is null by default. | |

|  |  |
| --- | --- |
| getTexts() | String[2] of text sent by a Trigger |
| Vanilla Denizen will use this to store information sent to/from a Chat Trigger. Element [0] contains the text typed by the Player when the script was triggered, and element [1] contains the text as set in the Trigger: node of the script. | |

## Registering your command

In order for Denizen to use your command, it needs to be registered. This could probably be done in your plugin's onEnable() method.

#### Example code

You can also see a [formatted version on Pastie.org](http://pastie.org/4369286).

```
/*
 * Sets up my plugin on start of the craftbukkit server.	
 */

public MyCommand myCommand = new MyCommand();

@Override
public void onEnable() {
   getLogger().info("Enabling my plugin!");
   
   try {
       myCommand.registerAs("CUSTOM_COMMAND");
   } catch (ActivationException e) {
       plugin.getLogger().log(Level.SEVERE, "Oh no! Activation Exception!");
       e.printStackTrace();
   }
}
```
