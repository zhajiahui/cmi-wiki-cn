# Conditional dialogue

**Before starting**

It's best to first read [First Interaction](https://docs.typewritermc.com/docs/creating-stories/interactions) [Facts](https://docs.typewritermc.com/docs/creating-stories/facts) before starting this tutorial.
Also, make sure you have created a **sequence** page.

In this tutorial, you will learn how to create conditional dialogue. This means that if the player has a certain fact set to a specific value, it will then display the correct dialogue.

## Adding a spoken {#adding-a-spoken}

First we need to add a spoken. This can be learned by following the [First Interaction](https://docs.typewritermc.com/docs/creating-stories/interactions) tutorial.

## Configuring the spoken {#configuring-the-spoken}

In the spoken we will set the field text to `Hey you clicked me for the first time.`

### Setting the Criteria {#setting-the-criteria}

Now we need to configure the criteria for the spoken. This can be done by clicking on the + icon in the inspector next to the criteria field. Then, you can select the fact you want to use. For this tutorial, we will use a permanent fact called `Flower Clicked` with the group set to a player group.

![Flower Clicked Fact](https://docs.typewritermc.com/assets/optimized-img/flower-clicked-fact.dfda5a1.539.avif)

Inside the criteria, set the operator to `==` and the value to `0`.

### Configuring the Modifier {#configuring-the-modifier}

You have configured the criteria, but now we need to modify the fact so that when you click the flower again, a different spoken is displayed. This can be done by clicking on the + icon in the inspector next to the modifier field. Then, you can select the fact you want to modify. For this tutorial, we will use the same fact as the criteria. Inside the modifier, set the operator to `=` and the value to `1`.

![Add Spoken Fields](https://docs.typewritermc.com/assets/optimized-img/add-spoken-fields.2df9135.528.avif)

## Adding the second spoken {#adding-the-second-spoken}

Now we need to add the second spoken. This can be done by right-clicking on the `On Interact Block Event` entry and selecting `+ Link with ...`. Then, search for `Add Spoken` and click on the + icon to add it to your sequence.  
In the text field we will set `Wow you clicked me again!`
Your sequence page should look like this:

![Conditional dialogue sequence](https://docs.typewritermc.com/assets/optimized-img/conditional-dialogue-sequence.6fa3c22.863.avif)

### Configuring the second spoken Criteria {#configuring-the-second-spoken-criteria}

Now we need to configure the criteria for the second spoken. This can be done by clicking on the + icon in the inspector next to the criteria field. Then, select the `Flower Clicked` fact again. Inside the criteria, set the operator to `==` and the value to `1`.

### Additional dialogue {#additional-dialogue}

To add more dialogues or interactions when you click the flower, set another modifier with the operator to `=` and the value to `2` (or any other value), then repeat the previous steps.

## Result {#result}

Now, when you click the flower for the first time, the first spoken will be displayed. When you click the flower again, the second spoken will be displayed.

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/interactions/final-result-conditional-dialogue.webm"></video>
