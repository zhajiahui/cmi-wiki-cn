# Mythic Skill Cinematic

The `Mythic Skill Cinematic` cinematic entry triggers a skill during a cinematic.

**caution**

A skill itself needs to define the group to be self using `group=self`

### Example: {#example}

```text
- effect:particlesphere{particle=flame;amount=200;radius=2;group=self} @self
```

## How could this be used? {#how-could-this-be-used}

This can be used to animate fancy particle effects during a cinematic.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Segments

Required List Segment

Segments are time frames in a cinematic. During a segment can take actions or display information.  

**info**

Segments cannot overlap. If you need overlapping segments, create a new entry.
