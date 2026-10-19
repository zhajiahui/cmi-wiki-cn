Citizens has an extensive API for working with NPCs. Make sure you always are using an up-to-date build of the CitizensAPI to ensure that your plugin works with the latest release of Citizens.

Javadocs can be found at <https://jd.citizensnpcs.co>

**IF YOU HAVE TROUBLE USING THE API** please speak to us on GitHub at <https://github.com/CitizensDev/Citizens2/issues> OR on Discord at <https://discord.gg/Q6pZGSR>

<table cellpadding="0" cellspacing="3" style="border: 0; background-color: #ffffff" width="275">
<tbody><tr>
<td style="width: 275; vertical-align: top; border:1px solid #ccc; background-color: #ffffff">
<div style="background-color:#aaa; font-size:1px; height:8px; border-bottom:1px solid #ccc;"></div>
<div style="float:right; margin:8px; margin-top:5px"></div>
<div style="padding:0.5em 0.3em 0.3em 0.3em; margin:0; text-indent:0.1em; font-weight: bold; border-bottom:1px solid #aaaaaa;"><b> </b></div>
<div style="font-size:100%; padding:3px">
<table cellpadding="0" cellspacing="3" width="100%">
<tbody><tr>
<td align="left" valign="top" width="100%">
<p><b> </b>
</p>
<div class="padded" style="padding: 19px">
<p><b>Current Release Download:</b> <a class="external text" href="https://ci.citizensnpcs.co/" rel="nofollow">Jenkins</a>
</p><p><b>Developmental Builds:</b> <a class="external text" href="https://ci.citizensnpcs.co/job/CitizensAPI/" rel="nofollow">Jenkins</a>
</p><p><b>Documentation:</b> <a class="external text" href="https://jd.citizensnpcs.co/" rel="nofollow">JavaDocs</a>
</p><p><b>Source:</b> <a class="external text" href="https://github.com/CitizensDev/CitizensAPI" rel="nofollow">Github</a>
</p>
</div></td></tr></tbody></table>
</div>
</td></tr></tbody></table>

## Linking Properly In Java

Citizens is built using Maven. Your plugin that links to Citizens should be using Maven as well.

For Maven users: your `pom.xml` should include this repository:

```
    <repository>
        <id>citizens-repo</id>
        <url>https://maven.citizensnpcs.co/repo</url>
    </repository>
```

and this dependency (EXACTLY AS WRITTEN WITH SCOPE SET TO PROVIDED NOT COMPILE):

```
    <dependency>
        <groupId>net.citizensnpcs</groupId>
        <artifactId>citizens-main</artifactId>
        <version>2.0.35-SNAPSHOT</version>
        <type>jar</type>
        <scope>provided</scope>
        <exclusions>
            <exclusion>
                <groupId>*</groupId>
                <artifactId>*</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
```

