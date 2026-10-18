# Interacting with an entity

**Before starting**

It's best to first read [Entities & NPC's](https://docs.typewritermc.com/docs/creating-stories/entity-extension) before starting this tutorial.

In this tutorial, you will learn how to interact with an entity.

## Adding the entity interact event {#adding-the-entity-interact-event}

First, we need to add the `Add On Entity Interact Event` entry to our sequence. This can be done by clicking on the + icon in the top right corner of the panel and searching for `Add On Entity Interact Event`. Add it to your page by clicking on the + icon.

Add Entity Interact Event

When the player clicks on an entity

+

### Selecting the definition {#selecting-the-definition}

Now inside the inspector of the `New Entity Interact Event` at the definition field, select the definition of the entity you want to interact with. (For this tutorial that will be Oliver)

![Entity Interact Event Fields](https://docs.typewritermc.com/assets/optimized-img/entity-interact-event-fields.f2ab662.540.avif)

## Adding the event. {#adding-the-event}

Now we need to add an event that gets triggered when the player interacts with the entity (For this tutorial we will use a spoken). Right-click on the `New Entity Interact Event` entry and click on `+ link with ...` to open the search menu. Search for `Add Spoken` and add it to the page.

Add Spoken

Display a animated message to the player

+

Set the speaker to the oliver definition and text field to `Hello I am Oliver.`.

## Result {#result}

You can now publish your pages, and in-game, it should look like this when interacting with Oliver:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/entity-extension/interact-entity-result.webm"></video>
