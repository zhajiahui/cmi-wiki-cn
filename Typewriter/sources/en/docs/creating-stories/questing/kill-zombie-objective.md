# Kill Zombie Objective

**Before starting**

It's best to first read [Questing](https://docs.typewritermc.com/docs/creating-stories/questing) before starting this tutorial.

**NPC**

This tutorial requires you to already have created an NPC using the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension) guide.

In this tutorial, you will learn how to create a quest where:

- The player interacts with an NPC
- The NPC gives the player a quest with the objective to kill 2 zombies.
- The player completes the objective by killing 2 zombies.
- The player returns to the NPC to complete the quest.

## Quest Flow {#quest-flow}

| State | Facts | Description | Transitions |
| --- | --- | --- | --- |
| Not Started | `Zombie Quest Fact = 0` | Player hasn't started the quest yet | Talk to NPC → Quest Received |
| Quest Received | `Zombie Quest Fact = 1` `Kill Zombie Fact = 0` | Player has received the quest from the NPC | Kill Zombies → Killing Zombies |
| Killing Zombies | `Zombie Quest Fact = 1` `Kill Zombie Fact >= 2` | Player is killing zombies | Return to NPC → Completed |
| Completed | `Zombie Quest Fact = 2` | Player has completed the quest by killing 2 zombies | Reset Quest → Not Started |

## Quest Setup {#quest-setup}

This guide is split up into 2 sections.

- [**Manifest Section**](https://docs.typewritermc.com/docs/creating-stories/questing/kill-zombie-objective#manifest-section): Covers how to set the quest up and add the objective.
- [**Sequence Section**](https://docs.typewritermc.com/docs/creating-stories/questing/kill-zombie-objective#sequence-section): Explains how to make the npc give the quest and how to make the objective completable.

## Manifest Section {#manifest-section}

**Before Starting**

Make sure you have the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension) guide completed before starting this tutorial.

> In this guide we will be using the Oliver NPC as the quest giver.

Also make sure you have created a manifest page.

> In this section, we will be setting up the quest and adding the objective to the manifest.

### Creating the Quest {#creating-the-quest}

Now inside the manifest page, click on the **+** button in the top right corner and search for `Quest`. Click on the **+** button to add it to your page.

Add Quest

A quest definition

+

#### Configuring the Quest Entry {#configuring-the-quest-entry}

Now inside the quest entry set the following fields:

- **Display Name**: `ZombieQuest`
- **Active Criteria**: `Zombie Quest Fact >= 1`
- **Completed Criteria**: `Zombie Quest Fact = 2`  
  *For this guide I used a permanent fact*

### Adding the Objective {#adding-the-objective}

Now inside the quest entry, click on the **+** button in the top right corner and search for `Completable Objective`. Click on the **+** button to add it to your page.

Add Completable Objective

An objective that can show a completed stage

+

### Configuring the Objective Entry {#configuring-the-objective-entry}

Now inside the objective entry set the following fields:

- **Quest**: `ZombieQuest`
- **Show Criteria**: `Zombie Quest Fact = 1`
- **Completed Criteria**: `Zombie Quest Fact = 1` + `Killed Zombies Fact >= 2`
- **Display**: `Kill 2 Zombies`

**Optional**

Inside the display you can also choose the display the progress using [PlaceHolderAPI](https://docs.typewritermc.com/docs/helpful-features/placeholderapi)

*Example:* `Kill 2 zombies (%typewriter_nOfQzADcAmcR6ao%/2)`

> We will be using this in the final result!

**Optional #2**

You can also add a second objective that requires the player to return to the NPC.

- **Show Criteria**: `Zombie Quest Fact = 1` + `Kill Zombie Fact >= 2`
- **Completed Criteria**: `Zombie Quest Fact = 2`
- **Display**: `Return to Oliver`

See [talk objective](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective) for more information on how to do this.

### Manifest Result {#manifest-result}

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/manifest.json)

[static.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/static.json)

## Sequence Section {#sequence-section}

**Before Starting**

It is recommended to have a good understanding of [Interactions](https://docs.typewritermc.com/docs/creating-stories/interactions) and [Facts](https://docs.typewritermc.com/docs/creating-stories/facts) before starting this section.

> In this section, we will be creating the sequence that gives the player the quest and makes the objective completable.

### Interaction with Oliver {#interaction-with-oliver}

Now we need to create the interaction with Oliver. This is where the player will receive the quest.
Click on the **+** button in the top right corner and search for `Add Entity Interact Event`. Click on the **+** button to add it to your page.

Add Entity Interact Event

When the player clicks on an entity

+

Inside the entry set the Definition field to `Oliver` (or what you named your npc).

### Adding dialogue to Oliver {#adding-dialogue-to-oliver}

Now when you click on Oliver nothing happens. It would be nice to add some dialogue to the npc.

> The following steps are optional, but recommended to make the quest more immersive.

1. Add a `New Option` to your sequence and set the following fields:
   - **Text**: `Could you help me with something?`
   - **Option 1**: `Yeah sure, whats up?`
   - **Option 2**: `No sorry.`
2. Now in the option 1 add a trigger for a spoken with fields:
   - **Text**: `Go kill 2 zombies.`
   - **Duration**: `1s`
3. Inside that spoken add a modifier: `Zombie Quest Fact = 1`

### On kill increase fact {#on-kill-increase-fact}

Now we need to increase the fact when the player kills a zombie. To do this we need to add a `On Player Kill Entity` event to the sequence.

Add On Player Kill Entity

When a player kills an entity

+

Inside the entry enable the Enity Type and set the Entity Type to `Zombie`.

### Increasing the fact {#increasing-the-fact}

Now we need to increase the fact when the player kills a zombie. To do this right click on the `On Player Kill Entity` and select `Link with ...` select the `Triggers | 1` and search for `Add Simple Action`.

Add Simple Action

Simple action to modify facts

+

Inside the entry set the following fields:

- **Criteria**: `Zombie Quest Fact = 1`
- **modifier**: `Zombies Killed Fact + 1`

This will increase the fact by 1 every time the player kills a zombie and only do this if the player has the quest.

### Sequence Result {#sequence-result}

[sequence.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/sequence.json)

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/manifest.json)

[static.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/static.json)

## Final Result {#final-result}

Now when you click on Oliver you will get the dialogue and when you click on the first option you will get the quest. When you kill 2 zombies the objective will be completed.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/kill-zombie-objective/kill-zombie-objective-result.webm"></video>
