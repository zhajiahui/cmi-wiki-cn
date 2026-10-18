# 🤔 FAQ {#🤔-faq}

More frequent bugs and issues are documented on **[this MythicLib wiki page](https://docs.phoenixdevt.fr/mythiclib/faq)**, please consider checking it as well.

## Is there an installation guide {#is-there-an-installation-guide}

An installation guide is available [here](https://docs.phoenixdevt.fr/mmoinventory/install).

## Is MySQL supported? {#is-mysql-supported}

Yes, you can enable MySQL in the main plugin config file. Look for the following lines:

```yml
mysql:
  enabled: false
  host: localhost
  port: 3306
  database: minecraft
  user: mmolover
  pass: ILoveAria
  ....
```

## How do I make it open when I press E? {#how-do-i-make-it-open-when-i-press-e}

You can do this using [MythicKeys](https://www.spigotmc.org/resources/mythickeysplugin-custom-keybinds-api.98893/) which requires a client mod. You cannot do this without a client mod as there are **NO** ways (in vanilla Spigot) of checking if a player has his crafting inventory open, as it is all client side. A client mod allows you to send the right packets for the server to detect when a player opens his inventory.

This used to be possible under Spigot 1.12 using advancement packets but these were removed in non legacy builds.

What you can do is use another plugin to make the 2x2 crafting grid perform the `/mmoinventory` command when clicked which can be a nice vanilla alternative. Some other alternative is using an item you'd place in some static slot of your inventory that opens the inventory when right clicked (there's an option to do that in the main config file).

## Does MMOInventory have auto-elytra equip? {#does-mmoinventory-have-auto-elytra-equip}

In recent dev builds, yes!

## Does MMOInventory auto use totems? {#does-mmoinventory-auto-use-totems}

No.

## MMOItems placed in their respective slots don't apply their stats. {#mmoitems-placed-in-their-respective-slots-don-t-apply-their-stats}

Make sure the corresponding item type from `MMOItems/item-types.yml` has its subtype/parent set to `ACCESSORY`, which is **mandatory** to have MMOItems register stats from items placed in the custom inventory GUI. If you try equipping a catalyst item in a catalyst slot, you'll succeed but won't get ANY stat because catalysts don't apply their stats when equipping in custom inventory slots! This is a limitation with how MMOItems is made.

Similarly items with non met level restrictions can be equipped but won't apply their stats (unless you are using the `milevel{}` slot restriction).

## Is there a backpack slot, or a mount slot? {#is-there-a-backpack-slot-or-a-mount-slot}

No.

## Is there a weapon slot? {#is-there-a-weapon-slot}

No, because this feature gets glitchy really fast with other plugins like MMOItems. It used to be a thing in old inventory plugins such as RPGInventory but we decided not to implement it.

## My GUI looks weird {#my-gui-looks-weird}

This issue is no longer relevant as of 1.21.8 as the *scale* parameter can no longer be used to cover up the vanilla inventory grid pattern. Please refer to [this wiki page](https://docs.phoenixdevt.fr/mmoinventory/features/custom-inventory-texture) for more details.

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgEAAAEHCAIAAAC4NQK2AAAL1klEQVR42u3dvXHcyBYGUPGVPJZyYADMgBa9NWSOswEoAFbBUQRrMYINYB2aayiDSYABMAet7FmDr5pbBNnEz8ygge8ci+8Ro72DHtSt+7ExuDgcDp8AiPS/pQsAYDF6AECuz+/9Yr/fL10bAKdlDgDIpQcA5HqdBYmAAHKYAwBy6QEAufQAgFx6AEAuPQAg1+c5L/7+/ft7v/rjjz+WfmtnUk5CzlsGNsMcAJBLDwDINSsLKumHPARgjcwBALn0AIBcs7KgISp7h4p+gjQkXKocM2rD0swKT1dPP2o73RkDMpkDAHLpAQC5Tp4FFWfIKGbmIaNeNWRP1LESrWn/MsCHzAEAufQAgFzny4LOachWn/ZVch4REHAU5gCAXHoAQK5Gs6DKrpshW2ICo5LKDWUA7zEHAOTSAwByHfk5Yke/d2laBDTtK4COXuGQeo4eWw25Hw3gmTkAIJceAJDr4nA4/Pd/7/f7pUtiinPGX8BmmAMAcukBALlkQQC5zAEAufQAgFx6AEAuPQAglx4AkEsPAMilBwDk0gMAck357ui7u7uly37bbrd7/uHh4WHpWlSoQhWqsIkKb25uKodNfH7A/f390m/wXWu51bn9c9h+he1r/xy2X2H7Vn0OZUEAuRp9pvwcXdeV6axMQ43ouu75h2bnx1Lniiq0ypPrXFGFVnlynfVRwBwAkEsPAMi1wSxovr///vu9X339+nXp6gCOxhwAkEsPAMglC3pRIqBK4DPkGGARlRS3zyX8zBwAkEsPAMglCxoX75RjhEIrNSouKKxyy6ZdjC7hZ+YAgFx6AECu3Cxo5vw489/hzGYuk1VuUH9Rpu0LCl9ccwBALj0AIFduFjSK28dW6liLIjdYlyGrU4mSohbXHACQSw8AyCULqnH7GGxV5YKNuoTNAQC59ACAXHFZ0Bl2+GROlKsz5H4iC8fmmQMAcukBALlSsqC//vrr+YcvX74sXQtLKhHQz58/hx8sFGKrzAEAufQAgFwpWdA///zz6v8x5sOqucnrKMwBALn0AIBcKVnQt2/fnn/4888/X/2qf6/QzPnRHArnNCQUGvXyIuFaNgcA5NIDAHKlZEFFJRSaeftYwti4OpUx//fff//w5eVVFncVpu0LCn9KoDkAIJceAJArLgsqhuwU6s99lW0G2xsSt2Tm14CzLqP2BYUzBwDk0gMAcuVmQcU5bx8DzmnUvqBM5gCAXHoAQC5Z0ItKKDTkfiJgjYZsItpwCGwOAMilBwDkkgW9oYRCQI4NBz4V5gCAXHoAQK4pWdBut1u67KEVdl23dC0fVNisFVVolRMqtMonYg4AyDXxb8L7/f5Tw515Fdo/h+1X2L72z2H7FbZv1efw4nA49N9M3d3d3dJlv60MZQ8PD0vXokIVqlCFTVR4c3NTOWziHHB/f7/0G3zXkDbWAucwQfur3H6F7Vv1OfT3AIBcG7xHrOu6Mp219if7khg2Oz+WOld0DtuvsE3/XeU2retz2Kau6+qjgDkAIJceAJBrg1kQp1a+YvcMD2nK/AoXZpr2qcv8sJkDAHLpAQC5ZEFvGDJIZo6Nr/RDof6pm3miRuVOQ/6dUYUd/e1wUjM/Lcf6sK2LOQAglx4AkEsW9KI/CT4+Pj7/cH19/eHBOfrJT+VsLLIvaEiGM6TmIW8n8APQmpkfv/Kq/gc7YXHNAQC59ACAXLKgiXPf1dXVnJdv1bGikh8/fsz5r59uLUYFR5zUkAjo9vZ2wr8TFQqZAwBy6QEAuXKzoDLllVSnomwQKspOofJDwtj43juduflnEae7r42ljLoGf/369ergnEv4v8wBALn0AIBccVlQZdyrBD6VY4rwifK9kzDqbJTtQL/99tv5aybK5eXl0iU0wRwAkEsPAMgVlwUN0Y+A+r+qhEJbVdkO1I9TZoZC05wzjktO/Jo17QMQvpTmAIBcegBArtws6FhhTj84enp6WvrNNWSRUIgoQ77wp+LoX3i+LuYAgFx6AECu3Cyosvmn8viwwO1Ax3LOUOh0G4QEWQ2qLPeoZdrGF2GNZQ4AyKUHAOSKy4JGpQSjvkGobAeSEtTZKcSJzMxwMj9+5gCAXHoAQK64LKjoj43lgWKjtgOJgCb7/Pn/H79zflM0CVyMw5kDAHLpAQC5crOgoh8KVW4fK2xlqStPBKsQATGHOwGPwhwAkEsPAMglC3ox5AYTu4De1E9+Gsl5jhUXRIUDq2OV5zAHAOTSAwByyYLeEDUJDnfOJ7afofhpL6dlVnkCcwBALj0AIJcsiNFWPTKvungGssrDmQMAcukBALmmZEG73W7psodW2HXd0rV8UGGzVnQO26+wWSuq0CqfiDkAINfEvwnv9/tPDXfmVXAOE7S/yu1X2L5Vn8OLw+HQfzN1d3d3S5f9tjKUPTw8LF2LClWoQhU2UeHNzU3lsIlzwP39/dJv8F1D2lgL2j+H7VfYvvbPYfsVtm/V59DfAwBybfAesa7rynTW2p/sS2LY7PxY6lxRhVZ5cp0rqtAqT66zPgqYAwBy6QEAufQAgFx6AEAuPQAg1wb3Bc035CFEvpx2XaY9WKrPuq+C54gNZw4AyKUHAOSSBb3oPyr98fHx+Yfr6+sPD6ZBR18m696yUavTPzhzcc0BALn0AIBcsqCJA+DV1dWclwPHMu0arERAURe1OQAglx4AkCs3CyrjXkl1KsoGoaLsFCo/RM2PsLjKFTfqNs/wUMgcAJBLDwDIFZcFVYa7SuBTOaaImh+3pJ8bWLiVKkt5e3v76leXl5fvHRy+3OYAgFx6AECuuCxoiH4E1P9VJRRiFYbsKglPCTagHwHxijkAIJceAJArNws6VpjTD46enp6WfnMAg5gDAHLpAQC5crOgyuafyuPDbAcCtsQcAJBLDwDIFZcFjfpWn1HfIFS2A7mxCBbRv7qHHBzOHACQSw8AyBWXBRX9sbE8UGzUdiARECyikuuOuhgzHx9WmAMAcukBALlys6CiPwBWbh8roqZFaNm0DCc8AirMAQC59ACAXLKgF0NuMLELCJo16h6xIjMCKswBALn0AIBcsqA3ZI6E2zYqHJj5KhbnEh7OHACQSw8AyCULYsumZQKSBHKYAwBy6QEAuaZkQbvdbumyh1bYdd3StXxQYbNWVKFVTqjQKp+IOQAg18S/Ce/3+08Nd+ZVaP8ctl9h+9o/h+1X2L5Vn8OLw+HQfzN1d3d3S5f9tjKUPTw8LF2LClWoQhU2UeHNzU3lsIlzwP39/dJv8F1D2lgL2j+H7VfYvvbPYfsVtm/V59DfAwBybfAesa7rynTW2p/sS2LY7PxY6lxRhVZ5cp0rqtAqT66zPgqYAwBy6QEAufQAgFx6AEAuPQAg1wb3Bc035OlRvl4YmjXtAXCZF7U5ACCXHgCQSxb0osyPZSR8fHx8/uH6+vrDg2lZJRzor+Cog2nHqKuyf3DmRW0OAMilBwDkkgVNHACvrq7mvJzzqKzOtN1flrtB0xalEgFFrbI5ACCXHgCQKzcLKuNeSXUqygahouwUKj9EzY+wuGMFfeGhkDkAIJceAJArLguqDHeVwKdyTBE1P0KDyqV3e3v76leXl5fvHRx+nZoDAHLpAQC54rKgIfoRUP9XlVAIaEQ/AuIVcwBALj0AIFduFnSsMKcfHD09PS395gAGMQcA5NIDAHLlZkGVzT+Vx4fZDrQKp7v9x52AbIw5ACCXHgCQKy4LGjXLj/oGobIdSDiwlHPmM0KhBvUXZcjB4cwBALn0AIBccVlQ0R8bywPFRm0HEgGty5DoRs6zCpVlGrVemY8PK8wBALn0AIBcuVlQ0R8AK7ePFVHT4upUtoWMWq9R+0xYyrQMJzwCKswBALn0AIBcsqAXQwZ/u4BadrpFsdyrMC27y4yACnMAQC49ACCXLOgNmSMhbIZLeDhzAEAuPQAglx4AkEsPAMilBwDkmrIvaLfbLV320Aq7rlu6lg8qbNaKKrTKCRVa5RMxBwDkmnh/wH6//9RwZ16F9s9h+xW2r/1z2H6F7Vv1Obw4HA79NwNAAlkQQK5/AYi8EwGge7SZAAAAAElFTkSuQmCC)

As explained on the main plugin resource page, the default MMOInventory resource pack uses custom textured diamond hoes to display gray filler items to fill in the Minecraft default inventory grid pattern. In order to hide that grid pattern you have to resize your items to approximately 110% but the required percentage can vary sometimes. Edit your resource pack and find the corresponding model which is (by default) located in `/assets/minecraft/models/item/slots/fill.json`.

Using the `scale` json section you can change it to something higher to hide that tiny 1-pixel-wide frame from the inventory grid pattern. Then tweak the `1.1` value so that the grid pattern fully hides. Be careful, if you set it too high the filler items will get past the item slot square.

```json
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "items/slots/fill"
  },
  "display": {
    "gui": {
      "rotation": [ 0, 0, 0 ],
      "translation": [ 0, 0, 0 ],
      "scale": [ 1.1, 1.1, 1.1 ]
    }
  }
}
```

## Is it compatible with Oraxen, ItemsAdder, Nexo? {#is-it-compatible-with-oraxen-itemsadder-nexo}

**MMOInventory is fully compatible with Oraxen, ItemsAdder and Nexo.** MMOInventory features a few additional built-in compatibility features [with Oraxen](https://docs.phoenixdevt.fr/mmoinventory/compatibility/oraxen).
