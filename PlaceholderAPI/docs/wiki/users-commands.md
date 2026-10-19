---
title: 命令
source_url: https://wiki.placeholderapi.com/users/commands/
source_kind: official-wiki
translation_review: reviewed
source_version: official-site-2026-10-19-15adfb5d4a300156
---

<a id="commands"></a>
# 命令

本页列出了全部命令，并详细说明了每个命令的用途。

<a id="overview"></a>
## 一览

- **[解析命令](users-commands.md#parse-commands)**

  - [`/papi bcparse <player|me|--null> <text>`](users-commands.md#papi-bcparse)
  - [`/papi cmdparse <player|me|--null> <text>`](users-commands.md#papi-cmdparse)
  - [`/papi parse <player|me|--null> <text>`](users-commands.md#papi-parse)
  - [`/papi parserel <player|me> <player|me> <text>`](users-commands.md#papi-parserel)
- **[eCloud 命令](users-commands.md#ecloud-commands)**

  - [`/papi ecloud clear`](users-commands.md#papi-ecloud-clear)
  - [`/papi ecloud disable`](users-commands.md#papi-ecloud-disable)
  - [`/papi ecloud download <expansion> [version]`](users-commands.md#papi-ecloud-download)
  - [`/papi ecloud enable`](users-commands.md#papi-ecloud-enable)
  - [`/papi ecloud info <expansion> [version]`](users-commands.md#papi-ecloud-info)
  - [`/papi ecloud list <all|<author>|installed>`](users-commands.md#papi-ecloud-list)
  - [`/papi ecloud placeholders <expansion>`](users-commands.md#papi-ecloud-placeholders)
  - [`/papi ecloud refresh`](users-commands.md#papi-ecloud-refresh)
  - [`/papi ecloud status`](users-commands.md#papi-ecloud-status)
- **[占位符扩展命令](users-commands.md#expansion-commands)**

  - [`/papi info <expansion>`](users-commands.md#papi-info)
  - [`/papi list`](users-commands.md#papi-list)
  - [`/papi register <jar file>`](users-commands.md#papi-register)
  - [`/papi unregister <jar file>`](users-commands.md#papi-unregister)
- **[其他命令](users-commands.md#other-commands)**

  - [`/papi dump`](users-commands.md#papi-dump)
  - [`/papi help`](users-commands.md#papi-help)
  - [`/papi reload`](users-commands.md#papi-reload)
  - [`/papi version`](users-commands.md#papi-version)

---

<a id="parse-commands"></a>
### 解析命令

这些命令用于将占位符解析为对应的值，可用于调试。

<a id="papi-bcparse"></a>
#### `/papi bcparse`

**说明**:  
解析字符串中的占位符，并向所有玩家广播结果。

**参数**:

- `<player|me|--null>` - 解析占位符时使用的玩家（`me` 表示自己，`--null` 强制将玩家设为 null，适用于控制台）。
- `<text>` - 包含待解析占位符的文本。

**示例**:  

```
/papi bcparse funnycube My name is %player_name%!
```

<a id="papi-cmdparse"></a>
#### `/papi cmdparse`

**说明**:  
解析字符串中的占位符，并将结果作为命令执行。

**参数**:

- `<player|me|--null>` - 解析占位符时使用的玩家（`me` 表示自己，`--null` 强制将玩家设为 null，适用于控制台）。
- `<text>` - 包含待解析占位符的文本，解析后将作为命令执行（命令前不要加 `/`）。

**示例**:  

```
/papi cmdparse funnycube say My name is %player_name%!
```

<a id="papi-parse"></a>
#### `/papi parse`

**说明**:  
解析给定文本中的占位符，并显示结果。

**参数**:

- `<player|me|--null>` - 解析占位符时使用的玩家（`me` 表示自己，`--null` 强制将玩家设为 null，适用于控制台）。
- `<text>` - 包含待解析占位符的文本。

**示例**:  

```
/papi parse funnycube My group is %vault_group%
```

<a id="papi-parserel"></a>
#### `/papi parserel`

**说明**:  
解析关系占位符。

**参数**:

- `<player1|me>` - 第一名玩家（`me` 表示自己）。
- `<player2|me>` - 用于比较的第二名玩家（`me` 表示自己）。
- `<text>` - 包含待解析占位符的文本。

**示例**:  

```
/papi parserel funnycube extended_clip %placeholder%
```

---

<a id="ecloud-commands"></a>
### eCloud 命令

这些命令均以 `/papi ecloud` 开头，用于执行与 [Expansion Cloud](developers-expansion-cloud.md) 有关的操作。  
仅执行 `/papi ecloud`，不加任何参数，就会列出该命令下所有可用的子命令。

<a id="papi-ecloud-clear"></a>
#### `/papi ecloud clear`

**说明**:  
清除 eCloud 缓存。

<a id="papi-ecloud-disable"></a>
#### `/papi ecloud disable`

**说明**:  
禁用与 eCloud 的连接。

<a id="papi-ecloud-download"></a>
#### `/papi ecloud download`

**说明**:  
从 eCloud 下载占位符扩展。

**参数**:

- `<expansion>` - 要下载的占位符扩展。
- `[version]` - 要下载的占位符扩展的指定版本（可选）。

**示例**:  

```
/papi ecloud download Vault
/papi ecloud download Vault 1.5.2
```

<a id="papi-ecloud-enable"></a>
#### `/papi ecloud enable`

**说明**:  
启用与 eCloud 的连接。

<a id="papi-ecloud-info"></a>
#### `/papi ecloud info`

**说明**:  
显示指定占位符扩展的信息。

**参数**:

- `<expansion>` - 要查询信息的占位符扩展。
- `[version]` - 要查询信息的占位符扩展版本。

**示例**:  

```
/papi ecloud info Vault
```

<a id="papi-ecloud-list"></a>
#### `/papi ecloud list`

**说明**:  
列出 eCloud 上的全部占位符扩展、指定作者的扩展，或仅列出[已安装](users-commands.md#papi-ecloud-download)的扩展。  
已安装的占位符扩展在列表中显示为绿色；已安装且有可用更新的扩展显示为金色。

**参数**:

- `<all|<author>|installed>` - 列出全部占位符扩展、指定作者的扩展，或全部已安装的扩展。

**示例**:  

```
/papi ecloud list all
/papi ecloud list clip
/papi ecloud list installed
```

<a id="papi-ecloud-placeholders"></a>
#### `/papi ecloud placeholders`

**说明**:  
列出某个占位符扩展提供的全部占位符。

**参数**:

- `<expansion>` - 要列出占位符的扩展。

**示例**:  

```
/papi ecloud placeholders Vault
```

<a id="papi-ecloud-refresh"></a>
#### `/papi ecloud refresh`

**说明**:  
刷新从 eCloud 获取的缓存数据。

<a id="papi-ecloud-status"></a>
#### `/papi ecloud status`

**说明**:  
显示 eCloud 的当前状态。

---

<a id="expansion-commands"></a>
### 占位符扩展命令

这些命令用于管理当前已安装的占位符扩展。

<a id="papi-info"></a>
#### `/papi info`

**说明**:  
显示指定占位符扩展的信息。

**参数**:

- `<expansion>` - 要查询信息的占位符扩展（必须已注册且处于启用状态）。

**示例**:  

```
/papi info Vault
```

<a id="papi-list"></a>
#### `/papi list`

**说明**:  
列出全部已启用或已注册的占位符扩展。  
与 [/papi ecloud list installed](users-commands.md#papi-ecloud-list) 不同，此命令还会列出通过插件安装的占位符扩展（并非独立的 jar 文件），而且不会显示哪些扩展有可用更新。

<a id="papi-register"></a>
#### `/papi register`

**说明**:  
根据指定的文件名注册占位符扩展。  
适用于手动下载占位符扩展后，不想重启服务器的情况。  
文件必须放在 `/plugins/PlaceholderAPI/expansions` 中。

**参数**:

- `<filename>` - 要注册的文件（包含文件扩展名）。

**示例**:  

```
/papi register MyExpansion.jar
```

<a id="papi-unregister"></a>
#### `/papi unregister`

**说明**:  
注销指定的占位符扩展。

**参数**:

- `<filename>` - 要注销的占位符扩展。

**示例**:  

```
/papi unregister MyExpansion.jar
```

---

<a id="other-commands"></a>
### 其他命令

以下是 PlaceholderAPI 中不属于上述类别的其他命令。

<a id="papi-dump"></a>
#### `/papi dump`

**说明**:  
将 PlaceholderAPI 的插件版本、服务器版本、已安装的占位符扩展等有用信息上传到 <https://paste.helpch.at>，方便分享和寻求支持。

<a id="papi-help"></a>
#### `/papi help`

**说明**:  
显示 PlaceholderAPI 当前提供的全部命令。

<a id="papi-reload"></a>
#### `/papi reload`

**说明**:  
重新加载配置。  
从 eCloud [下载占位符扩展](users-commands.md#papi-ecloud-download)后，必须执行此命令，否则扩展无法正确注册。

<a id="papi-version"></a>
#### `/papi version`

**说明**:  
显示 PlaceholderAPI 的当前版本和作者。
