# Particle Cinematic

The `Particle Cinematic` entry is used to spawn particles for a cinematic.

## How could this be used? {#how-could-this-be-used}

This can be used to add dramatic effects to a cinematic.
Like, blowing up a building and spawning a bunch of particles.
Or, adding focus to a certain area by spawning particles around it.

## Fields {#fields}

## Criteria

Inherited List

A list of facts that must be met by the player before this entry can be triggered.

## Location

Required

The location to spawn the particles at.

## Particle

Required

The particle to spawn.

## Count

Required

The amount of particles to spawn.

## Offset X

Required

The offset from the location on the X axis.

## Offset Y

Required

The offset from the location on the Y axis.

## Offset Z

Required

The offset from the location on the Z axis.

## Speed

Required

The speed of the particles. For some particles, this is the "extra" data value to control particle behavior.

## Segments

Required List Segment

Segments are time frames in a cinematic. During a segment can take actions or display information.  

**info**

Segments cannot overlap. If you need overlapping segments, create a new entry.
