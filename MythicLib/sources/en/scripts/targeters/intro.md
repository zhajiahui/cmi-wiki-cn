# Introduction {#introduction}

Some mechanics require parameters like entities or positions: for instance, if you'd like to spawn a particle at a given position, you need to specify that exact position, which is done using **targeters**. If you'd like to deal X damage to an entity you must be able to tell ML what entity to damage.

There are targeters for both **entities** and **positions/locations**. Targeters can return multiple entities or positions at the same time, in which case the same script/mechanic will be executed multiple times, once for every entity/position.

| Targeter Type | Description |
| --- | --- |
| [Entity](https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/entity) | Entity targeters |
| [Location](https://docs.phoenixdevt.fr/mythiclib/scripts/targeters/location) | Location/position targeters |
