## Syntax

### Values

```
10, 1.02, 123 - number
"test" - text
"${message}" - text with query value inside
$message - query value
[10, 12, 12...] - list of values
{"key" : value, "key2" : value...} - dictionary
```

### Rule syntax

```
rule rulename {
   criteria events="any"...;
   // statements here
}
```

### Statement syntax

```
rule example {
    // criteria
    say "example", $sender; // arguments can be without names
    say message:"example", target:$sender; // or all named to prevent ambiguity
    say "example", target:$sender; // or only some named
}
```

### Random syntax

```
response example {
    random {
        say "Hi", "p:fullwall" : 0.5;
        say "Hi2", "p:fullwall" : 0.3;
    }
}
```

Each statement is checked for the given probability; if the check fails, it moves on to the next one. Once a successful check is reached, the statement is executed and no more are checked.

## Events

##### Standard variables available

- *Entity under some root name*

```
root.health : entity's current health
root.maxhealth : entity's max health
root.type : entity type
root.location.x : x 
root.location.y : y 
root.location.z : z 
root.location.pitch : pitch 
root.location.yaw : yaw 
root.location.world : world
```

- *Player under some root name*

```
root.name : name
```

##### onchat

```
message : the message involved in the event
sender : the sender
```

## Statements

- [] - required argument
- () - optional argument
- ... - repeated argument
- Arguments can be given without explicit keys, and will be parsed in order of required and then optional arguments.

##### Remember

```
remember [$fact:value (10ns|ms|s|m|h|d (expiration time)) (-p (persistent)), ($fact2:value ...)];
```

##### Forget

```
forget [memory:"factname" | ["factname1", "factname2"...]];
```

##### Say

```
say [message:"message"], [target:"p:playername"|"n:npcid"|"broadcast"|"log"|fact of type 'Player'];
```

##### Code

```
java|js|py|lua|rb|clj|scala [code:"code"]
```

Evaluates raw code based on input. Note: JS is built into Java, but all others require additional programs. Eg. rb requires installing JRuby, scala requires installing scala, etc.
Java evaluation is done within a run() method of an anonymous runnable class. Only org.bukkit imports can be unprefixed; message fullwall if you want more to be automatically imported.

##### Denizen Script

```
dtask [name:"script name"], [player:query player | "playername"], (denizen:query NPC or Denizen | "denizen ID" | denizen ID as number)
dtask [name:"script name"], [denizen:query NPC or Denizen | "denizen ID" | denizen ID as number], (player:query player | "playername")
```

Requires [Denizen](https://wiki.citizensnpcs.co/Denizen "Denizen") 0.8 to be installed.
