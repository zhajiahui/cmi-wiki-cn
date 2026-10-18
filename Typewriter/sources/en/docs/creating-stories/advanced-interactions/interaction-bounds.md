# Interaction Bounds

**Before starting**

This guide assumes that you have already installed the [Basic Extension](https://docs.typewritermc.com/docs/getting-started/installation#basic-extension).

**Before Starting**

This guide is made for advanced users. It is recommended to have a good understanding of how [Interactions](https://docs.typewritermc.com/docs/creating-stories/interactions) work and function!

Before starting this guide there is some theory you need to know about interaction bounds before you should use them in your stories.

## What are interaction bounds? {#what-are-interaction-bounds}

Interaction bounds are conditions that confine an interaction to a specific action or space. They provide control over when and how interactions can occur or be interrupted. A common example is cancelling a dialogue when the player walks away from an NPC.

### Two Modes of Bounds {#two-modes-of-bounds}

Interaction bounds operate in two distinct modes:

#### Interruption Mode {#interruption-mode}

When in Interruption Mode, if the player breaks the bounding condition (such as walking out of a defined area), the interaction will be immediately cancelled. This is useful for casual conversations where you want to allow players the freedom to walk away.

#### Blocking Mode {#blocking-mode}

In Blocking Mode, the player is prevented from violating the bounding condition altogether. The player cannot, for example, walk away from an important dialogue. This ensures players experience critical story moments fully before proceeding.

| Mode | Behaviour | Use Case |
| --- | --- | --- |
| Interruption | Interaction cancels when bound is broken | Optional dialogues, ambient interactions |
| Blocking | Player cannot break the bound | Critical story moments, important instructions |

### How Modes Are Determined {#how-modes-are-determined}

The mode is determined by comparing the **priority** of the interaction with the **priority** of the bound:

- If the interaction has a **higher priority** than the bound → **Blocking Mode**
- If the interaction has the **same or lower priority** than the bound → **Interruption Mode**

**tip**

Entries inherit their priority from the page they belong to. You can set page priorities in the page properties panel.

## How to use interaction bounds {#how-to-use-interaction-bounds}

Now that we have covered the theory, let's see how to use interaction bounds in your stories.  
For this guide, we created 3 different examples to show you how to use interaction bounds in different situations:

**Interruption Mode**

**Guide**

In this guide, we will show an example of how to make an interrupting interaction bound when the player walks away from a flower.

**Initial Setup**

This guide will build upon the [Interactions Guide](https://docs.typewritermc.com/docs/creating-stories/interactions) and requires you to have at least an
`On Interact With Block` entry in your editor.

#### Adding the Interaction Bound {#adding-the-interaction-bound}

To add an interaction bound, right-click on the `On Interact With Block` entry and select `Link with ...`, search for `Player Radius Interaction Bound` and add it to your sequence.

Add Player Radius Interaction Bound

An interaction bound around a player

+

#### Configuring the Interaction Bound {#configuring-the-interaction-bound}

Now that we have added the interaction bound, we need to configure it.  
Select the `Player Radius Interaction Bound` entry and open the inspector

You now got 2 options to configure

- **Radius**: The radius of the interaction bound. This is the distance from the player where the interaction will be cancelled.
- **zoom**: If the player's camera should zoom in when the player is nearby and zoom out when the player is walking away.

Now, your sequence should look a bit like this:

![](https://docs.typewritermc.com/assets/optimized-img/interaction-bound-player-radius-interupting.9abd31a.1585.avif)

#### Result {#result}

Now, your interaction should look like this:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/interaction-bound-interupting-result.webm"></video>

**Blocking Mode**

**Guide**

In this guide, we will show an example of how to make a blocking interaction bound when the player walks away from a flower.

**Initial Setup**

This guide will build upon the [Interactions Guide](https://docs.typewritermc.com/docs/creating-stories/interactions) and requires you to have at least an
`On Interact With Block` entry in your editor.

#### Adding the Interaction Bound {#adding-the-interaction-bound-1}

To add an interaction bound, right-click on the `On Interact With Block` entry and select `Link with ...`, search for `Player Radius Interaction Bound` and add it to your sequence.

Add Player Radius Interaction Bound

An interaction bound around a player

+

#### Making it a blocking interaction {#making-it-a-blocking-interaction}

What you now have done is created an interrupting interaction bound. To make it a blocking interaction bound, you need to set the priority of the `Spoken` entry to a higher priority than the `Player Radius Interaction Bound` entry.  
To do this,

1. create a new sequence page. Name it something like `Blocking Bounds`.
2. Select the `Player Radius Interaction Bound` entry and hold it for a few seconds.
3. Drag it to the new page and drop it there.
4. Right-click on the page that has the `Spoken` in it.
5. **Select `Change Priority` and set it to a higher number than the `Player Radius Interaction Bound` entry.**   
   For example, if the `Blocking Bounds` page has a priority of 0, set the page containing the `Spoken` entry to 1.
6. Now, your sequence should look like this:

![](https://docs.typewritermc.com/assets/optimized-img/interaction-bound-player-radius-blocking.8643896.1027.avif)

#### Result {#result-1}

Now, your interaction should look like this:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/interaction-bound-blocking-result.webm"></video>

**Interruption Mode (Entity Extension)**

**Guide**

In this guide, we will show an example of how to make an interrupting interaction bound when the player walks away from a NPC.

**Entity Extension**

This guide requires you to already have created a NPC using the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension)

**SOON**

This guide is not yet available. Please check back later.
