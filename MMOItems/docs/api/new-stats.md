---
title: 新增属性
source: https://docs.phoenixdevt.fr/mmoitems/api/new-stats
source_snapshot: '2026-10-19'
---

# 新增属性 {#💗-new-stats}

> **警告**
>
> MI7 中可能会有较大改动。

使用MMOItemsAPI，你可以注册与能力或物品限制一样复杂的自定义属性。你需要做的第一件事是定义一个扩展`ItemStat`的类，这是一个具有许多函数的抽象类，我们将介绍每个函数的作用，但首先让我们处理你需要调用的 ItemStat 构造函数。

## 项目统计构造函数 {#itemstat-constructor}

```java
ItemStat(String id, Material material, String name, String[] lore, String[] types, Material... materials)
```

`id`字符串对应于你的内部属性ID。你只能使用大写字母和 _ 破折号。这个属性用于计算MMOLib中的玩家属性，用于将属性数据保存在MMOItems配置文件中，实际上在插件中的任何位置。设置属性后切勿更改它，否则你可能会“丢失”之前创建的物品数据。

`material`参数对应于属性在物品版本GUI中的图标。`name`对应你的属性名称，它也用于显示你的属性版本GUI。正常的玩家是看不到这段字符串的。`lore`是你的属性描述（版本GUI）。

`types`是物品属性支持的物品类型的列表。

`new String[] { "!armor", "!gem_stone", "all" }`将禁止盔甲和宝石使用你的属性。使用`!<type_name>`你可以禁止特定的物品类型。确保将类型限制放在字符串数组的开头。使用`all`，你可以使属性与任何物品类型兼容。确保在类型限制后使用`all`。

`materials`是支持的物品材料。这是特定于某些属性的，例如`Dye Color`或`Shield Pattern`，它们依赖于 ItemMeta 实例，并且是type-specific。如果给定的数组为空，则默认情况下属性显然可用于任何类型。

## 重写的方法 {#methods-to-override}

这是数字属性的类。

```java
@Override
public StatData whenInitialized(Object object) {
	return new DoubleData(object);
}

@Override
public RandomStatData whenInitializedGeneration(Object object) {
	if (object instanceof Number)
		return new NumericStatFormula(Double.valueOf(object.toString()), 0, 0, 0);
	
	if (object instanceof ConfigurationSection) 
		return new NumericStatFormula((ConfigurationSection) object);
	
	throw new IllegalArgumentException("Must specify a number or a config section");
}

@Override
public void whenApplied(MMOItemBuilder item, StatData data) {
	double value = ((DoubleData) data).generateNewValue();
	item.addItemTag(new ItemTag(getNBTPath(), value));
	item.getLore().insert(getPath(), formatPath(value, "#", new StatFormat("##").format(value)));
}

@Override
public boolean whenClicked(EditionInventory inv, InventoryClickEvent event) {
	if (event.getAction() == InventoryAction.PICKUP_HALF) {
		ConfigFile config = inv.getItemType().getConfigFile();
		config.getConfig().set(inv.getItemId() + "." + getPath(), null);
		inv.registerItemEdition(config);
		inv.open();
		inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + "Successfully removed " + getName() + ChatColor.GRAY + ".");
		return true;
	}
	new StatEdition(inv, this).enable("Write in the chat the numeric value you want.",
			"Or write [MIN-VALUE]=[MAX-VALUE] to make the stat random.");
	return true;
}

@Override
public boolean whenInput(EditionInventory inv, ConfigFile config, String message, Object... info) {
	String[] split = message.split("=");
	double value = 0;
	double value1 = 0;
	try {
		value = Double.parseDouble(split[0]);
	} catch (Exception e1) {
		inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + ChatColor.RED + split[0] + " is not a valid number.");
		return false;
	}

	// second value
	if (split.length > 1)
		try {
			value1 = Double.parseDouble(split[1]);
		} catch (Exception e1) {
			inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + ChatColor.RED + split[1] + " is not a valid number.");
			return false;
		}

	// STRING if length == 2
	// DOUBLE if length == 1
	config.getConfig().set(inv.getItemId() + "." + getPath(), split.length > 1 ? value + "=" + value1 : value);
	if (value == 0 && value1 == 0)
		config.getConfig().set(inv.getItemId() + "." + getPath(), null);
	inv.registerItemEdition(config);
	inv.open();
	inv.getPlayer().sendMessage(MMOItems.plugin.getPrefix() + getName() + " successfully changed to "
			+ (value1 != 0 ? "{between " + value + " and " + value1 + "}" : "" + value) + ".");
	return true;
}

@Override
public void whenLoaded(MMOItem mmoitem, NBTItem item) {
	if (item.hasTag(getNBTPath()))
		mmoitem.setData(this, new DoubleData(item.getDouble(getNBTPath())));
}

@Override
public void whenDisplayed(List<String> lore, FileConfiguration config, String id) {
	lore.add("");

	String[] split = config.contains(id + "." + getPath()) ? config.getString(id + "." + getPath()).split("=") : new String[] { "0" };
	String format = split.length > 1 ? tryParse(split[0]) + " -> " + tryParse(split[1]) : "" + config.getDouble(id + "." + getPath());

	lore.add(ChatColor.GRAY + "Current Value: " + ChatColor.GREEN + format);
	lore.add("");
	lore.add(ChatColor.YELLOW + AltChar.listDash + " Left click to change this value.");
	lore.add(ChatColor.YELLOW + AltChar.listDash + " Right click to remove this value.");
}
```

