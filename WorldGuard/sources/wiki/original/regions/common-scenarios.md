# Common Scenarios { #common-scenarios }

These are common scenarios that you may come across. Some of these scenarios have already been described in some other pages.

<a id="contents"></a>

- [General](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#general)



  - [How do I allow the usage of doors, levers, etc.?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-allow-the-usage-of-doors-levers-etc)

  - [How do I let people ride horses and Minecarts?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-let-people-ride-horses-and-minecarts)

  - [How do I prevent building in the wilderness?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-prevent-building-in-the-wilderness)

  - [How can I only deny exit for non-members?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-can-i-only-deny-exit-for-non-members)

  - [How can I let players exit one side of an exit=deny region?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-can-i-let-players-exit-one-side-of-an-exit-deny-region)

  - [How do I unprotect all enchantment tables?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-unprotect-all-enchantment-tables)

  - [How do I allow mining but prevent block placing?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-allow-mining-but-prevent-block-placing)

  - [How do I allow players to read lectern books, but not take them?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-allow-players-to-read-lectern-books-but-not-take-them)

  - [How do I allow breaking of only certain block types?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-allow-breaking-of-only-certain-block-types)

- [Plot Setups](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#plot-setups)



  - [How can I create a setup with plots?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-can-i-create-a-setup-with-plots)

  - [How do I prevent door, etc. usage in public areas of the mall?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#how-do-i-prevent-door-etc-usage-in-public-areas-of-the-mall)

- [Problems](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#problems)



  - [Why don’t pistons work?](https://worldguard.enginehub.org/en/latest/regions/common-scenarios/#why-don-t-pistons-work)

!!! tip "Tip"

    Be sure to also to check out the [Common Questions](https://worldguard.enginehub.org/en/latest/faq/) page for more solutions to common problems.

## General { #general }

### How do I allow the usage of doors, levers, etc.? { #how-do-i-allow-the-usage-of-doors-levers-etc }

If you want everyone to be able to use doors, levers, buttons, pressure plates, and so on, set the `use` flag:

```text
/rg flag REGION_NAME use allow
```

If you want to apply it to **all** regions, set it on the [Global Region](https://worldguard.enginehub.org/en/latest/regions/global-region/):

```text
/rg flag __global__ use allow
```

### How do I let people ride horses and Minecarts? { #how-do-i-let-people-ride-horses-and-minecarts }

If you want everyone to be able to use all vehicles, set the `ride` flag:

```text
/rg flag REGION_NAME ride allow
```

If you want to apply it to **all** regions, set it on the [Global Region](https://worldguard.enginehub.org/en/latest/regions/global-region/):

```text
/rg flag __global__ ride allow
```

!!! warning "Warning"

    This would allow players to take horses from others’ regions! Only use this if you want that, or have other protections against stealing horses.

### How do I prevent building in the wilderness? { #how-do-i-prevent-building-in-the-wilderness }

As described on the [Global Region](https://worldguard.enginehub.org/en/latest/regions/global-region/) page, you can set the `passthrough` flag to `deny`:

```text
/rg flag __global__ passthrough deny
```

Do **not** set the `build` flag.

### How can I only deny exit for non-members? { #how-can-i-only-deny-exit-for-non-members }

Since non-members is the default for `entry` and `exit` you don’t need to set region groups:

```text
/rg addmember example_region sk89q
/rg flag example_region exit deny
```

### How can I let players exit one side of an exit=deny region? { #how-can-i-let-players-exit-one-side-of-an-exit-deny-region }

Make two regions:

- One region would have `exit=deny`.

- The other region would border the side of the deny region, extending a bit outside, on the sides that you want to let players exit out of. This region would have `exit-overide=true`.

### How do I unprotect all enchantment tables? { #how-do-i-unprotect-all-enchantment-tables }

In the [Configuration](https://worldguard.enginehub.org/en/latest/config/), adjust the `interaction-whitelist` setting and add the enchantment table. Get the proper names that you can use from [Bukkit’s Material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html).

### How do I allow mining but prevent block placing? { #how-do-i-allow-mining-but-prevent-block-placing }

Set the `block-break` flag to `allow`:

```text
/rg flag mining_area block-break allow
```

### How do I allow players to read lectern books, but not take them? { #how-do-i-allow-players-to-read-lectern-books-but-not-take-them }

First, make sure you are on WorldGuard 7.0.1+. Earlier versions of WorldGuard released before 1.14 (and thus before lecterns) existed.

- Set the `use` flag to `allow`: `/rg flag <region> use allow`

### How do I allow breaking of only certain block types? { #how-do-i-allow-breaking-of-only-certain-block-types }

Sorry, this is not supported per region yet! However, this can either be done per world in whitelist mode as described in [Blacklist](https://worldguard.enginehub.org/en/latest/blacklist/) or using [Build Permissions](https://worldguard.enginehub.org/en/latest/build-perms/).

## Plot Setups { #plot-setups }

### How can I create a setup with plots? { #how-can-i-create-a-setup-with-plots }

If you want to create plots, you’d make use of region inheritence as described in [Priority and Inheritance](https://worldguard.enginehub.org/en/latest/regions/priorities/). There are two regions that you’d want to create, followed by the plot regions themselves.

You will have the following regions:

- The outer region (`mall`)

- An optional “template” region that all plot regions will inherit from (`shop_template`)

- The plots

Create the mall:

```text
/rg define mall
```

Create the shop template. However, we’ll use `-g` to make it a non-physical region since we’re not actually using it to protect any area.

```text
/rg define shop_template -g
```

Let’s make some plots:

```text
/rg define shop1
/rg define shop2
/rg define shop3
```

Now, you will need to set parents:

```text
/rg setparent shop_template mall
/rg setparent shop1 shop_template
/rg setparent shop2 shop_template
/rg setparent shop3 shop_template
```

!!! hint "Hint"

    An alternative is to set the mall region to a lower priority (`/rg setpriority mall -1`).

### How do I prevent door, etc. usage in public areas of the mall? { #how-do-i-prevent-door-etc-usage-in-public-areas-of-the-mall }

The goal here is:

- Set the `use` flag to `deny` in the mall: `/rg flag mall use deny`

- Since that prevents usage in the plots too, we need to change `use` within the plots only

- Since we created the template region, that makes it easy: `/rg flag shop_template use allow`

Due to the inheritance, the plots inherit the `use` flag from the template, which overrides the `use` flag on the mall.

## Problems { #problems }

### Why don’t pistons work? { #why-don-t-pistons-work }

Did you set the `build` flag? You **shouldn’t** do that. Be sure to remove it:

```text
/rg flag __global__ build
```

- If you are trying to prevent building, you don’t actually have to do anything! By default, when a region is made, it is protected.

- If you want to prevent building in the wilderness, you can set the `passthrough` flag to `deny`:



  ```text
  /rg flag __global__ passthrough deny
  ```

!!! warning "Warning"

    If you want a piston to push from one region into another, make sure both regions are in the same [nonplayer-protection-domain](https://worldguard.enginehub.org/en/latest/regions/flags/#flag-overrides).
