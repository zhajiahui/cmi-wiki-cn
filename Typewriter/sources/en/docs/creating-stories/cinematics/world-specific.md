# World Specific Cinematics

**Before starting**

It's best to first read [Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics) before starting this tutorial.

In this tutorial, you will learn how to create world-specific cinematics. This feature allows you to create 1 cinematic that can be used in multiple worlds.

## Creating the dynamic variable {#creating-the-dynamic-variable}

First, we need to create a dynamic variable. This variable will be used to determine which world the player is in. To do this please follow the these steps:

1. Go to your camera cinematic and click on a segment
2. Inside the segment at 1 of your paths click on the  icon.
3. Search for `Player World Position Variable` and click on it to add it to your segment.

Add Player World Position Variable

Absolute Position in the players world

+

### Configuring the dynamic variable {#configuring-the-dynamic-variable}

**repeat**

Repeat this step for all paths inside the camera cinematic segment.

Now inside the inspector of the **camera cinematic segment** you can set the coordinates of your cinematic.

![Configuring the dynamic variable](https://docs.typewritermc.com/assets/optimized-img/world-specific-player-variable.47acd57.517.avif)

#### Where is the world value? {#where-is-the-world-value}

Good question, the world value is gone because we are using the `Player World Position Variable` to determine the world.  
The world the player is in will be the world used.

## Result {#result}

**Entity**

For this guide we used an entity cinematic from the [entities](https://docs.typewritermc.com/docs/creating-stories/cinematics/entities) tutorial and an [actionbar dialogue](https://docs.typewritermc.com/docs/creating-stories/cinematics/dialogue). This is to demonstration the use of the dynamic variable.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/world-specific.webm"></video>
