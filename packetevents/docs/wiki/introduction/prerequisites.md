---
title: "前置知识"
source_url: "https://docs.packetevents.com/introduction/prerequisites/"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "packetevents-docs a2a91c32fe7ff913413072ab0e51fe95a36f4028（2026-10-19 快照）"
---

<a id="prerequisites"></a>

# 前置知识

<a id="networking-and-tcpip"></a>

## 网络与 TCP/IP

前面提到，PacketEvents 用于在 Minecraft 中传输和处理数据包，因此掌握一些网络知识非常重要。Minecraft Java 版与基岩版不同，它使用 TCP/IP 协议，了解这一协议会有帮助。开发者使用 TCP/IP 时，可以依赖它提供的几项保证。首先，数据包的接收顺序与发送顺序相同。

!!! note "数据包顺序"

    假设服务器在 **10:00:01** 被要求向玩家 **Steve** 发送 **SetHealth** 数据包，随后在 **10:00:02** 被要求向 **Steve** 发送 **SpawnEntity**。那么 **Steve** 会先收到 **SetHealth**，再收到 **SpawnEntity**。如果服务器因故未能发送 **SetHealth**，它会延后发送 **SpawnEntity**，直到 **SetHealth** 发送成功。

另一项保证是丢失的数据包会被重新安排发送。TCP/IP 以可靠的数据包传输著称，UDP/IP 等其他协议并不提供这项保证。

!!! note "重新发送数据包"

    假设服务器被要求向玩家 **jeb_** 发送 **SetHealth** 数据包。如果服务器因任何原因未能将 **SetHealth** 发送给 **jeb_**，它就会再次尝试。当然，前提是服务器始终没有关闭或重启。

<a id="minecraft-protocol"></a>

## Minecraft 协议

你需要了解一些 [Minecraft 协议](https://minecraft.wiki/w/Java_Edition_protocol/Packets)知识。PacketEvents 只是实现协议，并不会完整解释协议的全部内容。几乎每次 Minecraft 更新都会修改协议，为持续变化的协议编写文档相当困难。如果希望软件在 Minecraft 更新后仍能运行，需要更新 PacketEvents，也可能需要跟进 Minecraft 协议的变化。社区维护了一份较为准确的[协议 Wiki](https://minecraft.wiki/w/Java_Edition_protocol/Packets)。

<a id="threading-concurrency"></a>

## 线程与并发

线程与并发经验也很重要。线程让开发者可以并行执行任务。可以用下面的例子来理解：

!!! note "并发示例"

    顾客点了一份餐，厨师希望尽量缩短等待时间。厨房里有三名工作人员：**Steve** 准备米饭，**Alex** 烹饪鸡肉，**Retrooper** 煮咖啡。如果三人并发工作，顾客只需等最慢的任务完成。如果依次工作，顾客就得等三个任务逐一完成，耗时会长得多。

并发在厨房很重要，在软件开发中更重要。Minecraft 也在一定程度上使用并发。网络通信处理由一个或多个工作线程负责，NPC 行为、世界生成等逻辑则由所谓的“主线程”处理。面对多线程系统，设计软件时要谨慎。多线程有性能方面的优势，但也会带来许多问题。例如，两个线程同时试图修改或访问同一份信息，就可能需要专门处理。因此，建议在使用这个库之前，先熟悉 Java 中的并发与线程。
