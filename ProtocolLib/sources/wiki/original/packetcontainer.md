The primary interface between you and the packet is PacketContainer. It contains a set of StructureModifiers that allow you to modify the packet. See the [JavaDoc](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/events/AbstractStructure.html) for a list of supported modifiers. Modifiers are based on the NMS representation of a packet, NOT the wiki representation. They're _generally_ equivalent, but the wiki shows the serialized form. Your best bet for determining the NMS representation of a packet is to search for the decompiled source file in your BuildTools work directory.

## StructureModifier

JavaDoc: [StructureModifier.java](https://ci.dmulloy2.net/job/ProtocolLib/javadoc/com/comphenix/protocol/reflect/StructureModifier.html)  
  
StructureModifiers allow you to read from and write to a packet. Depending on how you feel about optionals, you can use `modifier.optionRead(index)` or `modifier.readSafely(index)` to read data from a packet. You can then write with `modifier.writeSafely(index, value)`