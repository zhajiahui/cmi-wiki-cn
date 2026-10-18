# Adding entities

**Before starting**

It's best to first read [Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics) before starting this tutorial.

**Entity Extension**

You must have installed the Entity Extension before starting this tutorial.

In this tutorial, you will learn how to add entities to your interactions.

## Adding an entity {#adding-an-entity}

Firstly click on the + icon in the top right corner of the panel and search for `Add Entity Cinematic`. Add it to your page by clicking on the + icon.

Add Entity Cinematic

Use an animated entity in a cinematic

+

### Selecting the definition {#selecting-the-definition}

Now in the inspector, click on `Select a entity_definition` and select the type of entity you want to have as an NPC, but for this tutorial, we will use the `Add Npc Definition`. Now you will need to select a manifest page or create one by clicking on `Add manifest`.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/select-entity-definition.webm"></video>

Then inside that NPC Definition you can follow the [entity-extension](https://docs.typewritermc.com/docs/creating-stories/entity-extension) Tutorial to create a Beautiful NPC.

### Adding segments {#adding-segments}

Now we need to add a segment to our track. You can do this by clicking in the inspector at Operations on `Add Segment`. This will add a segment to your track.

### Configuring the segment {#configuring-the-segment}

In the segment, we now need to add an artifact. You can do this by clicking on `Select a entity_cinematic_artifact` and selecting your artifact, or create one by clicking on `Add Entity Cinematic Artifact`. Then select or create your static page.

### Requesting the content mode. {#requesting-the-content-mode}

Now, back on the cinematic page, click on the  icon in the inspector just above the artifact. This will open the content mode in Minecraft. If you like, you can read what the items do in your inventory just by hovering over them with your mouse, but we will just use the book for now.
By clicking on the book, Typewriter will start recording your movements and items that you were holding before you requested the content mode.

#### Recording the NPC {#recording-the-npc}

**Items in inventory**

The items you were holding before you requested the content mode will be the items that the NPC will be holding.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/recording.webm"></video>

#### Using the playback items {#using-the-playback-items}

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/playback.webm"></video>

## result {#result}

Now that you have successfully added the entity, you can view it in your cinematic.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/cinematic-npc-result.webm"></video>
