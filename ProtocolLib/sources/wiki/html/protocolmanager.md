Now that you have ProtocolLib added to your project, it's time to start actually working with it. The ProtocolManager is your primary entry point to ProtocolLib. It can be accessed like this:

```java
import com.comphenix.protocol.ProtocolManager;
import com.comphenix.protocol.ProtocolLibrary;

@Override
public void onEnable() {
    ProtocolManager manager = ProtocolLibrary.getProtocolManager();
    manager.addPacketListener(...);
}
```

***

The main methods you will be working with in the ProtocolManager are:
* `addPacketListener(PacketListener)`
  * Tells ProtocolLib to listen for a given set of packets. See [that wiki page](https://github.com/dmulloy2/ProtocolLib/wiki/Packet-listeners-and-adapters) for more info.
* `createPacket(PacketType)`
  * Creates a packet of a given type, that you can then...
* `sendServerPacket(Player, PacketContainer)`
  * Send a packet to a player

***

More advanced methods can be found in the JavaDocs:
* [ProtocolManager JavaDoc](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/ProtocolManager.html)
* [PacketStream JavaDoc](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/PacketStream.html) (PacketStream is the [superclass](https://www.geeksforgeeks.org/inheritance-in-java/) of ProtocolManager) 

### [Next Page](https://github.com/dmulloy2/ProtocolLib/wiki/Packet-listeners-and-adapters)