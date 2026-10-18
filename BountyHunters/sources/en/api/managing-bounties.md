# 📜 Bounties {#📜-bounties}

You may use the `BountyManager` class to register/unregister bounties or to simply check existing bounties. You can access the class instance using the following code snippet:

```java
BountyManager manager = BountyHunters.getInstance().getBountyManager();
```

## Creating & registering a bounty {#creating-registering-a-bounty}

To create a bounty, you have to use the `Bounty` constructor.

```java
Bounty bounty = new Bounty(creator, target, reward);
```

- creator - OfflinePlayer
- target - OfflinePlayer
- reward - Double

To register the bounty, use `bountyManager.registerBounty(bounty)`, which calls the `BountyCreateEvent` event. To unregister a bounty, you need to use `bountyManager.unregisterBounty(bounty)`. The `Bounty` class no longer has any register or unregister methods to reduce confusion and potential data glitches.

These methods both reset the bounty hunters. That means players hunting the bounty target will stop their hunt.

## Getting the list of active bounties {#getting-the-list-of-active-bounties}

Use `bountyManager.getBounties()` to get a collection of all active bounties, sorted in order of creation.

## Getting a bounty {#getting-a-bounty}

You can use `bountyManager.getBounty(OfflinePlayer)` to get the bounty on a player.

You will first have to check if there is any bounty on the player using `bountyManager.hasBounty(OfflinePlayer)` as the `getBounty(OfflinePlayer)` method will throw an NPE error if the player does not have any bounty on them.
