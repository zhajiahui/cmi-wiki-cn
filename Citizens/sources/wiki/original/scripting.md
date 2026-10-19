## NOTICE

This page refers to the legacy Javascript scripting which is no longer fully supported. The main scripting support available in modern Citizens is through [Denizen](https://denizenscript.com/).

## Scripting Support in Citizens2

Citizens2 includes support for various scripting languages including Lua, Javascript and Python.

Javascript support is built into Java; additional languages can be added in through installing things such as JRuby (<http://jruby.org/>), Jython (<http://www.jython.org/>), Kahlua (<https://github.com/krka/kahlua2>) and more.

The scripting API contains a few built in objects in the global namespace which aid in some tasks. Currently, the 'events' object allows registering event listeners for Bukkit events and a reference to the Citizens plugin object is available under 'plugin'.

## Behaviours

Let's see an example of how to use scripts. Scripts can be added to an NPC via the /npc script --add [scripts] command, where scripts is a list of files inside the plugins/Citizens/scripts folder to use. Scripts are differentiated by their extension -- make sure it is correct!

When the script file is loaded by Citizens, it will call the method 'onLoad(NPC)' - anything can be performed at this time, although the NPC will not necessarily be spawned. If the method 'run(NPC)' exists it will also be called every tick by Citizens.

```
   function leftClick(event) {
       event.getClicker().sendMessage("hello from Javascript scripting!");
   }
```

```
   function onLoad(npc) {
       events.on(Java.type('net.citizensnpcs.api.event.NPCLeftClickEvent').class, leftClick);
   }
```

## Scripting Gotchas and Tips

### Javascript (Nashorn)

- Nashorn is a much faster Javascript engine only included in Java 7 and above. It is recommended to run this over the older Rhino engine.
- Read <https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/api.html> for more information on Java-Javascript connection.

### Javascript (Rhino)

- Some code will expect the methods equals and hashcode to be implemented - a simple equals function should be used often.
- for.. in loops do not work with Java collections.
- Rhino cannot use abstract classes.
- You can implement Java interfaces by using new [interfacename](object), where object contains the methods implementing the interface.
- Use importPackage(Packages.name.space) or importClass(Packages.name.space.YourClass) to import other classes/packages. The Packages. prefix is not required if the class is in the java.util package.
