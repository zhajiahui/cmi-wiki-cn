# Trigger Sequence Cinematic

The `Trigger Sequence Cinematic` entry that runs a sequence of triggers. It is very powerful but also very dangerous.

**caution**

Be aware of which triggers are running. If you run a trigger that is viewable by everyone, it will be visible to everyone.
Also, **never trigger dialogues**, they should not be triggered from a cinematic.
If you want to trigger a dialogue after the cinematic, connect it to the [CinematicEntry](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/cinematic)

## How could this be used? {#how-could-this-be-used}

When you want to use any triggerable entry. Like giving an item to the player at a specific frame.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Segments

Required List Segment

The sequence of triggers to run

Segments are time frames in a cinematic. During a segment can take actions or display information.  

**info**

Segments cannot overlap. If you need overlapping segments, create a new entry.
