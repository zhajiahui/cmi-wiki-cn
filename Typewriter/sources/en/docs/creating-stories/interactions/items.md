# Giving items

**Before starting**

It's best to first read [First Interaction](https://docs.typewritermc.com/docs/creating-stories/interactions) before starting this tutorial.

In this tutorial, you will learn how to give items in your interactions.

## Adding the give item {#adding-the-give-item}

To add a give item entry, follow these steps:

1. Right-click on your entry and select `+ Link with ...`.
2. Search for `Add give item` and click on the + icon to add it to your sequence.

Add Give Item

Give an item to the player

+

## Configuring the give item {#configuring-the-give-item}

The giving item entry has two types of giving an item: A custom item and a Serialized item.

### Differences {#differences}

**Custom Item**

The custom item allows you to customize almost all the aspects of the item.

**NBT**

A custom item can't contain NBT data.

**Serialized Item**

The serialized item gives you the ability to use the Item Capturer and capture the item from in-game.

**Not Editable**

You can't edit a serialized item. Only the name can be changed.

### Using the Item Capturer(Serialized Item) {#using-the-item-capturerserialized-item}

The easy way is to use the item capture because it just copies the item that you are currently holding in-game to the panel. To do this, just click on  icon next to the `item` field.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/item-capturer.webm"></video>

### Configuring it yourself(Custom Item) {#configuring-it-yourselfcustom-item}

You can also configure the item yourself. Inside the item field select `Custom Item`. Press the + icon right next to the `Components(0)` text to add one of the following components:

1. **Amount**: The amount of items given to the player.
2. **Flag**: Specific options for the item.
3. **Lore**: The lore of the item.
4. **Material**: This is the item that the player will get.
5. **Item Name**: This is the name of the item.

## Result {#result}

After you configured your item, you can test your interaction by clicking the publish button, and then it should look something like this:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/final-result-give-item.webm"></video>
