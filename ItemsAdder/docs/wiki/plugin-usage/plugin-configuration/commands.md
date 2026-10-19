---
title: "命令"
source_url: "https://wiki.itemsadder.com/plugin-usage/plugin-configuration/commands"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 命令

| 命令 | 权限 | 用法 | 说明 |
|:------------------------|:----------------------------------------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------|
| [e](commands/iaimage.md) | `ia.user.image.gui` | `/iaimage` | 显示字体图片（表情符号、HUD 等）列表。也可用于发送带表情符号自动补全的消息。 |
| ia | `ia.user.ia` | `/ia` | 打开物品列表界面 |
| ia | `ia.user.ia.categories` | `/ia <category>` | 打开物品类别界面 |
| ia | `ia.user.ia.categories.others` | `/ia <category> [player]` | 为其他用户打开物品类别界面 |
| iablock | `ia.admin.iablock` | `/iablock` | 显示你正在看的方块的信息 |
| iacleancache | `ia.admin.iacleancache` | `/iacleancache` | 从缓存中清除未使用的 ID，以供今后添加的方块/物品使用。 |
| [iaconfig](commands/iaconfig.md) | `ia.admin.iaconfig` | `/iaconfig` | 对插件配置执行操作的主命令。<br>更多信息请参阅[此处](commands/iaconfig.md)。 |
| iacustommodeldata | `ia.admin.custommodeldata` | `/iacustommodeldata` | 显示自定义物品的 CustomModelData |
| iadrop | `ia.admin.iadrop` | `/iadrop <item> [amount]` | 在指定坐标或玩家位置掉落自定义物品 |
| iadurability | `ia.admin.iadurability` | `/iadurability` | 修改当前物品（原版或自定义）的耐久度 |
| iaemote | `ia.user.iaemote`<br>`ia.user.iaemote.others` | `/iaemote <emote> [player]` | 播放自定义玩家动画。 |
| iaentity | `ia.admin.iaentity` | `/iaentity` | 管理自定义实体的主命令。 |
| iaget | `ia.admin.iaget` | `/iaget <item> [amount]` | 通过带命名空间的 ID 或 ID 获取自定义物品 |
| iagive | `ia.admin.iagive` | `/iagive <item> [amount] [silent]` | 将自定义物品给予玩家 |
| iahitbox | `ia.admin.iahitbox` | `/iahitbox` | 显示已放置家具的碰撞箱。 |
| iahud | `ia.admin.iahud` | `/iahud [name]` | 通过带命名空间的 ID 手动强制显示/隐藏 HUD |
| iainfo | `ia.admin.iainfo` | `/iainfo` | 显示插件信息 |
| iakill | `ia.admin.iakill` | `/iakill` | 杀死自定义生物 |
| ialiquid | `ia.admin.ialiquid` | `/ialiquid [x] [y] [z]` | 显示你正在看的液体的信息 |
| iaplayerstat | `ia.admin.iaplayerstat` | `/iaplayerstat <read\|write\|increment\|decrement> <player> <attribute> [value] [silent]` | 使用该命令 |
| iaplayerstat | `ia.admin.iaplayerstat.read` | `/iaplayerstat <read> <player> <attribute>` | 读取自定义玩家属性的数值 |
| iaplayerstat | `ia.admin.iaplayerstat.write` | `/iaplayerstat decrement <player> <attribute> <amount> [silent]` | 减少自定义玩家属性的数值（并更新 HUD） |
| iaplayerstat | `ia.admin.iaplayerstat.write` | `/iaplayerstat increment <player> <attribute> <amount> [silent]` | 增加自定义玩家属性的数值（并更新 HUD） |
| iaplayerstat | `ia.admin.iaplayerstat.write` | `/iaplayerstat write <player> <attribute> <value> [silent]` | 设置自定义玩家属性的数值（并更新 HUD） |
| iaplaysound | `ia.admin.iaplaysound` | `/iaplaysound <sound> <player>` | 播放 ItemsAdder 声音。<br>原版 `/playsound` 在控制台中存在漏洞，因此该命令适合在控制台中使用。 |
| iaplaytotemanimation | `ia.admin.iatotemanimation` | `/iaplaytotemanimation <totem> <player>` | 显示不死图腾动画 |
| iarecipe | `ia.user.iarecipe` | `/iarecipe [item]` | 显示物品配方界面 |
| iareload | `ia.admin.iareload` | `/iareload` | 重载配置文件 |
| iaremove | `ia.admin.iaremove` | `/iaremove <item> [amount] [silent]` | 从玩家背包中移除自定义物品 |
| [iarename](commands/iarename.md) | `ia.admin.iarename` | `/iarename <name>` | 重命名当前物品（原版或自定义）。支持表情符号（font_images）和 ItemsAdder 文本效果。 |
| iarepair | `ia.admin.iarepair` | `/iarepair` | 修复当前物品（原版或自定义） |
| iasha1 | `ia.user.iasha1` | `/iasha1` | 计算当前资源包的 sha1。 |
| iaspawntree | `ia.admin.iaspawntree` | `/iaspawntree <tree>` | 生成自定义树木 |
| iasummon | `ia.admin.iasummon` | `/iasummon [amount]` | 召唤自定义生物 |
| iatag | `ia.admin.iatag` | `/iatag` | 显示自定义物品的调试信息 |
| iatexture | `ia.user.iatexture` | `/iatexture` | 强制客户端重新加载资源包 |
| iatexture | `ia.user.iatexture.all` | `/iatexture [all\|player]` | 强制客户端重新加载资源包（单个玩家或所有人） |
| iazip | `ia.admin.iazip` | `/iazip` | 执行 /iareload 并生成资源包文件 |
| iatrademachine | `ia.admin.iatrademachine` | `/iatrademachine <player> <block/furniture>` | 为玩家打开交易机器界面。需要 [ItemsAdderAdditions](https://itemsadderadditions.com/en/docs/commands/iatrademachine) |