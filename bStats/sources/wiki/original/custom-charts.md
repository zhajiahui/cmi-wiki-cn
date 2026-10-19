Documentation

# Custom charts

bStats ships a handful of chart types you can wire into your Metrics instance.

## Basics

Adding a custom chart consists of two steps: provide the data in your plugin code
and register the chart on the website.

1. Navigate to your plugin page and click **Edit**.
2. Add a new chart and assign the chart ID you use in code.

## Pie charts

Great for categorical data such as configuration options Simple pies track one
value per server. Advanced pies let you collect multiple values per server.

### Simple pie

### Java

### PHP

 

```
metrics.addCustomChart(new SimplePie("used_language", () -> {
    return config.getString("language", "English");
}));
// If you use the copy & paste Metrics classes, use `Metrics.SimplePie` instead
```

### Advanced pie

### Java

### PHP

 

```
metrics.addCustomChart(new Metrics.AdvancedPie("player_gamemodes", () -> {
    Map<String, Integer> gamemodeMap = new HashMap<>();
    
    for (Player player : Bukkit.getOnlinePlayers()) {
        String gamemode = player.getGameMode().name();
        gamemodeMap.put(gamemode, gamemodeMap.getOrDefault(gamemode, 0) + 1);
    }
    
    return gamemodeMap;
}));
// If you use the copy & paste Metrics classes, use `Metrics.AdvancedPie` instead
```

## Drilldown pie

Ideal when you want to group categories and drill into details.

Click the slices to view details

### Drilldown pie

### Java

### PHP

 

```
metrics.addCustomChart(new DrilldownPie("java_version", () -> {
    // Format: Map<Category, Map<Subcategory, Count>>
    Map<String, Map<String, Integer>> data = new HashMap<>();

    String javaVersion = System.getProperty("java.version");
    Map<String, Integer> subCategory = new HashMap<>();
    subCategory.put(javaVersion, 1);

    if (javaVersion.startsWith("1.7")) {
        data.put("Java 7", subCategory);
    } else if (javaVersion.startsWith("1.8")) {
        data.put("Java 8", subCategory);
    } else if (javaVersion.startsWith("1.9")) {
        data.put("Java 9", subCategory);
    } else {
        data.put("Other", subCategory);
    }

    return data;
}));
// If you use the copy & paste Metrics classes, use `Metrics.DrilldownPie` instead
```

## Line charts

Track trends over time. Single line charts are perfect for players, servers, or
any value that has one sample per interval. Multi line charts let you compare
metrics side by side.

### 1d

### 1w

### 1m

### 3m

### 1y

### All

### Single line chart

### Java

### PHP

 

```
metrics.addCustomChart(new SingleLineChart("players", () -> {
    // There is already a player count chart by
    // default. This is just an example.
    return Bukkit.getOnlinePlayers().size();
}));
// If you use the copy & paste Metrics classes, use `Metrics.SingleLineChart` instead
```

### Multi line chart

### Java

### PHP

 

```
metrics.addCustomChart(new MultiLineChart("players_and_servers", () -> {
    Map<String, Integer> valueMap = new HashMap<>();
    valueMap.put("servers", 1);
    valueMap.put("players", Bukkit.getOnlinePlayers().size());
    return valueMap;
}));
// If you use the copy & paste Metrics classes, use `Metrics.MultiLineChart` instead
```

(Note: Multi line charts are still in development)

## Bar charts

Surface rankings or option adoption. Simple bar charts display a single value
per category. Advanced bar charts support multiple bars per category.

### Simple bar chart

### Java

### PHP

 

```
metrics.addCustomChart(new SimpleBarChart("features", () -> {
    // Format: Map<Category, Value>
    Map<String, Integer> map = new HashMap<>();
    map.put("Feature A", 1);
    return map;
}));
// If you use the copy & paste Metrics classes, use `Metrics.SimpleBarChart`instead
```

### Advanced bar chart

### Java

### PHP

 

```
metrics.addCustomChart(new AdvancedBarChart("features", () -> {
    // Format: Map<Category, [<Bar 1 Value>, <Bar 2 Value>, ...]>
    Map<String, int[]> map = new HashMap<>();
    map.put("Feature A", new int[]{0, 1});
    map.put("Feature B", new int[]{1, 0});
    return map;
}));
// If you use the copy & paste Metrics classes, use `Metrics.AdvancedBarChart` instead
```
