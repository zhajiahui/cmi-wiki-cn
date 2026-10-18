# Talk To NPC Objective

**Before starting**

It's best to first read [Questing](https://docs.typewritermc.com/docs/creating-stories/questing) before starting this tutorial.

**NPC**

This tutorial requires you to already have created an NPC using the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension) guide.

In this tutorial, you will learn how to create a quest where:

- The player interacts with an NPC
- The NPC gives the player a quest
- The player completes the quest by talking to a different NPC.

## Quest Flow {#quest-flow}

| State | Facts | Description | Transitions |
| --- | --- | --- | --- |
| Not Started | `Talk Quest Fact = 0` | Player hasn't started the quest yet | Talk to First NPC → Quest Received |
| Quest Received | `Talk Quest Fact = 1` | Player has received the quest from the first NPC | Talk to Second NPC → Completed |
| Completed | `Talk Quest Fact = 2` | Player has completed the quest by talking to the second NPC | Reset Quest → Not Started |

## Quest Setup {#quest-setup}

This guide is split up into 2 sections.

- [**Manifest Section**](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective#manifest-section): Covers how to set the quest up and add the objective.
- [**Sequence Section**](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective#sequence-section): Explains how to make the npc give the quest and the other npc react to the quest.

## Manifest Section {#manifest-section}

**Before Starting**

You must already have created 2 NPCs using the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension) guide.

> For this guide, we will be using a young npc `James` and an old man npc `Old Man`.

![](https://docs.typewritermc.com/assets/optimized-img/npc-example.0bc9ff5.821.avif)

> In this section, we will be creating the quest and adding the objective to it.

### Creating the Quest {#creating-the-quest}

Now inside the manifest page, click on the **+** button in the top right corner and search for `Quest`. Click on the **+** button to add it to your page.

Add Quest

A quest definition

+

#### Configuring the Quest Entry {#configuring-the-quest-entry}

Now inside the quest entry set the following fields:

- **Display Name**: `TalkQuest`
- **Active Criteria**: `Talk Quest Fact >= 1`
- **Completed Criteria**: `Talk Quest Fact = 2`  
  *For this guide I used a permanent fact*

### Adding the Objective {#adding-the-objective}

You now successfully created a quest entry. Now we need to add the objective to the quest.
Click on the **+** button in the top right corner and search for `Add Interact Entity Objective`. Click on the **+** button to add it to your page.

Add Interact Entity Objective

Interact with an entity

+

### Configuring the Objective Entry {#configuring-the-objective-entry}

Inside the objective entry set the following fields:

- **Quest**: `TalkQuest`
- **Criteria**: `Talk Quest Fact = 1`
- **Entity**: `Old Man` (or what you named your second npc)
- **Override Display**: `Talk to the Old Man`

### Manifest Result {#manifest-result}

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/manifest.json)

[static.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/static.json)

## Sequence Section {#sequence-section}

**Before Starting**

It is recommended to have a good understanding of [Interactions](https://docs.typewritermc.com/docs/creating-stories/interactions) and [Facts](https://docs.typewritermc.com/docs/creating-stories/facts) before starting this section.

> In this section, we will be creating the sequence that gives the player the quest and the other npc reacts to the quest.

### Interaction with the First NPC {#interaction-with-the-first-npc}

Now we need to create the interaction with the first npc. This is where the player will receive the quest.
Click on the **+** button in the top right corner and search for `Add Entity Interact Event`. Click on the **+** button to add it to your page.

Add Entity Interact Event

When the player clicks on an entity

+

Inside the entry set the Definition field to the first npc you created. In this case, we will be using `James`.

### Adding dialogue to the First NPC {#adding-dialogue-to-the-first-npc}

Now when you click on the first npc nothing happens. Let's add some dialogue to the npc.

> The following steps are optional, but recommended to make the quest more immersive.

1. Add a `New Option` to your sequence and set the following fields:
   - **Text**: `Could you help me with something?`
   - **Option 1**: `Yeah sure, whats up?`
   - **Option 2**: `No sorry.`
2. Now in the option 1 add a trigger for a spoken with fields:
   - **Text**: `Go talk to that old man on the other side.`
   - **Duration**: `2s 500ms`
3. Inside that spoken add a modifier: `Talk Quest Fact = 1`

### Interaction with the Second NPC {#interaction-with-the-second-npc}

Now you have created the first npc interaction. Now we need to create the second npc interaction. This is where the player will complete the quest.
Add a new `Add Entity Interact Event` entry and set the Definition field to the second npc you created. In this case, we will be using `Old Man`.

Add Entity Interact Event

When the player clicks on an entity

+

### Configuring the Second NPC Interaction {#configuring-the-second-npc-interaction}

Now we will make the interaction trigger a spoken. To do this right click on the `Entity Interact Event` and select `Link with ...` select the `Triggers | 1` and search for `Add Spoken`.

Add Spoken

Display a animated message to the player

+

#### Configuring the spoken {#configuring-the-spoken}

Inside the spoken entry set the following fields:

- **Criteria**: `Talk Quest Fact = 1`
- **Modifier**: `Talk Quest Fact = 2`
- **Text**: `Thanks for going to me!`

### Sequence Result {#sequence-result}

[sequence.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/sequence.json)

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/manifest.json)

[static.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/static.json)

## Result {#result}

Now you have successfully created a quest where the player interacts with an npc and completes the quest by talking to a different npc.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/talk-objective/talk-objective-result.webm"></video>

**Quest Status Changes**

In this video you can see that when the quest starts and ends it shows a title and some extra effects. To also add this read: **SOON**

**Visualizing the Path**

You can also visualize the path of the quest by using the `Interact Entity Objectives Path Stream` entry.

Add Interact Entity Objectives Path Stream

A Path Stream to Interact Entity Objectives

+

Inside the entry set the `Road` field to a Road Network you created and it will visualize the path to the npc for you!

Read more about road networks in the [Road Network Documentation](https://docs.typewritermc.com/docs/creating-stories/road-network).
