# Option Bound

**Before Starting**

This guide is made for advanced users. It is recommended to have a good understanding of how [Interactions](https://docs.typewritermc.com/docs/creating-stories/interactions) and [Interaction Bounds](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions/interaction-bounds/) work.

**Story**

The story of this guide will be a waiter that is asking at wich table the player would like to sit.

In this guide, you will learn how to create an option that has a interaction bound applied to it. This means that while scrolling thrue the options the players bound location can change.

## Creating the option {#creating-the-option}

**Entity Extension**

For this guide we will be connecting the option to an `On Entity Interact Event` from the [Entity Extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension).

### Creating the Option Dialogue {#creating-the-option-dialogue}

First, we'll create an option dialogue that will be shown when the player interacts with our waiter NPC:

1. Right-click on your `On Entity Interact Event` entry and select `+ Link with ...`
2. Search for `Option` and add it to your sequence

Add Option

Display a list of options to the player

+

## Configuring the option {#configuring-the-option}

Now that we have added the option, we need to configure it. Select the `Option` entry and open the inspector.

Configure the dialogue text to be: `Welcome, at which table would you like to sit?` and the options:

- **Spruce Table**
- **Birch Table**
- **Dark Oak Table**
- **Go Back**

Learn how to configure the options in the [Options Guide](https://docs.typewritermc.com/docs/creating-stories/interactions/options).

## Adding the Interaction Bound {#adding-the-interaction-bound}

To add an interaction bound, right-click on the `On Entity Interact Event` entry and select `Link with ...`, search for `Lock Interaction Bound` and add it to your sequence.

Add Lock Interaction Bound

An interaction bound that locks the camera for the player

+

## Configuring the Interaction Bound {#configuring-the-interaction-bound}

Select the `Lock Interaction Bound` entry and open the inspector.

### Adding a Case Variable {#adding-a-case-variable}

Enable the Target Position setting in the inspector and click on the  icon, search for `Add Case Variable` and add it to a facts page.

Add Case Variable

A variable that returns a value based on a selection

+

### Configuring the Case Variable {#configuring-the-case-variable}

Select the `Case Variable` entry and open the inspector.

**Case Variable**

The case variable stores different locations based on a supplied number:

- This system is **1-based** (not 0-based)
- Case 0 = default location (used when no matching case is found)
- If no case matches, the default location is used

For our restaurant scenario:

1. Set a **default location** using the  icon (shown when no case matches)
2. Click the `+` icon in the cases field to add our four viewing positions:
   - **Case 1**: Spruce Table location
   - **Case 2**: Birch Table location
   - **Case 3**: Dark Oak Table location
   - **Case 4**: Go Back location (original position)
3. Capture each position using the  icon
4. Your `Case Variable` should look like this:

![](https://docs.typewritermc.com/assets/optimized-img/option-bound-case-variables.4ee1eef.522.avif)

### Adding a Interaction Context Variable {#adding-a-interaction-context-variable}

Now when the player scrolls thrue the options nothing happens yet. To do this we need to add a `Interaction Context Variable` to the `Case Variable` inside the `Lock Interaction Bound` entry.

To do this, click on the  icon at the `Selection` field inside the `Case Variable` entry and search for `Interaction Context Variable`.

Add Interaction Context Variable

Fill in a field with some data from another entry

+

### Configuring the Context Variable {#configuring-the-context-variable}

This variable automatically provides the currently selected option index:

1. Select the `Interaction Context Variable` entry
2. In the inspector, click on `Select a Entry`
3. Choose the `Option` entry we created earlier
4. Your `Interaction Context Variable` should look like this:

![](https://docs.typewritermc.com/assets/optimized-img/option-bound-target-position.daa5430.521.avif)

**About the Case Count**

The image shows `Cases (0)` because I configured the cases globally in the facts page rather than locally in this specific entry.  
You can configure variables via 2 ways:

- globally (in the facts page for reuse across multiple entries)
- locally (within a specific entry).

The functionality works the same either way - the system will use the appropriate position based on the selected option index.

## Result {#result}

Now your pages should look like this:

**Sequence Page**

![](https://docs.typewritermc.com/assets/optimized-img/option-bound-sequence.3d15527.1294.avif)

**Static Page**

![](https://docs.typewritermc.com/assets/optimized-img/option-bound-static.6a7809d.892.avif)

When players interact with the waiter NPC, they'll see the option menu. As they scroll through the different table options, their view will automatically shift to look at each table, creating an immersive way to make a choice.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/option-bound-result.webm"></video>

**Confirmation Key**

While writing these docs a bug was found with the confirmation key. If your confirmation key is `SWAP_HANDS`(F) than while inside a interaction bound the dialogue will not continue. You need to press SPACE to do this!

## How it Works {#how-it-works}

The Option Bound system works through these key components:

1. **Lock Interaction Bound** - Controls the player's position and view
2. **Case Variable** - Stores different positions for each option
3. **Interaction Context Variable** - Provides the current option index
4. **Option Entry** - Provides the dialogue interface

When the player scrolls through options, the Interaction Context Variable updates with the new option index, which selects the corresponding position from the Case Variable, and the Lock Interaction Bound applies this position to the player.

This creates a seamless experience where the player's view changes based on which option they're currently hovering over, allowing them to "look at" their choices in the game world.
