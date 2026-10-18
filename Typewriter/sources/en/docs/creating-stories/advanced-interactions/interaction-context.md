# Interaction Context

**Before starting**

For this tutorial we recommend reading the [Interactions](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions) guide as we will build upon this.

In this tutorial, you will learn about interaction contexts and how to use them. We will create an interaction where the player needs to specify the amount of flowers given.

## What is an interaction context? {#what-is-an-interaction-context}

Interaction contexts is a powerfull concept that allow you to pass variables to subsequent entries in a sequence. This means you can capture user input, store it, and use it later to drive dynamic interactions  
whether it's using the input in future steps or triggering actions (like spawning effects on a clicked block). This flexibility makes your stories more adaptive and engaging.

**Multiple Types**

For this tutorial we will use an `integer input dialogue` but there are more types like a `string input dialogue`.

## Creating an input dialogue {#creating-an-input-dialogue}

In this tutorial, we will create an interaction where the player needs to specify the amount of flowers given. We will use an integer input dialogue to capture the amount of flowers given by the player.
To add an integer input dialogue, go to the top right corner of the panel and click on the + icon. Search for `Add Integer Input Dialogue` and add it to your sequence  
(For this guide we linked it to the spoken from [Interactions](https://docs.typewritermc.com/docs/creating-stories/advanced-interactions)).

Add Integer Input Dialogue

An input dialogue which excepts an integer

+

## Configuring the integer input dialogue {#configuring-the-integer-input-dialogue}

Now inside of the integer input dialogue set the text you want. For this guide we will use: `How many flowers would you like?`.

**Range**

If you want you also can configure the range of an integer input dialogue

## Adding the give flowers {#adding-the-give-flowers}

Now we need to create an event that gets triggered when the player specifies the amount of flowers. Right-click on the `Integer Input Dialogue` entry and click on `+ link with ...` to open the search menu. Search for `Give Item` and add it to the page.

Add Give Item

Give an item to the player

+

**Give Item Entry**

If you don't how the Give Item Entry works than you should first read [Giving Items](https://docs.typewritermc.com/docs/creating-stories/interactions/items)

## Configuring the give flowers {#configuring-the-give-flowers}

Now you can configure the give entry. For this guide we will use a `Red Tulip`.

**Custom Item**

For the item you need to use the custom item. As of right now the amount of a serialized item can't be a variable.

### Creating the interaction context variable {#creating-the-interaction-context-variable}

Now inside the Give Item Entry at the item field create an extra component and select amount. Now at the amount field click on the  and search for `Add Interaction Context Variable`.

Add Interaction Context Variable

Fill in a field with some data from another entry

+

When you have done that you can than select the `Integer Input Dialogue` entry at the entry field.

#### Video Tutorial {#video-tutorial}

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/configure-spoken-interaction-context.webm"></video>

## Result {#result}

Now when the player specifies the amount of flowers, the player will receive the amount of flowers specified.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/interaction-context-result.webm"></video>
