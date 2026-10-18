# Displaying Quests

**Before starting**

It's best to first read [Questing](https://docs.typewritermc.com/docs/creating-stories/questing) for the theory and [Talk Objective](https://docs.typewritermc.com/docs/creating-stories/questing/talk-objective) for the practical!

In this tutorial, you will learn how to display quest information to players using Typewriter's quest tracking system and placeholders.

## Understanding Quest Tracking {#understanding-quest-tracking}

Typewriter uses **facts** to track quest progress behind the scenes. These facts determine the state of your quests, but to actually **display** quest information to players, you need to track a specific quest.

**The Big Picture**

Think of quest tracking as a spotlight. While many quests might be active, tracking puts one quest in the spotlight for the player to focus on.

### How Tracking Works {#how-tracking-works}

When a quest is tracked, it becomes the "highlighted" quest that players see in their quest displays. This tracked quest becomes the focus for all display systems like scoreboards, sidebars, and custom UIs, keeping players focused on their current objective.

**One Quest at a Time**

While many quests can be **active** simultaneously, only **one quest can be tracked at a time**. This keeps the player focused and prevents UI clutter.

## Setting Up Quest Tracking {#setting-up-quest-tracking}

### Automatic Tracking {#automatic-tracking}

Typewriter automatically tracks quests in these situations:

- When a quest becomes active
- When an objective becomes active and has a higher priority than the currently tracked objectives

This means in most cases, you won't need to manually manage quest tracking. Typewriter handles it intelligently!

### Manual Tracking {#manual-tracking}

Sometimes you want full control over which quest is tracked.

You can manually track a quest using the command:

```text
/tw quest track <quest_id>
```

Or by using the **Track Quest Action** entry in your quest flow.

Add Track Quest

Start tracking a quest for a player

+

## Displaying Quest Information with Placeholders {#displaying-quest-information-with-placeholders}

Now that you understand tracking, let's look at how to actually display quest information to players. Typewriter provides several placeholders that dynamically show information about the currently tracked quest.

### Available Placeholders {#available-placeholders}

| Placeholder | Description | Example Output |
| --- | --- | --- |
| `%typewriter_tracked_quest%` | The display name of the tracked quest | `Kill Zombie Quest` |
| `%typewriter_tracked_objectives%` | A comma-separated list of the quest's active objectives | `Kill 2 Zombies, Return to Oliver` |
| `%typewriter_tracked_objectives_locations%` | The locations of the tracked locatable objectives | `X: 100, Y: 64, Z: -200` |

## Sidebar Display {#sidebar-display}

If Typewriter is managing your sidebar, you can use the [Objective Lines Entry](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/objective_lines) to display the objectives of the tracked quest.

A possible setup for the sidebar could be:

**tip**

Notice how the objectives lines doesn't use the placeholder

[quest_display_manifest.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/display/quest_display_manifest.json)

## Quest Status Changes {#quest-status-changes}

You can also display visual feedback when quests become active or are completed. This creates satisfying feedback for players and helps them understand their progress.

Common approaches include:

- **Title announcements** when a quest starts or completes
- **Particle effects** to celebrate quest completion
- **Sound effects** for important quest milestones
- **Chat messages** for quest updates

An example setup for this could be:

[quest_display_sequence.json](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/assets/questing/display/quest_display_sequence.json)

**Keep It Balanced**

While visual feedback is great, avoid overwhelming players with too many effects. A simple title or sound can be more impactful than elaborate animations.
