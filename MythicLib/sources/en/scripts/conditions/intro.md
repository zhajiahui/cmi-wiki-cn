# Introduction {#introduction}

A script only executes its list of mechanics **when all of its conditions are met**. They are checked in-order, which means MythicLib will first evaluate the first condition, stop there if it's not met, then evaluate the second, stop if not met, etc... If all conditions are met, then mechanics are executed one after the other.

| Condition Type | Description |
| --- | --- |
| [Generic](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/generic) | Math formulas, boolean expressions, string checks... |
| [Location](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/location) | Location-based conditions |
| [Miscellaneous](https://docs.phoenixdevt.fr/mythiclib/scripts/conditions/misc) | Other |
