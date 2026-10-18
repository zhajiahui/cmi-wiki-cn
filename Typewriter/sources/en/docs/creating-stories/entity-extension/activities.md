# Entity Activities

**Before you begin**

Make sure to read [Entities & NPCs](https://docs.typewritermc.com/docs/creating-stories/entity-extension) before starting this tutorial.

In this tutorial, you'll learn how to assign activities to your entities.

## What are activities? {#what-are-activities}

By default, entities are static. Fortunately, activities can make them dynamic. For example, you can set up an activity that triggers when a player approaches the entity, or at specific moments—such as when the player talks to it. You can even use Road Networks to make entities travel between different nodes!

## Assigning an activity to an entity {#assigning-an-activity-to-an-entity}

In this tutorial, we’ll configure **Oliver** to automatically move along a Road Network. When a player interacts with him, he’ll stop and turn to face them.

To do this, we'll use an **In Dialogue Activity**, which lets you define two separate behaviours: one when the player is talking to the entity, and one for when they're not.

Let’s update Oliver’s instance by adding an `In Dialogue Activity`.

Add In Dialogue Activity

An in dialogue activity

+

## Configuring the activity {#configuring-the-activity}

The `In Dialogue Activity` controls two child activities, depending on whether the player is currently speaking to the entity.

![In Dialogue Activity panel image](https://docs.typewritermc.com/assets/optimized-img/in_dialogue_activity.fea2a9f.648.avif)

- For the **Talking Activity**, we’ll use a `Look Close Activity`, so Oliver will look directly at the player during the conversation.
- For the **Idle Activity**, we’ll use a `Patrol Activity`, allowing Oliver to walk between the nodes of a Road Network.

If you haven’t created a Road Network yet, you can follow this tutorial: [Road Network](https://docs.typewritermc.com/docs/creating-stories/road-network). You'll need to add the nodes you want by clicking on the  button.

![Patrol Activity panel image](https://docs.typewritermc.com/assets/optimized-img/patrol_activity.412a105.532.avif)

## Final result {#final-result}

When a player interacts with Oliver, he will stop patrolling and turn to face them. Once the interaction ends, he will resume his patrol between the Road Network nodes.

### Page Preview {#page-preview}

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/04-entity-extension/assets/activities/pages/manifest.json)

[static.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/04-entity-extension/assets/activities/pages/static.json)

[sequence.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/04-entity-extension/assets/activities/pages/sequence.json)

### In-Game Preview {#in-game-preview}

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/04-entity-extension/assets/activities/result.webm"></video>
