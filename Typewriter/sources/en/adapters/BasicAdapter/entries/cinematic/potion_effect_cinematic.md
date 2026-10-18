# Potion Effect Cinematic

The `PotionEffectCinematicEntry` is used to apply different potion effects to the player during a cinematic.

## How could this be used? {#how-could-this-be-used}

This can be used to dynamically apply effects like blindness, slowness, etc., at different times
during a cinematic, enhancing the storytelling or gameplay experience.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Segments

Required List Segment

Segments are time frames in a cinematic. During a segment can take actions or display information.  

**info**

Segments cannot overlap. If you need overlapping segments, create a new entry.
