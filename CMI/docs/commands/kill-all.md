---
title: 清理实体
---

# 清理实体

`/cmi killall` 可以按指定条件清理当前已加载的实体。

- 默认保留有自定义名称的实体。
- 忽略船或矿车中的实体。
- 可以指定范围，只清理附近实体。

## 参数

| 参数 | 说明 |
| --- | --- |
| `-monsters` | 清理怪物类实体，例如僵尸、骷髅和凋灵。 |
| `-pets` | 包含可驯服的实体，例如马和狼。 |
| `-npc` | 包含带 NPC 元数据的实体，通常由 Citizens 等插件创建。 |
| `-animals` | 清理猪、牛等动物。 |
| `-ambient` | 清理蝙蝠等环境生物。 |
| `-named` | 包含所有有自定义名称的实体，不区分敌对或友好生物。目前无法指定名称。 |
| `[mobType]` 或 `-m:[mobType]` | 只清理指定类型的生物。 |
| `-f` | 合并 monsters、pets、npc、golems、animals、ambient 和 vehicles 这些类别。 |
| `-lightning` | 在被清理实体的位置生成闪电。 |
| `[range]` 或 `-r:[range]` | 指定附近的清理范围，单位为格。 |
| `-list` | 按对应分类列出实体。 |
| `-w:[world]` | 清理指定世界中的实体。 |
| `-s` | 不向玩家显示指令输出。 |

## 示例

- `/cmi killall`：清理所有未命名的怪物。
- `/cmi killall -list`：列出实体。
- `/cmi killall 60`：清理周围 60 格内的怪物。
- `/cmi killall -r:5`：清理周围 5 格内的怪物。
- `/cmi killall zombie`：清理所有僵尸。
- `/cmi killall zombie skeleton`：清理所有僵尸和骷髅。
- `/cmi killall -m:sheep`：清理所有未命名的绵羊。
- `/cmi killall -monsters -lightning`：清理所有怪物，并在它们的位置生成闪电。
- `/cmi killall -named`：清理所有有名称的生物，包括敌对和友好生物；不会清理未命名的怪物。
- `/cmi killall -monsters -named`：清理所有怪物，以及所有有名称的敌对和友好生物。
- `/cmi killall -w:world_nether`：清理 `world_nether` 世界中的所有怪物。
- `/cmi killall -f -named`：强制清理所有友好生物、怪物和已命名生物。

## 指令、权限与占位符

**指令：**

```text
> cmi checkcommand killall
 --------------------------------------------------
 /cmi killall (-monsters/-pets/-npc/-animals/-ambient/-named/-f/-lightning/-list/-m:[mobType]) (-r:range) (-s) (-w:[worldName])
> 

To kill a player, use /cmi kill instead
```

**权限：**

```text
> cmi checkperm killall
 --------------------------------------------------
 cmi.command.killall - Kill mobs around you
>
```

**占位符：**

```text
There are no placeholders for this feature
```

---

[查看原文](https://www.zrips.net/cmi/commands/kill-all/)
