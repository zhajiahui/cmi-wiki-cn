# Custom Commands

**Before starting**

This guide assumes that you have already installed the [Basic Extension](https://docs.typewritermc.com/docs/getting-started/installation#basic-extension).

In this tutorial, you will learn about custom commands and how to create one. We will create a command where you can define a pseudo and an age to display a message to the player.

## Creating a Custom Command {#creating-a-custom-command}

In this tutorial, we will create a command where you can define a pseudo and an age to display a message to the player. We will use a Custom Command Entry to start defining our command.
To add a custom command entry, go to the top right corner of the panel and click on the + icon. Search for `Add Custom Command`, add it to your manifest and name it.

Add Custom Command

Create custom commands with parameters

+

## Creating the arguments {#creating-the-arguments}

Now, we will need two types of arguments; a `Word Argument` to get a word, in this case, the pseudo, and a `Number Argument` to get a number, in this case, the age.
To add an argument, click on the `Custom Command` entry, then on `Arguments`, and select `Add Word Argument`. Next, click on the last argument and add a child: `Add Number Argument`.

![Custom Command Arguments](https://docs.typewritermc.com/assets/optimized-img/custom-command-arguments.e8e529a.528.avif)

![Arguments Children](https://docs.typewritermc.com/assets/optimized-img/arguments-children.5d45883.528.avif)

**Number Argument**

Rename your arguments to make it easier for players to understand it when they will execute the command.

## Do something with your command {#do-something-with-your-command}

Then, if you want your command to perform an action, add a Trigger to the last argument. So, in the `Number Argument`, click on `Trigger` and choose your action entry. In this case, we will use a `Send Message` entry.
To retrieve what the player has entered in the arguments, we will use a `Interaction Context Text Variable` and add keys to it. Finally, we need to construct a message using the values retrieved from the arguments.

![Interaction Context Text Variable](https://docs.typewritermc.com/assets/optimized-img/context-text-variable.aa02770.528.avif)

## Result {#result}

### Sequence result {#sequence-result}

Now your pages should look something like this:

[sequence.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/07-advanced-interactions/assets/commands/sequence.json)

[manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/03-creating-stories/07-advanced-interactions/assets/commands/manifest.json)

**Variables**

Our documentation renderer doesn't currently support displaying dynamic variables, so you'll only see a simplified static message instead of the actual variable.

### In Game result {#in-game-result}

In game, the command should look like this:

<video controls preload="metadata" src="https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/custom-commands/result.webm"></video>
