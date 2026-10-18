---
title: 附魔插件
source: https://docs.phoenixdevt.fr/mmoitems/compatibility/enchant-plugins
source_snapshot: '2026-10-19'
---

# 附魔插件 {#🔮-enchant-plugins}

MMOItems部分具有对 [EcoEnchants](https://www.spigotmc.org/resources/ecoenchants-%E2%AD%95-250-enchantments-%E2%9C%85-create-custom-enchants-%E2%9C%A8-essentials-cmi-support.79573)、 [MythicEnchants](https://mythiccraft.io/index.php?resources/mythicenchantments-early-access.397)和 [AdvancedEnchants](https://www.spigotmc.org/resources/43058)] 的本机兼容性。大多数现代附魔插件都具有合理的附魔实现（也称为使用Bukkit附魔注册表），应该可以与MMOItems一起正常工作。

## 实现与你的自定义附魔插件的兼容性 {#implementing-compatibility-with-your-custom-enchant-plugin}

如果你想与MMOItems兼容，你的插件必须使用默认的Bukkit附魔注册表。创建并注册`EnchantPlugin`的实例，并使用以下代码将其注册到MMOItems中（**在**MMOItems启用之前运行此代码）：

```java
MMOItems.plugin.registerEnchantPlugin(...);
```

这是你必须实现的接口：

```java
/**
 * There are three types of enchant plugins.
 * - enchants saved using the Bukkit Enchantment interface (EcoEnchants, MythicEnchants)
 * - enchants saved in the NBT (AdvancedEnchants)
 * - enchants saved in lore only (CrazyEnchants)
 * <p>
 * Interface used to support plugins which use the Bukkit Enchantment
 * interface to register their enchantments. This makes enchant storage
 * so much easier for MMOItems.
 *
 * @param <T> The plugin class implementing Enchantment
 */
public interface EnchantPlugin<T extends Enchantment> {

    /**
     * @param enchant Enchant being checked
     * @return If this enchant plugin handles a given enchant
     */
    boolean isCustomEnchant(Enchantment enchant);

    /**
     * Called when an item is built. This should be used to add the enchantment
     * lines to the item lore or add any item tag required by the enchantment.
     *
     * @param builder Item being built
     * @param enchant Enchantment being applied
     * @param level   Enchant level
     */
    void handleEnchant(ItemStackBuilder builder, T enchant, int level);

    NamespacedKey getNamespacedKey(String key);
}
```

以下是 MythicEnchants 插件的实现示例。`MythicEnchant` 类继承 Bukkit 的 `Enchantment` 类。`getNamespacedKey(String)` 应返回以插件名为命名空间的键。每次生成或重新生成物品时，都会运行 `handleEnchant(...)`，在物品描述中添加一行文字，表示已应用该附魔。可以通过 `ItemStackBuilder` 类访问 `LoreBuilder` 类，后者提供修改物品描述所需的方法。`LoreBuilder#insert(int, String)` 可以将任意字符串插入第 1 个位置。

```java
public class MythicEnchantsSupport implements EnchantPlugin<MythicEnchant> {

    @Override
    public boolean isCustomEnchant(Enchantment enchant) {
        return enchant instanceof MythicEnchant;
    }

    @Override
    public NamespacedKey getNamespacedKey(String key) {
        return new NamespacedKey(MythicEnchants.inst(), key);
    }

    public void handleEnchant(ItemStackBuilder builder, MythicEnchant enchant, int level) {
        Validate.isTrue(level > 0, "Level must be strictly positive");

        // Type cannot be changed. Must make sure that item is an enchanted book

        if (!builder.getMeta().hasItemFlag(ItemFlag.HIDE_ENCHANTS))
            builder.getLore().insert(0, LoreParser.formatEnchantment(enchant, level));
    }
}
```

像 EcoEnchants 这样的附魔插件不需要你注册`EnchantPlugin`实现，因为描述显示是使用数据包处理的，这是另一种可能性。

## 如果你的附魔插件不使用Bukkit附魔注册表 {#if-your-enchant-plugin-doesn-t-use-the-bukkit-enchant-registry}

> **警告**
>
> 此部分将在 MI7 中调整。

这有点困难，因为你需要注册一个新的物品属性，它将识别你用来保存附魔数据的NBT标签。像 AdvancedEnchants 这样的插件确实使用NBT标签（例如`ae_enchant:thorns`）来保存附魔（附魔等级是标签值）。确实建议使用Bukkit注册表。

你可以在`net.Indyuce.mmoitems.comp.enchants.advanced_enchants`查看 AdvancedEnchants 的`ItemStat`实现（查看源代码）。

注册你的属性**之前**MMOItems启用使用：

```java
MMOItems.plugin.getStats().register(...);
```

---

原文：[🔮 Enchant Plugins](https://docs.phoenixdevt.fr/mmoitems/compatibility/enchant-plugins) · 原文归档：2026-10-19
