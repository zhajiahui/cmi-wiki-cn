# Navigation { #navigation }

You may often find yourself in need of getting to places in order to do your work better. The following commands deal with that issue.

<a id="contents"></a>

- [The Navigation Wand](https://worldedit.enginehub.org/en/latest/usage/navigation/#the-navigation-wand)

- [Freeing yourself](https://worldedit.enginehub.org/en/latest/usage/navigation/#freeing-yourself)

- [Jumping to the block in sight](https://worldedit.enginehub.org/en/latest/usage/navigation/#jumping-to-the-block-in-sight)

- [Passing through walls](https://worldedit.enginehub.org/en/latest/usage/navigation/#passing-through-walls)

- [Ascending and descending](https://worldedit.enginehub.org/en/latest/usage/navigation/#ascending-and-descending)

- [Ascending to the ceiling](https://worldedit.enginehub.org/en/latest/usage/navigation/#ascending-to-the-ceiling)

- [Ascending up an arbitrary distance](https://worldedit.enginehub.org/en/latest/usage/navigation/#ascending-up-an-arbitrary-distance)

## The Navigation Wand { #the-navigation-wand }

WorldEdit gives you access to a navigation wand, a [tool](https://worldedit.enginehub.org/en/latest/usage/tools/tools/) that is by default bound to the compass (though you can [configure](https://worldedit.enginehub.org/en/latest/config/) this).

At any time, you can left click while holding a compass to jump to the block you are looking at (as with the jumpto command, described below). You can also right click with the compass to pass through walls (as with the thru command, described below).

## Freeing yourself { #freeing-yourself }

> ```text
> /unstuck
> /!
> ```

This will get you out of a block if you somehow got embedded inside. It moves you to the top-most free position, choosing to do nothing if you were not stuck to begin with. The short alias (`/!`) can often be useful if you aren’t in creative mode and find yourself suffocating after pasting or generating something on top of yourself.

## Jumping to the block in sight { #jumping-to-the-block-in-sight }

```text
/jumpto
```

This command sends you to the top of the block that you are looking at. If that block is a vertical wall, you will be placed on top of the cliff at the very edge.

## Passing through walls { #passing-through-walls }

```text
/thru
```

This command sends you through a wall in the direction you are looking. Just look into a wall and use the command. Make sure that you do not look downwards into a wall because it will attempt to go through the ground. This command limits the thickness of the wall to a reasonable amount.

## Ascending and descending { #ascending-and-descending }

```text
/ascend [levels]
/descend [levels]
```

These two commands allow you to pass through the ceiling above or floor below you. For example, if you were inside a home, you would move to the roof of the building if you used /ascend. You can also optionally provide a number of levels to ascend or descend. For example, if you were in a skyscraper on the bottom floor, and used `/ascend 2`, you’d be on the 3rd floor.

## Ascending to the ceiling { #ascending-to-the-ceiling }

```text
/ceil [clearance]
```

This command brings you up to the ceiling of the current room that you are in. If you provide no clearance parameter to use, you will be right up to the ceiling. If you do specify a clearance, the space above your head will be larger. A glass block is placed under your feet in order to support you. You must remove the block manually.

## Ascending up an arbitrary distance { #ascending-up-an-arbitrary-distance }

```text
/up <distance>
```

This will move you up a certain number of blocks. You cannot pass through walls with this command and a glass block will be placed at your feet to support you. The glass block has to be removed manually after you are done.
