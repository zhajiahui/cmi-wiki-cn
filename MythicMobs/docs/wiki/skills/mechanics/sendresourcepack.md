---
title: Sendresourcepack
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/sendresourcepack
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Sendresourcepack {#sendresourcepack}

## 说明 {#description}

向目标玩家发送资源包。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| url | u, link | 要下载的资源包链接 | NONE |
| hash | h | 资源包的哈希值 | mythicmobs |

## 示例 {#examples}

> 本例中提供的哈希只是一个演示，请勿
> 在你的技能中使用它

```yaml
Skills:
  - sendresourcepack{url="https://yourresourcepackurlhere";hash="cf23df2207d99a74fbe169e3eba035e633b65d94"} @PIR{r=15} ~onSpawn
  - ...
```

## 别名 {#aliases}

- resourcepack
