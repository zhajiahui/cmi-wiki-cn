---
title: "CompletionException: z: Stitching"
source_url: "https://wiki.itemsadder.com/faq/completionexception-z-stitching"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# CompletionException: z: Stitching

```
minecraft:textures/atlas/blocks.png: dropping miplevel from 4 to 0, because of minimum power of two: 1
Caught error loading resourcepacks, removing all selected resourcepacks
java.util.concurrent.CompletionException: v: Stitching
    at java.base/java.util.concurrent.CompletableFuture.encodeThrowable(CompletableFuture.java:315)
    at java.base/java.util.concurrent.CompletableFuture.completeThrowable(CompletableFuture.java:320)
    at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:649)
    at java.base/java.util.concurrent.CompletableFuture.postComplete(CompletableFuture.java:510)
    at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1773)
    at bbf.b(SourceFile:51)
    at java.base/java.util.concurrent.ForkJoinTask$RunnableExecuteAction.exec(ForkJoinTask.java:1423)
    at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:387)
    at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1312)
    at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1843)
    at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1808)
    at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:188)
Caused by: v: Stitching
    at ill.a(SourceFile:90)
    at ill.a(SourceFile:114)
    at java.base/java.util.concurrent.CompletableFuture$UniApply.tryFire(CompletableFuture.java:646)
    ... 9 more
Caused by: iln: Unable to fit: ia:43904 - size: 128x128 - Maybe try a lower resolution resourcepack?
    at ilm.c(SourceFile:55)
    at ill.a(SourceFile:84)
    ... 11 more
```

此错误（及类似错误）是由于资源包中的纹理过多所致。使用大量高清纹理时更容易出现。

此限制取决于 GPU（显卡），例如 Intel 集成显卡就存在这个问题。

达到游戏和 GPU 的这一限制后，无论使用哪种内容管理工具，还是手动创建资源包，都会遇到相同问题。

## 如何修复？

1. 限制高清纹理的使用
2. 避免使用重复的 PNG 文件
3. 确保 HDMI 线连接的是独立显卡的接口，而非集成显卡的接口
