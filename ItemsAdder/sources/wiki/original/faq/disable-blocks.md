
# Disable Blocks

## Completely disable blocks

Requires ItemsAdder 4.0.13+

If you do not use custom blocks you can optimize the plugin by disabling them.

```yaml
blocks:
  custom:
    note: false
    mushroom: false
    chorus: false
    wire: false
    fire: false
  worlds: []
```

Also delete the `itemsadder` folder from each of your worlds (<mark style="color:orange;">make a backup</mark> before doing that, just in case).
