# Conditional NPC showing

**NPC created**

In this tutorial, we assume you already have created an entity.  
If you haven't done that yet, please follow the [entity extension tutorial](https://docs.typewritermc.com/docs/creating-stories/entity-extension) first.

In this tutorial, you will learn how to conditionally show an entity using audiences.

## Adding an audience entry {#adding-an-audience-entry}

There are a lot of different audience entries available. For this tutorial, we will use Game Time audience, but all others have similar features.

Firstly, click on the + icon in the top right corner of the panel and search for `New Game Time Audience`. Add it to your page by clicking on the + icon.

Add Game Time Audience

Filters an audience based on the game time

+

## Adding it onto your entity instance. {#adding-it-onto-your-entity-instance}

Now hold your entity instance and drag it onto the `New Game Time Audience` entry. This will link the audience to the entity.

It should now look something like this:

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/04-entity-extension/assets/conditional/manifest.json)

## Configuring the audience {#configuring-the-audience}

Inside the audience entry, there are 2 fields:

- **Children**: This is where you can add the entities that should be shown when the audience is met.
- **Active Times**: This will make that the Children of the audience is only showed when this condition is met.
- **Inverted**: This will invert the audience, meaning that the entity will only be shown when the audience is not met.

## Result {#result}

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/entity-extension/conditional-npc-result.webm"></video>
