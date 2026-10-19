---
title: "盔甲 - Unable to fit - try a lower resolution resourcepack"
source_url: "https://wiki.itemsadder.com/faq/armors-issues/armor-unable-to-fit-try-a-lower-resolution-resourcepack"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---

# 盔甲 - Unable to fit - try a lower resolution resourcepack

此错误是因为自定义盔甲过多和/或其纹理过大（例如高清纹理）。

这是游戏的限制，目前我对此没有办法。所有通过着色器技巧创建自定义盔甲的插件都有同样的问题。

如果客户端和服务器均为 1.21.2 或更高版本，你可以使用[新方法](../../adding-content/items/armors.md)创建盔甲。新方法没有这个问题。

```
Caught error loading resourcepacks, removing all selected resourcepacks
java.util.concurrent.CompletionException: z: Stitching
    at java.base/java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:315)
    at java.base/java.util.concurrent.CompletableFuture.completeThrowable(CompletableFuture.java:320)
    at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:649)
    at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:510)
    at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1773)
    at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.exec(CompletableFuture.java:1760)
    at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:387)
    at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1312)
    at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1843)
    at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1800)
    at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:188)
Caused by: z: Stitching
    at heo.a(SpriteLoader.java:146)
    at heo.lambda$loadAndStitch$8(SpriteLoader.java:212)
    at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:646)
    ... 8 more
Caused by: hr: Unable to fit: minecraft:entity/equipment/humanoid_leggings/leather - size: 7936x128, atlas: 4096x8192
z, atlasMax: 8192x8192 - Maybe try a lower resolution resourcepack?
```
