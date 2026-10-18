# Questing

**Quest Extension**

You must have installed the Quest Extension before proceeding with any quest-related features.

**Writers Note**

The questing section on our docs is currently being rewritten. If you want the old documentation that is complete read: [**Old Quest Documentation**](https://docs.typewritermc.com/0.7.0/docs/creating-stories/questing)

## Typewriter's Unique Approach to Quests {#typewriters-unique-approach-to-quests}

**The Big Idea**

In Typewriter, quests are **visual reflections** of your game state, not the drivers of it. Use permanent facts to track real progress, and let quests simply display that progress to players.

### 🔑 Key Concept {#-key-concept}

Unlike traditional quest plugins where completing quests directly triggers progression, Typewriter separates:

- **Game State** - Facts that drive true progression
- **Quest Display** - What players see in the UI

### ⚙️ How Quests Work {#️-how-quests-work}

InactiveActiveCompleted

**Quest state is determined by:**

1. If **Completed Criteria** are met → Completed
2. If **Active Criteria** are met → Active
3. Otherwise → Inactive

### 💪 Why This Is Powerful {#-why-this-is-powerful}

**🤔 Open-ended Objectives**

Guide players with goals, not just clicks. Use immersive objectives like **`Find a way into the locked study`** instead of the rigid **`Use the Silver Key on the Study Door`**.

**🕵️‍♀️ Multiple Entry Points**

Provide various ways to begin the same quest. The investigation can begin by **`Being briefed by the chief detective`** OR by independently finding the **`Discarded Ransom Note`**.

**⏳ Evolving Objectives**

Objectives can update based on time or lack of progress. If **`Search the market district for clues`** yields no results after a while, it might refine to **`Focus your search near the merchant stalls`**.

**🗺️ Contextual Objectives**

Display the most relevant task based on context. At the plaza, show **`Ask locals about the suspect`**, but enter the nearby alley, and it updates to **`Check the alley for escape routes`**.

**🌿 Branching Narratives**

Adapt the quest depending on the players' actions. Based on evidence found, objectives can change to **`Investigate the garden shed`** or **`Confront the butler`**.

**⚖️ Lasting Consequences**

Prior decisions influence current tasks. A corrupt detective might get **`Plant misleading evidence`** instead of **`Collect all available evidence`**.

## Visual Guide: How Facts Drive Quests {#visual-guide-how-facts-drive-quests}

Quest Progression Flow

How facts drive quest states in Typewriter

| State | Facts | Description | Transitions |
| --- | --- | --- | --- |
| Not Started | `Quest Fact = 0` | Player hasn't started the quest yet | Talk to NPC → Searching |
| Searching | `Quest Fact = 1` `Item Fact = 0` | Player is looking for the required item | Find Item → Item Found; Abandon Quest → Not Started |
| Item Found | `Quest Fact = 1` `Item Fact >= 1` | Player has found the required item | Return to NPC → Completed; Lose Item → Searching |
| Completed | `Quest Fact = 2` | Quest has been completed | Reset Quest → Not Started |

## Creating a Quest {#creating-a-quest}

In Typewriter, quests are created using the **Quest** entry.

**Quest Entry**

The Quest Entry is only a visual representation of the quest state. It does not affect the quest state itself.

**Before Starting**

You must have a decent understanding of Typewriter's [**Facts**](https://docs.typewritermc.com/docs/creating-stories/facts) and [**Interactions**](https://docs.typewritermc.com/docs/creating-stories/interactions) before starting with creating quests.

### Adding the Quest Entry {#adding-the-quest-entry}

In the top right corner of the Typewriter editor, click on the **+** button and search for `Quest`. Click on the **+** button to add it to your page.

Add Quest

A quest definition

+

### Configuring the Quest Entry {#configuring-the-quest-entry}

Display Name

The name shown in player's quest log (e.g., **`QuestGuide`**)

Active Criteria

Condition for quest visibility (e.g., **`Permanent Fact >= 1`**)

Completed Criteria

Condition for quest completion (e.g., **`Permanent Fact == 5`**)

### Visualizing the Quest Entry {#visualizing-the-quest-entry}

In this editor you can increase and decrease the permanent fact used in the image on the right.

Try setting it from 0 to 5!

TW_STATUS_EDITOR_PLACEHOLDER

![Quest Configuration](https://docs.typewritermc.com/assets/optimized-img/quest-configuration.c3d537d.521.avif)

## Adding objectives {#adding-objectives}

You now have created a quest entry, but it doesn't have any objectives yet. For this documentation we have created multiple guides on how to do different objectives.

- **Talk to NPC**: [**Talk Objective**](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective)
- **Kill 10 Zombies**: [**Kill Objective**](https://docs.typewritermc.com/docs/creating-stories/questing/kill-zombie-objective)
- **Gather 10 Emeralds**: Soon
- **Give to Npc (Mail delivery)**: Soon

## Displaying the Quest {#displaying-the-quest}

It is also possible to display the quest to players via placeholders. Read: **BEING WRITTEN** to learn more about this.
