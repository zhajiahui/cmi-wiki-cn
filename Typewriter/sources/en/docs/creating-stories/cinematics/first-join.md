# First Join Cinematic

**Before Starting**

Before starting, it's recommended to read the following sections: [Interactions](https://docs.typewritermc.com/docs/creating-stories/interactions), [Cinematics](https://docs.typewritermc.com/docs/creating-stories/cinematics), and [Facts](https://docs.typewritermc.com/docs/creating-stories/facts). Ensure you have a sequence and a cinematic page created.

In this tutorial, you'll learn how to create a cinematic that plays when a player joins the server for the first time.

## Adding the Join Entry {#adding-the-join-entry}

First, we need to add the `Add On Player Join` entry to our sequence. This can be done by clicking on the + icon in the top right corner of the panel and searching for `Add On Player Join`. Add it to your page by clicking on the + icon.

Add On Player Join

When the player joins the server

+

## Waiting for Interaction {#waiting-for-interaction}

**Early Start Cinematic**

Before a player fully loads the server, it is possible for Typewriter to start the cinematic prematurely. This can occur if the player has a slow internet connection or a low-performance computer. In such cases, the player may join the server in the middle of the cinematic instead of at the beginning. To address this, it is recommended to add an option or a delay where the player needs to perform an action before the cinematic starts.

To add an option to your sequence, it's best to read the [Options](https://docs.typewritermc.com/docs/creating-stories/interactions/options) page. For this tutorial, we will have a `New Option` with a `Start Cinematic` option.

### Configuring the Criteria {#configuring-the-criteria}

**Option**

If you are using the option from the [waiting for interaction](https://docs.typewritermc.com/docs/creating-stories/cinematics/first-join#waiting-for-interaction), you need to configure the following steps in the option and **NOT** inside the start cinematic.

Now we need to configure the criteria for the cinematic. This can be done by clicking on the `+` icon in the inspector next to the criteria field. Then, you can select the fact you want to use. For this tutorial, we will use a permanent fact called `First Join` with the group set to a player group.

![first-join-fact](https://docs.typewritermc.com/assets/optimized-img/first-join-fact.2803121.524.avif)

Inside the criteria, set the operator to `==` and the value to `0`.

### Configuring the Modifier {#configuring-the-modifier}

You have configured the criteria, but now we need to modify the fact so that when you join again, the cinematic is not played. This can be done by clicking on the `+` icon in the inspector next to the modifier field. Then, you can select the fact you want to modify. For this tutorial, we will use the same fact as the criteria. Inside the modifier, set the operator to `=` and the value to `1`.

Now your inspector should look like this:

![add-cinematic-fields](https://docs.typewritermc.com/assets/optimized-img/add-cinematic-fields.b15ef7e.535.avif)

## Adding the `Add Cinematic` Entry {#adding-the-add-cinematic-entry}

Now we need to add the `Add Cinematic` entry to our sequence. This can be done by right-clicking on the `New On Player Join` entry and selecting `+ Link with ...`. Then, search for `Add Cinematic` and click on the + icon to add it to your sequence. Now your sequence page should look like this:

![Add-Cinematic](https://docs.typewritermc.com/assets/optimized-img/add-cinematic.9e15988.735.avif)

Inside the `New Cinematic`, select the cinematic you want to trigger via the inspector at the page field. For this tutorial, we will use the `Tutorial_Cin` cinematic.

## Result {#result}

Now, when a player joins the server for the first time, the cinematic will play. When the player joins again, the cinematic will not play.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/cinematics/first-join-result.webm"></video>
