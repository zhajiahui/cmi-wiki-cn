Plugins can listen for packets through PacketAdapters. A packet adapter is generally set up like this:

```java
ProtocolManager manager = ProtocolLibrary.getProtocolManager();
manager.addPacketListener(new PacketAdapter(plugin, ListenerPriority.NORMAL, PacketType.Play.Client.USE_ENTITY) {
    @Override
    public void onPacketReceiving(PacketEvent event) {
        Player player = event.getPlayer();
        PacketContainer packet = event.getPacket();
        int entityId = packet.getIntegers().read(0);
        System.out.println(player.getName() + " interacted with entity " + entityId);
    }
});
```

This is a rather trivial example that listens for incoming entity interaction packets and reads the target entity ID. There are a few things to unpack though:

## PacketType
PacketType is an enum-like class that contains every packet supported by ProtocolLib. PacketTypes are formatted as `PacketType.[Game Phase].[Direction].[Packet Name]`. The game phase is one of `Handshake`, `Play` (you'll probably mostly be working with play), `Status`, and `Login`. The direction is either `Client` (**incoming** packets) or `Server` (**outgoing** packets)

You can find a list of all packets in the [JavaDocs](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/PacketType.html). Note that `@Deprecated` packets may be supported on older Minecraft versions, but not the latest.

## PacketContainer
PacketContainer is how plugins can inspect and modify packets with ProtocolLib. It contains accessors for every type of field present in Minecraft packets. In this example, `packet.getIntegers()` returns a modifier for each integer field, and `read(0)` reads the target entity ID.

You can read more about PacketContainers on the wiki page: [PacketContainer](https://github.com/dmulloy2/ProtocolLib/wiki/PacketContainer)

## Signed chat
Do not cancel or modify inbound `CHAT` packets to moderate chat on modern Minecraft versions. The server validates the signed-message chain, and intercepting a message before that validation can leave the chain out of sync and cause later messages to be rejected. Use the Bukkit or Paper chat event API instead, where the server has already processed the signed packet.

## Odds and Ends
* Every packet can be cancelled with `event.setCancelled(true)` (that doesn't mean you _should_, but you _can_)
* In some game phases (non-play ones), `event.getPlayer()` will sometimes return a TemporaryPlayer when a Bukkit player is not available. They have a reduced set of available methods and can be checked for with [`event.isPlayerTemporary()`](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/events/PacketEvent.html#isPlayerTemporary--)

## That's all for now
Feel free to contribute pages and/or content, though! I'll be working on adding more as I have the time.
