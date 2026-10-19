# Multiverse-Core 官方 Wiki 翻译记录

## 范围与快照

- 插件基线：`5.8.1`。
- 官方 Wiki 快照时间：`2026-10-19T14:57:54.668677+00:00`。
- 目录来源：https://github.com/Multiverse/multiverse-web/tree/d571cd29a391ce3affe2a21d9f68c4c275a6f33e。
- 官方文档仓库：`Multiverse/multiverse-web`，固定提交 `d571cd29a391ce3affe2a21d9f68c4c275a6f33e`；同时核对 `config/sidebar/core.js`、`config/sidebar/mv5.js` 和完整路由目录。
- Core 目录 19 页，其中 2 页 API 开发参考排除；另保留 5 页与 Core 有关的共用 MV5 说明，共完成 22 页译文。Multiverse-Inventories 等独立插件的整套手册不归入 Core；原文中的跨插件链接保留为官方外链。
- Wiki 是滚动更新资料，不是随 5.8.1 发布的独立文档包。原文已包含 v5.7、Paper 26.1+ 等条件；按固定提交完整保留，没有将这些资料改写成“全部已在 5.8.1 验证”。

## 排除的 API 页面

- [API Usages](https://mvplugins.org/core/developers/api-usage/)：Developer API and SDK integration reference。
- [Developer API Starter](https://mvplugins.org/core/developers/developer-api-starter/)：Developer API and SDK integration reference。

混合页面中少量 API 说明随整页保留，未因出现 API 字样而删除玩家或服主正文。

## 原站缺失与疑点

- `permissions-setup` 使用 `enforceaccess`，而当前配置样例使用 `enforce-access`；同页文字还使用 `multiverse.world.list`，示例命令则使用 `multiverse.core.list`，权限清单另列 `multiverse.core.list.worlds`。这些旧名按原文保留，未静默修订命令。
- `world-properties` 的 Adjust Spawn 段落写着“不希望修正位置时打开变量”，与该段其他说明存在歧义。翻译保留开关方向，未根据推测反转。
- World Blacklist 段落的一般说明与紧接着的方向示例容易产生歧义，均按原文保留。
- `configuration-file` 的版本输出示例仍写配置版本 2.7；与实际附带的新配置样例一并保留。
- 占位符清单的 `%multiverse-core_time_<format>` 在原文缺少结尾 `%`，按原文保留。
- `/mv confirm <otp>` 是原文缩进代码，不将 `<otp>` 翻译或转为 HTML 标签。

## 图片与链接

- 保存原始图片 18 个，未缩放或重绘。来源、使用页、文件大小及 SHA-256 见 `sources/wiki/assets-manifest.json`。
- 已存在译文的站内链接指向本地译文，API 和外站链接保留官方目标；原始来源链接与原文中的外部站点不做替换。
- 修复 14 个可确定对应关系的大小写、标点或旧名称锚点。

## 核对

- 每页 frontmatter 包含 `title`、`source_url`、`source_kind: official-wiki`、`translation_review: reviewed`、`source_version`。
- Manifest 是逐页对象列表；`source_sha256` 对统一 UTF-8/LF 原文计算。
- 22 页、111 个代码块、963 个行内代码标记、18 个图片文件已完成保真及本地链接检查，`verification.json` 的 `errors` 为 `[]`。
- 统一校对关键术语、开关方向、前置条件、数量、权限、命令示例和表格技术单元格；模板、商店、NPC 点击命令及基础安装/权限步骤另有人工审译覆盖。
- 此次检查覆盖原文对照及文件结构；未启动 Minecraft 服务器或客户端，未执行游戏内命令。
- 仅交付两个项目的 `docs/wiki`、`sources/wiki`、三个 Wiki 清单文件及本记录；未修改公共 Site、现有配置目录、项目主页或 mkdocs.yml，未提交或发布。

## 术语

world：世界；world property：世界属性；spawn point：出生点；respawn：重生；respawn anchor：重生锚；anchor：传送锚点；entry fee：入场费；namespaced key：命名空间键；world meta：世界元数据；generator：生成器；advancement：进度。
