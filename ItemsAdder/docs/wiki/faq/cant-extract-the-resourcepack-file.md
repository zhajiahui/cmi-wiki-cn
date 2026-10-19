---
title: "无法解压资源包文件"
source_url: "https://wiki.itemsadder.com/faq/cant-extract-the-resourcepack-file"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 无法解压资源包文件

禁用保护选项。

```yaml
  zip:
    protect-file-from-unzip:
      enabled: false
      extreme: false
```

此选项用于防止 zip 文件被解压。\
禁用时请谨慎；如果不保护文件，任何人都可以解压。

## 读取压缩资源包

如果需要在不解压的情况下获取资源包内容，例如用于调试，可以使用 `/iazip --uncompressed --apply-to none`。此命令会在 ItemsAdder 文件夹中创建 `output_uncompressed` 新文件夹。你可以在其中访问所有文件并进行检查。
