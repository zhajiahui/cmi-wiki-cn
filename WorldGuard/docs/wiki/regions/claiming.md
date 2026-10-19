---
title: 认领区域
source_url: https://worldguard.enginehub.org/en/latest/regions/claiming/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 认领区域 { #claiming }

WorldGuard 提供基础的玩家认领系统。它创建的区域与 `/rg define` 类似，但玩家必须使用单独授权的特殊命令。选择区域的实际范围时仍需使用 WorldEdit 选区，不过只需授予 `worldedit.selection` 权限。

玩家可使用 `/rg claim` 认领当前选区：

```text
/rg claim region_name
```

执行命令的玩家会自动成为区域所有者。使用该命令需要 `worldguard.region.claim` 权限。

## 规则 { #rules }

- **区域数量上限：**除非拥有 `worldguard.region.unlimited`，否则玩家的区域数量不得超过[配置](../config.md)为其规定的上限。

- **区域体积上限：**除非拥有 `worldguard.region.unlimited`，否则认领区域的体积不得超过 `regions.max-claim-volume` 配置值。

- **防止覆盖：**认领的区域不能替换同名的现有区域。

- **防止重叠：**认领的区域不得与玩家并非所有者的其他区域重叠。

- **只能与自有区域重叠：**启用 `regions.claim-only-inside-existing-regions` 时，认领区域必须与玩家拥有的另一个区域重叠。注意，新认领区域*无需*完全包含在另一现有区域中，详见 [Issue #753](https://github.com/EngineHub/WorldGuard/issues/753)。

!!! note "注意"

    目前尚未完整支持多边形区域，详见 [Issue #1537](https://github.com/EngineHub/WorldGuard/issues/1537)。

## 其他命令 { #other-commands }

通过设置相应[权限](../permissions.md)，可以允许玩家使用其他命令，例如设置旗标和添加成员。