### `whenInitialized(Object)` {#wheninitialized-object}

当MMOItems请求从配置文件读取属性数据时，调用`whenInitialized(Object)`。`obj`可以是任何东西，它是使用`ConfigurationSection#get(yourStatPath)`获得的对象。在这里，用户可以使用 double 来设置属性值，也可以使用配置部分，在这种情况下，MMOItems从该配置部分读取数字属性公式。

此方法必须返回一个扩展`StatData`接口的类。它是一个**纯粹的装饰**界面，因为它没有可以覆盖的功能，但我可能需要在以后的更新中向它添加一些功能。 **你可以在可合并属性部分下看到 StatData 类示例**。

### `whenInitializedGeneration(Object)` {#wheninitializedgeneration-object}

`whenInitializedGeneration(Object)`几乎是同样的事情，只是它应该返回一个`RandomStatData`实例。`RandomStatData`接口用于存储来自物品生成模板的属性数据。有关更多信息，请参阅下面的 RandomStatData 段落。

### `whenApplied(MMOItemBuilder, StatData)` {#whenapplied-mmoitembuilder-statdata}

MMOItems在根据`StatData`实例列表生成`ItemStack`实例时使用此函数。你可以使用`MMOItemBuilder`实例访问物品元、物品描述。你需要将作为输入给出的`StatData`实例转换为与属性兼容的任何实例。MMOItems只为你提供在`whenInitialized(Generation)`方法中作为输出提供的输入。

### `whenClicked(EditionInventory, InventoryClickEvent)` {#whenclicked-editioninventory-inventoryclickevent}

这是当玩家只需单击物品版本GUI中的属性图标时用于执行操作的函数。

### `whenInput(EditionInventory, ConfigFile config, String message, Object...)` {#wheninput-editioninventory-configfile-config-string-message-object}

用于当玩家在聊天中输入一些消息时执行操作。你可以使用以下方法请求玩家聊天输入：`new StatEdition(inv, this, objectArray).enable("Write in the chat the numeric value you want.", "Or write [MIN-VALUE]=[MAX-VALUE] to make the stat random.");`当玩家单击版本GUI中的属性图标时，通常会调用该函数。`StatEdition`类构造函数中的`objectArray`参数可以替换为**任何对象**，这是一种更复杂的属性的方式，例如玩家正在编辑的元素或能力（是能力施放模式，什么能力等？？）。该数组保持完整并作为`whenInput`方法的输入给出。

