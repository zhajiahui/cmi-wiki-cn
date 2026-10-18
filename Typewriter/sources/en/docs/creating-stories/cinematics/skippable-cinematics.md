# Skippable Cinematics

**Before starting**

It's best to first read [Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics) before starting this tutorial.

In this tutorial, you will learn how to allow players to skip certain parts of your cinematics.

## Adding a skippable cinematic {#adding-a-skippable-cinematic}

Firstly click on the + icon in the top right corner of the panel and search for `Add Skippable Cinematic`. Add it to your page by clicking on the + icon.

Add Skip Cinematic

Allows players to manually skip the cinematic

+

### Configuring the skippable cinematic {#configuring-the-skippable-cinematic}

Inside the inspector of the skip cinematic you can choose between `SNEAK` or `SWAP_HANDS` at the confirmation key field. This key will be the key the player has to press to skip the cinematic. This guide will use the SNEAK key to skip the cinematic.

## Adding a skippable part {#adding-a-skippable-part}

Now inside the inspector of the skippable cinematic you can add a new segment by clicking on the `Add segment` text at the operations section. This will create a new segment  
At the fields Start and End frame you can set the timings you want a player to be able to skip a cinematic. For this guide this will be 0 and 100.

## result {#result}

Now you have a skippable cinematic that can be skipped by pressing the key you set in the confirmation key field.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/skip_cinematic_result.webm"></video>
