When a mechanic/targeter/etc. tells you one of your attributes can be a Shape ***and it links to this page***, it means that its value can be any among the following ones:

1. [SPHERE](https://wiki.mythiccraft.io/mythicmobs/Enum/Shape#sphere)
2. [CUBE](https://wiki.mythiccraft.io/mythicmobs/Enum/Shape#cube)
3. [CYLINDER](https://wiki.mythiccraft.io/mythicmobs/Enum/Shape#cylinder)

And that the mechanic/targets/etc. in question can make use of the additional attribute specified in the SHAPE used when it is used.

# SPHERE {#sphere}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the sphere shape | 5.0 |
| livingonly | living, l | Whether to target only living entities | true |

# CUBE {#cube}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | Half the length of one of the cube's edges | 5.0 |
| livingonly | living, l | Whether to target only living entities | true |

# CYLINDER {#cylinder}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| radius | r | The radius of the cylinder | 5.0 |
| height | h | The height of the cylinder | 5.0 |
| yOffset | offsety, yo | The y offset | 0 |