And replace the version with the current version of Citizens (check [the repo if unsure](https://maven.citizensnpcs.co/#/repo/net/citizensnpcs/citizens-main)), for example `2.0.35-SNAPSHOT` (but with the version numbers changed to the relevant version).

### Common Mistakes

1. **Using "citizensapi" as the artifact** - this is missing many important traits and classes that the plugin contains. The **citizens-main** module includes the API and plugin classes.
2. **Using "citizens" as the artifact** - this no longer works
3. **Not updating the version** - latest version is almost always the best one to go with. Older versions lack new features and classes you might need.
4. **Not keeping literal `-SNAPSHOT`** - it looks like a fill in spot, but it's not. Use that word exactly like that.
5. **Forgetting the `provided` scope** - the scope is important! If it's unset or set incorrectly, your project will build but not work properly on server.
6. **Using maven shade** - many users seem to accidentally enable the maven Shade plugin without understanding what it does. If you have the shade plugin and you're not confident exactly why, you probably don't need it. If you are intentionally using shade, please make sure that you do not shade Citizens into your plugin (do not use `compile` scope).
7. **Leaving off the exclusions** - this is a new recommendation (Sept 2022), the **exclusions** option makes the maven build much faster by informing maven that you don't need to download a separate copy of any of Citizens' upstream artifacts.

### Gradle

Some users prefer gradle. We don't use gradle for Citizens, so our references and support for it may be incomplete.

In short: same config as with Maven, but reformatted to how the gradle file expects it.

You should link the same repo. Something like:

```
    maven {
        name = 'citizens-repo'
        url = 'https://maven.citizensnpcs.co/repo'
    }
```

And add a dependency like this (with the version updated of course):

```
dependencies {
    compileOnly('net.citizensnpcs:citizens-main:2.0.35-SNAPSHOT') {
        exclude group: '*', module: '*'
    }
}
```

## Hooking Into Citizens

Hooking into Citizens is as simple as adding the line

```
depend: [Citizens]
# or 
softdepend: [Citizens]
```

into your plugin.yml.

Next, wait for CitizensEnableEvent or CitizensLoadEvent before using Citizens via the CitizensAPI class. This gives you access to the global NPCRegistry for NPCs, as well as the TraitFactory which allows trait registration. If Citizens is not loaded or you didn't wait for CitizensEnableEvent, all CitizensAPI.* methods will return null.

## Creating an NPC

The simplest way to create an NPC is to use an NPCRegistry, which manages the storage and creation of NPCs. The default registry is given by CitizensAPI.getNPCRegistry(), and you can create new ones with different storage methods by calling other CitizensAPI methods. A Player NPC with name "fullwall" could then be created like this:

`NPC npc = CitizensAPI.getNPCRegistry().createNPC(EntityType.PLAYER, "fullwall");
npc.spawn(location);`

## Checking if an entity is a Citizens NPC

Citizens NPCs will have the "NPC" Entity metadata set to true. `boolean isCitizensNPC = entity.hasMetadata("NPC");` This method doesn't even require a dependency on Citizens, as it works entirely through Spigot!

## Making an NPC Move

Want to make an NPC pathfind to a location? `npc.getNavigator().setTarget(yourLocation);`

## Creating a Trait

Traits are persistent, attachable objects that are linked to an NPC and provide specific functionality. This can be anything from custom AI to a simple talking trait.

To register a trait, we use the **TraitFactory** class. This controls registration for your custom traits.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:500px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java">//This is your trait that will be applied to a npc using the /trait mytraitname command. Each NPC gets its own instance of this class.
//the Trait class has a reference to the attached NPC class through the protected field 'npc' or getNPC().
//The Trait class also implements Listener so you can add EventHandlers directly to your trait.
@TraitName("mytraitname")
public class MyTrait extends Trait {
	public MyTrait() {
		super("mytraitname");
		plugin = JavaPlugin.getPlugin(MyPlugin.class);
	}

	MyPlugin plugin = null;

	boolean SomeSetting = false;
        
        // see the 'Persistence API' section
        @Persist("mysettingname") boolean automaticallyPersistedSetting = false;

	// Here you should load up any values you have previously saved (optional). 
        // This does NOT get called when applying the trait for the first time, only loading onto an existing npc at server start.
        // This is called AFTER onAttach so you can load defaults in onAttach and they will be overridden here.
        // This is called BEFORE onSpawn, npc.getEntity() will return null.
	public void load(DataKey key) {
		SomeSetting = key.getBoolean("SomeSetting", false);
	}

	// Save settings for this NPC (optional). These values will be persisted to the Citizens saves file
	public void save(DataKey key) {
		key.setBoolean("SomeSetting",SomeSetting);
	}

        // An example event handler. All traits will be registered automatically as Spigot event Listeners
	@EventHandler
	public void click(net.citizensnpcs.api.event.NPCRightClickEvent event){
		//Handle a click on a NPC. The event has a getNPC() method. 
		//Be sure to check event.getNPC() == this.getNPC() so you only handle clicks on this NPC!
		
	}
      
        // Called every tick
        @Override
        public void run() {
        }

	//Run code when your trait is attached to a NPC. 
        //This is called BEFORE onSpawn, so npc.getEntity() will return null
        //This would be a good place to load configurable defaults for new NPCs.
	@Override
	public void onAttach() {
		plugin.getServer().getLogger().info(npc.getName() + "has been assigned MyTrait!");
	}

        // Run code when the NPC is despawned. This is called before the entity actually despawns so npc.getEntity() is still valid.
	@Override
	public void onDespawn() {
        }

	//Run code when the NPC is spawned. Note that npc.getEntity() will be null until this method is called.
        //This is called AFTER onAttach and AFTER Load when the server is started.
	@Override
	public void onSpawn() {

	}

        //run code when the NPC is removed. Use this to tear down any repeating tasks.
	@Override
	public void onRemove() {
        }

}

//This is your Spigot plugin class. Use it to hook your trait into Citizens and handle any commands.
public class MyPlugin extends org.bukkit.plugin.java.JavaPlugin {

        public void onEnable() {
        // check if Citizens is present and enabled.
        if (getServer().getPluginManager().getPlugin("Citizens") == null
                || !getServer().getPluginManager().getPlugin("Citizens").isEnabled()) {
            getLogger().log(Level.SEVERE, "Citizens 2.0 not found or not enabled");
        } else {
            // Register your trait with Citizens.
            net.citizensnpcs.api.CitizensAPI.getTraitFactory()
                    .registerTrait(net.citizensnpcs.api.trait.TraitInfo.create(MyTrait.class));
            Bukkit.getServer().getPluginManager().registerEvents(new Listener() {
                @EventHandler
                public void onCitizensEnable(CitizensEnableEvent ev) {
                    NPC npc = CitizensAPI.getNPCRegistry().createNPC(EntityType.PLAYER, "Dinnerbone");
                    npc.spawn(yourlocationhere);
                }
            }, this);
        }
    }
}

</pre>
</div></td></tr></tbody></table>

### Dos and Don'ts

**DO**

- Use Spigot Entity API with npc.getEntity()
- Create a separate event Listener class if you expect there to be many trait instances. This may help performance with frequently called events.
- Honor npc.isProtected() If this is true the NPC should be 'invulnerable' to normal damaging effects.
- Use CitizensAPI.getNPCRegistry().isNPC() to check if an entity is a NPC. Real players and player-type NPCs will both return true for instanceof Player.

**DON'T**

- Attempt to access npc.getEntity() from within traits until onSpawn() has been called or npc.isSpawned() returns true.
- Change anything in npc.getNavigator().getDefaultParams() unless you're sure you want a global change. Use the localParams() instead *after* setting a navigation target.
- Assume a NPC is a Player. Mob types have some important differences.

## Default Traits

Citizens comes by default with Traits for its built-in commands. You can see these Traits in the JavaDocs <https://jd.citizensnpcs.co/net/citizensnpcs/api/trait/trait/package-summary.html> and also in the Citizens2 GitHub <https://github.com/CitizensDev/Citizens2/tree/master/main/src/main/java/net/citizensnpcs/trait>.

For example, you might add a piece of armor to an NPC using

```
npc.getOrAddTrait(Equipment.class).set(EquipmentSlot.BOOTS, new ItemStack(Material.LEATHER_BOOTS, 1));
```

## NPC Events

Citizens implements its own Listeners and will call new NPC-specific versions of many common events. This saves Trait developers the trouble of finding their npcs from the normal event entities. The event object these events provide are just like their Spigot counterparts with the addition of the getNPC() method.

See the [[Javadocs](http://jd.citizensnpcs.co/)] for a full list.

## Using the AI API

The AI API of Citizens can be broken down into two parts - *GoalController* and *Navigator*.

A *Goal* is a repeatable, abstract unit of work that can be performed by an NPC. For example, moving to a different location or attacking an enemy until it dies. It can be registered with a GoalController with a priority (higher is more important). The highest priority goal which can be executed will be prioritised. NPC contains getDefaultGoalController() for this purpose.

The GoalSelector allows for the dynamic selection of sub-goals and the concurrent execution of many sub-goals, and can stop execution at any time.

To add a new Goa, plugins should use Behavior interface which is a [behavior tree](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)) approach. Available node types are listed in the [javadocs](https://jd.citizensnpcs.co/net/citizensnpcs/api/ai/tree/package-summary.html).

Here is some suggested code for a new leaf Behavior node.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:500px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java"> public class MyBehavior extends BehaviorGoalAdapter {
     private Object state; 
     public void reset() {
         state = null;
         // this method can be called at any time if another goal is selected
     }
     public BehaviorStatus run() {
         if(!npcIsCool()) {
             return BehaviorStatus.FAILURE;
         } else if (npcIsAwesome()) {
             return BehaviorStatus.SUCCESS; 
         } else if (npcNeedsCool()) {
             new AccumulateCoolBehavior().run(); // easily run other behavior inline
             return BehaviorStatus.RUNNING;
         }
     }
     public boolean shouldExecute() {
         if (npcIsCool()) { 
             return true;
         }
         return false;
     } 
 }
</pre>
</div></td></tr></tbody></table>

You can compose behaviors using code like the following example:

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:300px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java"> public void setupTree(NPC npc) {
     npc.getGoalController().addGoal(Sequence.createSequence(new MyBehavior(), new MyAccumulateBehavior(), new MyParallelBehavior()));

     // A more complicated example
     npc.getGoalController().addGoal(Sequence.createSequence(
              new IfElse(() -&gt; npc.isCool(), 
                  TimerDecorator.tickLimiter(new MyLongRunningBehavior(), 100), 
                  new MyElseBehavior()),
              new MyParallelBehavior()
     ));
 }
</pre>
</div></td></tr></tbody></table>

The second important class is *[Navigator](https://jd.citizensnpcs.co/net/citizensnpcs/api/ai/Navigator.html)*. This enables pathfinding to a destination location or entity over time. The target should be set once only, not every tick. You can listen to the following navigation events to control the pathfinding flow:

- NavigationBeginEvent
- NavigationCancelEvent
- NavigationCompleteEvent
- NavigationEvent
- NavigationReplaceEvent

You can also use the [NavigatorParameters](https://jd.citizensnpcs.co/net/citizensnpcs/api/ai/NavigatorParameters.html) class to customise various aspects of pathfinding. The Navigator has two sets of parameters; "default", which are persisted over the lifetime of the NPC, and "local", which is a copy of the default parameters created when a pathfinding target is set.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:300px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java"> public void setPathfindingTarget(NPC npc, Location location) {
     npc.getNavigator().getDefaultParameters().speedModifier(1.1); // 110% speed by default.
     npc.getNavigator().setTarget(location);
     npc.getNavigator().getLocalParameters().speedModifier(1.2); // 120% speed for this pathfinding target only
 }
</pre>
</div></td></tr></tbody></table>

## Using the Persistence API

Sometimes, traits can store a lot of simple variables such as primitives, Strings, Locations, and others. Saving/loading them via the trait API can be a little bit of overkill.

Citizens provides a simple Persistence API to automatically save and load these variables using DataKeys. The key to this API is the @Persist annotation. Sample code is provided below.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:100%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> Example</div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:100%; height:300px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java"> public class MyTrait extends Trait {
     // logic omitted.

    @Persist boolean myVariable = false; // the default value of @Persist saves the value under the field name (in this case, 'myVariable').
    
    @Persist("newkey") int intVariable = 11; // this saves the value under 'newkey'. The default value of the variable has been set to 11 - this will be used when loading if the key doesn't exist.

    @Persist(value="newkey", required=true) String required; // if the value under 'newkey' doesn't exist, then the trait will fail to load.
 }
</pre></div></td></tr></tbody></table>

More advanced use of the API can be found in the @DelegatePersistence annotation. This allows complex types such as Locations to be saved and loaded with finer grained control. These types can be given default delegates by calling PersistenceLoader#registerPersistDelegate(Persister) - Location has a built in Persister for convenience.

<table border="0" cellpadding="0" cellspacing="0" style="clear:both; width:98%; background-color: #c1ffc1; border: solid 1px #88B288;">
<tbody><tr>
<td style="margin: 0px;"><div style="padding: 10px; font-size: 120%;"><b>Code:</b> </div></td>
</tr>
<tr>
<td style="margin: 0px;">
<div style="padding: 10px; overflow:auto; width:98%; height:500px; background-color: #F8F8F8; border-top: 1px solid #88B288; font-size: 120%;"><pre lang="java"> public class MyTrait extends Trait {
     // logic omitted.

    @Persist 
    @DelegatePersistence(ExplicitComplexTypePersister.class) // explicit delegation
    ComplexType myComplexType;

    @Persist ComplexType implicitComplexType; // implicit delegation
    static {
        PersistenceLoader.registerPersistDelegate(ImplicitComplexTypePersister.class);
    }
 }
 
 public class ExplicitComplexTypePersister implements Persister {
     public Object create(DataKey root) {
         return new ComplexType(root.getInteger("complexstructures"));
     }
     public void save(Object instance, DataKey root) {
         ComplexType real = (ComplexType) instance; // guaranteed cast - will always succeed.
         root.setInteger("complexstructures", real.getComplexStructure());
     }
 }
</pre></div></td></tr></tbody></table>

## See Also

[Characters](https://wiki.citizensnpcs.co/Characters "Characters")

| Quick Navigation | |
| --- | --- |
| [Usage](https://wiki.citizensnpcs.co/Category:Usage "Category:Usage") | [Installation](https://wiki.citizensnpcs.co/Installation "Installation")  · [Frequently Asked Questions](https://wiki.citizensnpcs.co/Frequently_Asked_Questions "Frequently Asked Questions")  · [Commands](https://wiki.citizensnpcs.co/Commands "Commands")  · [Editors](https://wiki.citizensnpcs.co/Editors "Editors")  · [Characters](https://wiki.citizensnpcs.co/Characters "Characters")  · API  · |
| [Configuration](https://wiki.citizensnpcs.co/Category:Configuration "Category:Configuration") | [Configuration](https://wiki.citizensnpcs.co/Configuration "Configuration")  · [Text Syntax](https://wiki.citizensnpcs.co/Text_Syntax "Text Syntax")  · [Permissions](https://wiki.citizensnpcs.co/Permissions "Permissions")  · [Waypoints](https://wiki.citizensnpcs.co/Waypoints "Waypoints")  · [Data Storage](https://wiki.citizensnpcs.co/Data_Storage "Data Storage") |
