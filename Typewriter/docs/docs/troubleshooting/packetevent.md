---
title: PacketEvents 问题排查（PacketEvents Troubleshooting）
source: https://docs.typewritermc.com/docs/troubleshooting/packetevent
source_version: 0.8.0
---

# PacketEvents 问题排查（PacketEvents Troubleshooting）

如果你在启用Typewriter插件时遇到错误，例如与`io.github.retrooper.packetevents`相关的`java.lang.NoClassDefFoundError`，这可能是由于PacketEvents插件版本不兼容造成的。

## 错误消息 {#error-message}

你可能会看到的错误消息示例：

```bash
[12:41:54 ERROR]: Error occurred while enabling Typewriter v0.5.1 (Is it up to date?)
java.lang.NoClassDefFoundError: io/github/retrooper/packetevents/bstats/Metrics$CustomChart
        at me.gabber235.typewriter.entry.entity.EntityHandler.initialize(EntityHandler.kt:23) ~[typewriter (5).jar:?]
        at me.gabber235.typewriter.Typewriter.onEnableAsync(Typewriter.kt:121) ~[typewriter (5).jar:?]
```

## 问题原因 {#cause-of-the-issue}

出现此错误的原因是安装的PacketEvents版本与你使用的Typewriter版本不兼容。**Typewriterv0.5.1 需要PacketEvents版本 2.5.x。**使用较新版本的PacketEvents可能会因 API 的更改而导致兼容性问题。

### 处理步骤 {#steps-to-fix}

1. **从服务器的`plugins`文件夹中删除**当前的PacketEvents插件。
2. **通过此网址](https://modrinth.com/plugin/packetevents/version/QLgJReg5)下载**PacketEvents版本**2.5.0**[。
3. **将**下载的PacketEventsjar 放入服务器的`plugins`文件夹中。
4. **重新启动**你的服务器以应用更改。

## 验证结果 {#verifying-the-fix}

执行上述步骤后，Typewriter插件应该加载且不会出现错误。检查服务器日志以确保不再有任何与PacketEvents相关的`NoClassDefFoundError`错误。

---

原文：[PacketEvents Troubleshooting](https://docs.typewritermc.com/docs/troubleshooting/packetevent) · 文档版本：0.8.0
