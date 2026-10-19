# Set Projectile Direction

## Description {#description}

Sets the calling projectile's movement direction to the given target

## Attributes {#attributes}

## Attributes {#attributes-2}

| Attribute | Aliases | Description | Default |
| --- | --- | --- | --- |
| magnitude | m | The magnitude of the change. A value of 1 will make the projectile change direction perfectly. Lower values will interpolate the changed direction position between 0 and 100% | 1 |

## Supported Targeters {#supported-targeters}

This mechanic accepts both location targeters and entity targeters. When given an entity targeter, the projectile is aimed at that entity's current location.

## Examples {#examples}

Once called by a projectile, this mechanic will change the projectile's direction based on its current direction

```yaml
  Skills:
  - setprojectiledirection @ProjectileForward{f=10;rot=45}
```

##  {#section}

Using an entity targeter aims the projectile at the nearest player within 10 blocks

```yaml
  Skills:
  - setprojectiledirection @NearestPlayer{r=10}
```