### `whenLoaded(MMOItem, NBTItem)` {#whenloaded-mmoitem-nbtitem}

用于从随机 ItemStack 加载属性数据。

### `whenDisplayed(List<String>, ConfigurationSection, String)` {#whendisplayed-list-string-configurationsection-string}

这是一个非常古老的方法，很快就会更新。该函数用于显示GUI版本中当前物品属性数据。它仍然使用配置部分作为输入，它将很快被 StatDatas 取代以实现更清晰的功能。

## `RandomStatData`的 {#randomstatdata-s}

它们与`StatData`等效，但具有随机物品生成所需的随机因子。一个很好的例子是`NumericStatFormula`类，它用于任何数字属性。

```java
public class NumericStatFormula implements RandomStatData {
	private final double base, scale, spread, maxSpread;

	private static final Random random = new Random();

	public static final NumericStatFormula ZERO = new NumericStatFormula(0, 0, 0, 0);

	public NumericStatFormula(Object object) {
		Validate.notNull(object, "Config must not be null");

		if (object instanceof Number) {
			base = Double.valueOf(object.toString());
			scale = 0;
			spread = 0;
			maxSpread = 0;
			return;
		}

		if (object instanceof ConfigurationSection) {
			ConfigurationSection config = (ConfigurationSection) object;
			base = config.getDouble("base");
			scale = config.getDouble("scale");
			spread = config.getDouble("spread");
			maxSpread = config.getDouble("max-spread");

			Validate.isTrue(spread >= 0, "Spread must be positive");
			Validate.isTrue(maxSpread >= 0, "Max spread must be positive");
			return;
		}

		throw new IllegalArgumentException("Must specify a config section or a number");
	}

	/*
	 * used as a StatData class to generate a DoubleData instance!
	 */
	public NumericStatFormula(double base, double scale, double spread, double maxSpread) {
		this.base = base;
		this.scale = scale;
		this.spread = spread;
		this.maxSpread = maxSpread;
	}

	public double getBase() {
		return base;
	}

	public double getScale() {
		return scale;
	}

	public double calculate(double x) {

		// calculate linear value
		double linear = base + scale * x;

		// apply gaussian distribution to add +- maxSpread%
		// spread represents the standard deviation in % of the calculated
		// linear value
		double gaussian = linear * (1 + Math.min(Math.max(random.nextGaussian() * spread, -maxSpread), maxSpread));

		return gaussian;
	}

	@Override
	public StatData randomize(GeneratedItemBuilder builder) {
		return new DoubleData(calculate(builder.getLevel()));
	}
}
```

`#randomize(..)`函数是这里的关键。这将包含有关物品等级、层等的信息的 generatedItemBuilder 作为输入，并输出随机的`RandomStatData`、i.e和`StatData`实例，该实例稍后将用于构建物品！

`GeneratedItemBuilder`类可以看作是随机属性生成的`MMOItemBuilder`的等效项。当从物品模板生成随机物品时，MMOItems首先创建`GeneratedItemBuilder`，滚动物品修饰器并在使用`MMOItemBuilder`生成物品时收集随机`StatData`。

## 可合并属性 {#mergeable-stats}

可合并的属性是可以相互堆叠的属性，例如，当玩家尝试将宝石应用到另一个物品上时，MMOItems需要将两个属性数据“合并”在一起。`DoubleData`类就是一个很好的例子。

