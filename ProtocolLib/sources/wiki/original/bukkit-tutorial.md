## A new API

ProtocolLib attempts to solve the network compatibility problem by providing a event API, much like Bukkit, that allow plugins to monitor, modify or cancel packets sent and received. But more importantly, the API also hides all the gritty, obfuscated classes with a simple index based read/write system. You no longer have to reference CraftBukkit!

### Using ProtocolLib

To use the library, first add ProtocolLib.jar to your Java build path. Then, add ProtocolLib as a dependency (or soft-dependency, if you can live without it) to your plugin.yml file: Code:

```
depend: [ProtocolLib]
```

In Eclipse, you can add the online JavaDoc documentation by right-clicking the JAR file in Project Explorer. Choose Properties, and from the left pane choose JavaDoc Location. Finally enter the following URL:

```
https://ci.dmulloy2.net/job/ProtocolLib/javadoc/
```

The first thing you need is a reference to ProtocolManager. Just add the following in onEnable() and you're good to go.

```
private ProtocolManager protocolManager;
  
@Override
public void onEnable() {
    protocolManager = ProtocolLibrary.getProtocolManager();
}
```

ProtocolLib uses an event API similar to Bukkit. The base listener class is PacketListener, but most people use PacketAdapter, which handles some of the overhead. In this tutorial, we will use PacketAdapter.

To listen for packets sent by the server to a client, add a server-side listener:

```
// Disable all sound effects
protocolManager.addPacketListener(
  new PacketAdapter(this, ListenerPriority.NORMAL, 
          PacketType.Play.Server.NAMED_SOUND_EFFECT) {
    @Override
    public void onPacketSending(PacketEvent event) {
        // Item packets (id: 0x29)
        if (event.getPacketType() == 
                PacketType.Play.Server.NAMED_SOUND_EFFECT) {
            event.setCancelled(true);
        }
    }
});
```

In the above code snippet, we created a PacketAdapter that will listen for sounds. The arguments are: your plugin instance, listener priority (optional), and a variable argument array of PacketTypes to listen for. In this case, we only listened for one packet, but theoretically you could listen for all of them.

It's also possible to read and modify the content of these packets. For instance, you can create a global censor by listening for Packet3Chat events:

```
// Censor
protocolManager.addPacketListener(new PacketAdapter(this,
        ListenerPriority.NORMAL, 
        PacketType.Play.Client.CHAT) {
    @Override
    public void onPacketReceiving(PacketEvent event) {
        if (event.getPacketType() == PacketType.Play.Client.CHAT) {
            PacketContainer packet = event.getPacket();
            String message = packet.getStrings().read(0);

            if (message.contains("shit")
                    || message.contains("damn")) {
                event.setCancelled(true);
                event.getPlayer().sendMessage("Bad manners!");
            }
        }
    }
});
```

### Sending packets

Normally, you might have to do something ugly like the following:

```
Packet60Explosion fakeExplosion = new Packet60Explosion();
 
fakeExplosion.a = player.getLocation().getX();
fakeExplosion.b = player.getLocation().getY();
fakeExplosion.c = player.getLocation().getZ();
fakeExplosion.d = 3.0F;
fakeExplosion.e = new ArrayList<Object>();
 
((CraftPlayer) player).getHandle().
    netServerHandler.sendPacket(fakeExplosion);
```

But with ProtocolLib, you can turn that into something more manageable. Notice that you don't have to create an ArrayList this version:

```
PacketContainer fakeExplosion = protocolManager.
        createPacket(PacketType.Play.Server.EXPLOSION);

fakeExplosion.getDoubles().
    write(0, player.getLocation().getX()).
    write(1, player.getLocation().getY()).
    write(2, player.getLocation().getZ());
fakeExplosion.getFloat().write(0, 3.0F);

try {
    protocolManager.sendServerPacket(player, fakeExplosion);
} catch (InvocationTargetException e) {
    throw new RuntimeException(
        "Cannot send packet " + fakeExplosion, e);
}
```

If you use [PacketWrapper](https://github.com/aadnk/PacketWrapper), you can get an even easier version. This is especially useful if you're trying to [send a entity spawn packet](http://dev.bukkit.org/server-mods/protocollib/forum/52983-creating-a-fake-player-not-in-the-playerlist/#p2):

```
WrapperPlayServerExplosion fakeExplosion = new WrapperPlayServerExplosion();
 
fakeExplosion.setX(player.getLocation().getX());
fakeExplosion.setY(player.getLocation().getY());
fakeExplosion.setZ(player.getLocation().getZ());
fakeExplosion.setRadius(3);

fakeExplosion.sendPacket(player);
```

Remember to add [AbstractPacket](https://github.com/aadnk/PacketWrapper/blob/master/PacketWrapper/src/main/java/com/comphenix/packetwrapper/AbstractPacket.java) **AND** [WrapperPlayServerExplosion](https://github.com/aadnk/PacketWrapper/blob/master/PacketWrapper/src/main/java/com/comphenix/packetwrapper/WrapperPlayServerExplosion.java) to your project.

### Cloning packets

Certain packets, such as [Entity Equipment](/linkout?remoteUrl=http%253a%252f%252fmc.kev009.com%252fProtocol%2523Entity_Equipment_.280x05.29), [Entity Metadata](/linkout?remoteUrl=http%253a%252f%252fmc.kev009.com%252fProtocol%2523Entity_Metadata_.280x28.29) or [Update Tile Entity](/linkout?remoteUrl=http%253a%252f%252fmc.kev009.com%252fProtocol%2523Update_Tile_Entity_.280x84.29), share the same instance when they are broadcasted to a group of players.

For instance, if you want to use armor color to designate hostile or friendly status, you might modify the armor color of every player individually before its sent to a player. But, for packets that are shared amongst players, this will only preserve the last written color, and thus every player will see what the last player written (or a random player) was supposed to see.

The solution is to clone each packet before writing to them ([full code](https://gist.github.com/aadnk/10336564)):

```
manager.addPacketListener(new PacketAdapter(this, 
        PacketType.Play.Server.ENTITY_EQUIPMENT) {
    @Override
    public void onPacketSending(PacketEvent event) {
        PacketContainer packet = event.getPacket();

        ItemStack stack = packet.getItemModifier().read(0);

        // Only modify leather armor
        if (stack != null && stack.getType().name().contains("LEATHER")) {

            // The problem turned out to be that certain Minecraft 
            // functions update every player with the same packet for 
            // an equipment, whereas other methods update the 
            // equipment with a different packet per player.

            // To fix this, we'll simply clone the packet before we
            // modify it
            packet = event.getPacket().deepClone();
            event.setPacket(packet);
            stack = packet.getItemModifier().read(0);

            // Color that depends on the player's name
            String recieverName = event.getPlayer().getName();
            int color = recieverName.hashCode() & 0xFFFFFF;

            // Update the color
            LeatherArmorMeta meta = (LeatherArmorMeta) stack.getItemMeta();
            meta.setColor(Color.fromBGR(color));
            stack.setItemMeta(meta);
        }
    }
});
```

### Raw packet data

You can also get a hold of the raw packet data, as seen in the network stream between the client and the server. Take a look at [this write up](http://forums.bukkit.org/threads/lib-1-6-2-protocollib-2-5-0-safely-and-easily-modify-sent-and-recieved-packets.101035/page-7#post-1760625) for more information. You can even customize how the packet will be written to the output stream.

These features require ProtocolLib 2.5.0.
