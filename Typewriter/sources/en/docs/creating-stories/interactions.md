# First Interaction

**Before starting**

This guide assumes that you have already installed the [Basic Extension](https://docs.typewritermc.com/docs/getting-started/installation#basic-extension).

Also, make sure you have read the [layout](https://docs.typewritermc.com/docs/getting-started/layout) documentation and created a **sequence** page.

Let's create our first interaction. Our example interaction will have the following steps:

1. The player clicks on a flower.
2. A chat dialogue opens.

If you need any assistance during the process, feel free to ask for help on our [Discord](https://discord.gg/HtbKyuDDBw).

## What are interactions? {#what-are-interactions}

An interaction occurs when the player interacts with something and triggers an event. In this tutorial, the player clicking on the flower is the interaction, and the chat dialogue is the event that gets triggered.

## Creating an interaction {#creating-an-interaction}

Let's get started by creating an entry. Click on the + icon in the top right corner of the panel and search for `on interact with block`. Add it to your page by clicking on the + icon.

Add On Interact With Block

When the player interacts with a block

+

### Configuring the interaction {#configuring-the-interaction}

In the inspector, set the block to `Red Tulip` (1) and the name to `on flower click` (2)

![Configuring an interact with flow entry](https://docs.typewritermc.com/assets/optimized-img/on_flower_click.60a7569.269.avif)

## Creating an event {#creating-an-event}

Now we need to create an event that gets triggered when the player clicks on the flower. Right-click on the `On Flower Click` entry and click on `+ link with ...` to open the search menu. Search for `Add Spoken` and add it to the page.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/add-spoken.webm"></video>

### Configuring the event {#configuring-the-event}

In the inspector, set the text to `Hello! I am a flower.` and set the duration to `1s`.

### Configuring the speaker {#configuring-the-speaker}

Follow these steps to configure the speaker:

1. Click on the text `Select a speaker` and in the search menu, click on `Add Simple Speaker`.
2. Select `Add static` and give that static page a name.
3. Click on the simple speaker.
4. Inside the inspector, set the Display Name to `A beautiful flower`.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/simple-speaker.webm"></video>

## Result {#result}

You can now publish your pages, and in-game, it should look like this when clicking on the flower:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/final-result-default.webm"></video>
