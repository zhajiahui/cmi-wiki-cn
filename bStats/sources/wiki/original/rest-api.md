API

# REST API

Use the bStats REST API to embed plugin metrics in your site or tooling. All endpoints
are read-only and return JSON.

## Getting started

Requests are simple `GET` calls. No authentication is required for public data.

These examples assume the API is reachable at `https://bstats.org`.

### List plugins

```
GET /api/v1/plugins
```

Returns all plugins registered on bStats.

```
[
  {
    "id": 1337,
    "name": "ExamplePlugin",
    "owner": { "id": 42, "name": "ExampleUser" },
    "software": { "id": 1, "name": "Bukkit / Spigot", "url": "bukkit" },
    "isGlobal": false
  },
  ...
]
```

### Plugin details

```
GET /api/v1/plugins/{pluginId}
```

Returns metadata plus chart definitions for a specific plugin.

```
{
  "id": 1337,
  "name": "ExamplePlugin",
  "owner": { "id": 42, "name": "ExampleUser" },
  "charts": {
    "players": {
      "uid": 1234,
      "type": "single_linechart",
      "position": 0,
      "title": "Players",
      "isDefault": true,
      "data": {
        "lineName": "Players",
        "filter": { "enabled": false, "maxValue": null, "minValue": null }
      }
    }
  }
}
```

### Charts for a plugin

```
GET /api/v1/plugins/{pluginId}/charts
```

Returns the chart registry for a plugin.

```
{
  "players": {
    "uid": 1234,
    "type": "single_linechart",
    "position": 0,
    "title": "Players",
    "isDefault": true,
    "data": {
      "lineName": "Players",
      "filter": { "enabled": false, "maxValue": null, "minValue": null }
    }
  }
}
```

### Chart metadata

```
GET /api/v1/plugins/{pluginId}/charts/{chartId}
```

```
{
  "uid": 1234,
  "type": "single_linechart",
  "position": 0,
  "title": "Players",
  "isDefault": true,
  "data": {
    "lineName": "Players",
    "filter": { "enabled": false, "maxValue": null, "minValue": null }
  }
}
```

### Chart data

```
GET /api/v1/plugins/{pluginId}/charts/{chartId}/data
```

Returns raw chart data. For line charts each entry is `[timestamp, value]`.

```
[
  [1479799800000, 122],
  [1479801600000, 121],
  [1479803400000, 124],
  [1479805200000, 134]
]
```

Append `?maxElements={amount}` to limit the number of entries (line charts only).

### Supported software

```
GET /api/v1/software
```

```
[
  {
    "id": 1,
    "name": "Bukkit / Spigot",
    "url": "bukkit",
    "globalPlugin": { "id": 1, "name": "_bukkit_" }
  },
  ...
]
```
