In this tutorial, you will learn the basics of the dialog system syntax, and the concepts involved.

## Overview

First, let's look at the basic flow of a dialog program. The world of Minecraft can be broken up into a series of *events*. These are things like talking, combat, block breaks, and so on. The general flow looks kind of like this: event -> listener. This isn't easy to represent in text. How do we make a nice system out of this?

The answer is pretty simple: think of an event as a series of facts, such as a player who was involved, their name, and so on. Each fact has a name or *key*, and a value eg. the player's name might have a key of "name" and a value of "fullwall". An event is simply a whole lot of facts about what happened. This makes it much easier to reason about in text.

This approach also makes it easy to associate more facts with an event; this group of facts is known as a *query*. A query can also have information about the world state, any memory that the NPC has picked up, and more.

Now we have a nice collection of facts - what do we do with them all? Time to introduce two new concepts: *rules* and *responses*. The final flow looks like this: event -> NPC -> generate facts -> dialog system -> rules.

## Rules

A rule takes in a query and checks it against a list of criteria. If it matches, it does something. For example in a chat event, it may check if the player's name is "fullwall", and then say "Hello, fullwall!" to the player. Rules are simple, yet can be combined to create complex interactions.

## Responses

A response is basically a list of commands; it has no criteria, but can be called from many different kinds of rules.

## Writing a Rule

Let's get onto the syntax. Before continuing, make sure you have Adventures downloaded and installed. Any NPC using the dialog system will need to have the dialog trait, so use /trait dialog before trying out any of these examples.

Here's an example rule; it doesn't too much at all.

```
rule example {
    criteria events=any;
}
```

This is the absolute minimum required to write a rule. We have the keyword 'rule' followed by the rule name, and the { character. { and } characters mark the start and end for Adventures.
Next, we have a 'criteria' declaration. This tells Adventures what events the rule is listening for and what criteria it checks.

```
criteria events="any";
                ^ matches any kind of event, as a demonstration
```

Notice the semicolon (';') after the criteria statement - every line within a rule should end with one of these.
You can also have multiple events, separated by commas:

```
criteria events=onchat, ondamage;
```

Before we move onto more advanced examples of criteria, let's review the different types of values in dialogs. Notice that "any" was in quotes - this means that the value should be treated as a block of text.

```
100 - a number
"100" - text containing the characters 100
"text" - text
true/false - yes or no value
$sender.location.x - value is taken from the query fact "sender.location.x"
"${sender.name}" - value is text containing the fact under sender.name
```

Now, criteria that just match the events are pretty pointless. You can also check facts from the query. Let's say that we only want to match the rule when the NPC is standing at x=100.

```
criteria events="any" $npc.location.x=100;
```

What about when y is below 50?

```
criteria events="any" $npc.location.x=100, $npc.location.y<50;
```

What about matching a chat rule that starts with h? (note: this uses regex)

```
criteria events="onchat" $message~=/h[a-zA-Z]+/
```

## Writing a Response

Note that many of the statements used in this section can be used in a rule, but it may be helpful to separate the logic out into a response.

A response is written much like a rule without a criteria statement.

```
response example {
}
```

Let's call this response in a rule.

```
rule example {
    criteria events="any";
    response example;
}
```

## Writing a full Dialog

Let's look at a classic 'Hello' example. When a player says 'Hi!' we want to reply 'Hello, (name)!'.

Copy and paste the text below into a new file, 'Hello.txt' inside the plugins/Adventures/dialog folder.

```
rule saidHi {
    criteria events=onchat $message="Hi!";
    response sayHi;
}
response sayHi {
    say message:"Hello, ${sender.name}!", target:$sender;
}
```