```java
public class DoubleData implements StatData, Mergeable {
	private static final Random random = new Random();

	private double min, max;

	public DoubleData(Object object) {
		if (object instanceof Number) {
			min = Double.valueOf(object.toString());
			return;
		}

		if (object instanceof String) {
			String[] split = ((String) object).split("=");
			Validate.isTrue(split.length == 2, "Must specify a valid range");
			min = Double.parseDouble(split[0]);
			max = Double.parseDouble(split[1]);
			return;
		}

		throw new IllegalArgumentException("Must specify a range or a number");
	}

	public DoubleData(double min, double max) {
		this.min = min;
		this.max = max;
	}

	public boolean hasMax() {
		return max > min && max != 0;
	}

	public double getMin() {
		return min;
	}

	public double getMax() {
		return max;
	}

	public void setMax(double value) {
		max = value;
	}

	public void setMin(double value) {
		min = value;
	}

	public void add(double value) {
		min = min + value;
	}

	public void addRelative(double value) {
		min *= 1 + value;
	}

	public double generateNewValue() {
		return hasMax() ? min + random.nextDouble() * (max - min) : min;
	}

	@Override
	public void merge(StatData data) {
		Validate.isTrue(data instanceof DoubleData, "Cannot merge two different stat data types");
		min += ((DoubleData) data).min;
		// TODO if hasMax()
	}
}
```

很简单：MMOItems只是将两个值相加。这里有一点规范：`min`和`max`选项用于具有属性范围，但每当使用`whenLoading(MMOItem mmoitem, NBTItem)`从 NBTItem 加载`StatData`时，仅使用`min`变量，因为生成的物品没有属性系列不再存在，它们已经推出到物品一代。

## 注册属性 {#registering-a-stat}

现在，你需要通过运行`MMOItems.plugin.getStats().register(ItemStat);`来注册你的属性确保在MMOItems启用之前注册你的属性，或者在MMOItems加载（如果它是依赖项）之后立即注册，或者在你的插件启用（如果它是加载之前）。MMOItems确实处理`Listener`属性，以后无需注册它们。

这会将属性注册到MMOItems中，因此默认情况下你的属性将出现在物品版本GUI中。以下两个步骤将使你的属性显示在任何生成的物品上的物品描述中：

1. 将你的属性添加到当前的描述格式。你可以通过打开`language/lore-format.yml`并在其中添加一行来完成此操作；例如，`- '#attack-damage#'`是攻击伤害属性的行。
2. 编辑你的`stats.yml`配置部分并在此处添加所需的翻译；例如，你可以为攻击伤害属性添加`attack-damage: '&3 &7➸ Attack Damage: &f{value}'`。

## 物品限制 {#item-restrictions}

```java
public class RequiredLevel extends DoubleStat implements ItemRestriction {

	/*
	 * stat that uses a custom DoubleStatData because the merge algorithm is
	 * slightly different. when merging two "required level", MMOItems should
	 * only keep the highest levels of the two and not sum the two values
	 */
	public RequiredLevel() {
		super("REQUIRED_LEVEL", new ItemStack(VersionMaterial.EXPERIENCE_BOTTLE.toMaterial()), "Required Level",
				new String[] { "The level your item needs", "in order to be used." }, new String[] { "all" });
	}

// ..........

	@Override
	public boolean canUse(RPGPlayer player, NBTItem item, boolean message) {
		int level = item.getInteger("MMOITEMS_REQUIRED_LEVEL");
		if (player.getLevel() < level && !player.getPlayer().hasPermission("mmoitems.bypass.level")) {
			if (message) {
				Message.NOT_ENOUGH_LEVELS.format(ChatColor.RED).send(player.getPlayer(), "cant-use-item");
				player.getPlayer().playSound(player.getPlayer().getLocation(), Sound.ENTITY_VILLAGER_NO, 1, 1.5f);
			}
			return false;
		}
		return true;
	}
}
```

只需让你的类实现`ItemRestriction`并重写`canUse(RPGPlayer, NBTItem, boolean)`方法即可。

## 正品属性 {#proper-stats}

“正确的”属性是属性的一种非常特殊的类型。这些是属性，由宝石支撑，但当宝石被附加到另一个物品上时，**不得**应用于目标物品。

示例：自定义模型数据、屏蔽图案、自定义声音...

如果你不希望 gem 将潜在宝石属性数据应用到目标物品上，请让你的属性类实现`ProperStat`接口。

## 可升级 {#upgradable}

稍后在 MI7 更新期间将详细介绍这一点。

---

原文：[💗 New Stats](https://docs.phoenixdevt.fr/mmoitems/api/new-stats) · 原文归档：2026-10-19
