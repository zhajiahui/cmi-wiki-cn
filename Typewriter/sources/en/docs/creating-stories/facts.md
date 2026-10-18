# Facts

Facts are essentially variables. They store information that can be modified by other entries. All facts are numbers and are treated as such.

The [`Basic Extension`](https://docs.typewritermc.com/adapters/BasicAdapter) encompasses numerous facts available for use. However, it's important to note that [`extensions`](https://docs.typewritermc.com/adapters) have the capability to further augment the array of available facts.

## Why Use Facts? {#why-use-facts}

Facts play a crucial role in dynamic content creation and system behavior customization. Here are some reasons to consider using facts:

- **Dynamic Quests:** Track player progress in quests by using facts to store and modify completion status.
- **Customization:** Personalize player experiences by utilizing facts to adjust in-game parameters, such as difficulty levels or character attributes.
- **Interactive Storytelling:** Enhance narrative elements by employing facts to remember player choices and actions, shaping the evolving story.
- **Achievement Systems:** Implement achievement tracking by using facts to record specific milestones and accomplishments.

### Types of facts {#types-of-facts}

Facts have two types: readable and writable.

- **Readable Facts:** Used in the criteria of an entry. For example, checking if a player has a certain item in their inventory.
- **Writable Facts:** Used in modifiers to modify the fact's value. For instance, updating a player's quest progression.

**info**

Some facts are both readable and writable. For example, the [permanent fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/permanent_fact) can be used in both criteria and modifiers.
But some facts are only readable. For example, the [inventory item count fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact) can only be used in criteria.

## Groups {#groups}

In a fact you can select a group. There are 3 types of groups:

- **Global**: Sets a fact for all players.
- **World**: Sets a fact for all players in a specific world.
- **Player**: Sets a fact for a specific player.

## Fields {#fields}

In some entries, there are fields that influence the way facts are handled.

![Criteria and modifiers fields](https://docs.typewritermc.com/assets/optimized-img/criteria_and_modifier.7444206.432.avif)

### Criteria {#criteria}

Criteria is the condition for an entry, e.g., `if fact = 10 then...`. It controls whether an entry will occur.

![Criteria field](https://docs.typewritermc.com/assets/optimized-img/criteria.aedf976.428.avif)

When using criteria, follow these steps:

1. Select the fact to check.
2. Choose the operator.
3. Insert the value for the operator to check.

### Modifiers {#modifiers}

Modifiers, as the name suggests, modify a fact.

![Modifier field](https://docs.typewritermc.com/assets/optimized-img/modifier.914e01c.431.avif)

When using modifiers, follow these steps:

1. Select the fact to modify.
2. Select the operator. You can change the value directly (=) or add to it (+).
3. Insert the value for the operator to modify.

**warning**

Modifiers only run when the entry is executed.
If the entry has criteria and **one of the criteria** is `false`, then the entry won't be executed, and the fact won't be modified.

## Tutorial {#tutorial}

To get you started with facts, we will use a permanent fact to track progression in a quest.

1. Create a new page and select it as `static`. Give it the name `Playerprogress`
2. Click on the + icon and select `Add Permanent Fact`. Rename it to `Playerprogress` and give it a nice comment.

   ![Static page button](https://docs.typewritermc.com/assets/optimized-img/static-page.2b9bf54.1789.avif)
3. Select the player group.
4. On the sequence page, click on an action.
   - Set a **Criteria:** Check if `Playerprogress` == 0.
   - Set a **Modifier:** If criteria are met, update `Playerprogress` to 1.
5. Create additional actions to represent different quest stages, modifying `Playerprogress` accordingly.

## Examples {#examples}

There are many possibilities with the fact's system. Here are some examples:

**Gathering Items Quest**

**Objective:** A player talks to an NPC and needs to gather items.

**Fact Used:**

- **Readable Fact:** [Inventory Item Count](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact)

**Scenario:**

1. The player talks to the NPC.
2. Check the criteria using the Inventory Item Count Fact to verify if the player has the required items.

**Progression Tracking**

**Objective:** Track a player's progression through different quest stages.

**Fact Used:**

- **Writable Fact:** [Permanent Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/permanent_fact)

**Scenario:**

1. The player talks to an NPC (progression set to 1).
2. Completes a specific action (progression set to 2).
3. Finishes the quest (progression set to 3).

**Balance check**

**Objective:** See if a player has enough money to buy an item.

**Fact Used:**

- **Readable Fact:** [Balance Fact](https://docs.typewritermc.com/adapters/VaultAdapter/entries/fact/balance_fact)

**Scenario:**

1. The player talks to an NPC.
2. Check the criteria using the balance fact to see if the player has enough balance.
3. If the player has enough balance, they can buy the item.
4. If the player doesn't have enough balance, show a message to the player.

**tip**

To see all the available facts, check out the [Extensions section](https://docs.typewritermc.com/adapters).
