# Audience Entries

Audience entries are a specific type of [Manifest Entry](https://docs.typewritermc.com/docs/concepts/Manifest) that is used to conditionally display content to a group of players.
Players can be in the audience of an entry.
In other words, the content of an audience entry will be displayed to the players in its audience.

There are two types of Audience entries:

### Audience Display Entry {#audience-display-entry}

The Audience Display is meant to display content to a group of players.
It can be things like: applying a potion effect, or showing a boss bar.

### Audience Filter Entry {#audience-filter-entry}

Audience Filter entries have a list of children that can include both Audience entries and Audience Filter entries.
They are used as a way to filter the audience of an Audience Display Entry.

Audience Filters can both:

#### Filter Players {#filter-players}

Filter the audience of itself and its children. Like the `CriteriaAudience`, where players are allowed to be in the audience if they meet the criteria.

#### Display Content {#display-content}

Display content just like a normal Audience Display Entry, but use the children for the content on what to display. Like the `Sidebar` does with `Lines` entries.

# How does filtering work?

When a player joins the server, they are added to all of the root audience entries.
A root audience entry is an entry that has no parents.

## Root Entries {#root-entries}

[Interactive Visualization](https://docs.typewritermc.com/docs/concepts/Audience#root-entries)

[audience_entries.riv](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/04-concepts/04-Audience/assets/audience_entries.riv)

As seen above, any entry that has no parents is a root entry.
The filters can still allow or deny players from being in their own audience.
However, if nothing is linked, they don't influence the audience of other entries.

## Chaining {#chaining}

We can chain filter together to create a more complex filter.
Now the player is in the `Display` only if both conditions are met.

[Interactive Visualization](https://docs.typewritermc.com/docs/concepts/Audience#chaining)

[audience_entries.riv](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/04-concepts/04-Audience/assets/audience_entries.riv)

Try turning on and off some conditions and see what happens.

## Multiple Parents {#multiple-parents}

When an entry has multiple parents, the player is in the audience of the entry if any of the parents allow the player to be in the audience.

[Interactive Visualization](https://docs.typewritermc.com/docs/concepts/Audience#multiple-parents)

[audience_entries.riv](https://raw.githubusercontent.com/gabber235/Typewriter/9b0a087150c594120d6b89b158f3402bb9d85142/documentation/versioned_docs/version-0.8.0/docs/04-concepts/04-Audience/assets/audience_entries.riv)

Try turning on and off some conditions and see what happens.
