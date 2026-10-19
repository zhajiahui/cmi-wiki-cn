# LuckPerms Wiki 翻译核对记录

## 完成范围

- 固定官方 Wiki 仓库提交：`fc2919c3d5e6bfba82af31f9930273b00f08ddbf`。
- 官方目录与仓库共有正文 47 页：完整翻译 45 页，排除 API 2 页；正文来源不可用 0 页。
- 以官方 `_Sidebar.md` 与全部页面清单交叉核对范围；独立应用与 REST API 入口介绍、贡献指南、技术细节页均完整收录。
- 原始 Markdown 统一为 UTF-8/LF 后归档并计算 SHA-256；图片/动图原始字节和来源 hash 保留。

## API 排除项

- [开发 API 用法](https://luckperms.net/wiki/Developer-API-Usage)：插件 API 接口与编程用法文档。
- [开发 API 简介](https://luckperms.net/wiki/Developer-API)：插件 API 接口与编程用法文档。

## 原文疑点（未静默改写事实或示例）

- [配置](https://luckperms.net/wiki/Configuration)：附加权限段落对“启用”的效果描述有疑点；`sync-minutes` 的示例位于 `data` 下；JSON 示例含尾随逗号。译文保留各处原有条件、缩进和示例。
- [上下文](https://luckperms.net/wiki/Context)：默认上下文一段写为 `contexts.yml`，与其他位置的 `contexts.json` 不一致，保留各自文件名。
- [用户命令](https://luckperms.net/wiki/User-Commands)：用户 `editor` 命令的说明写作编辑“指定权限组”，译文未擅自改为用户。
- [基于参数的命令权限](https://luckperms.net/wiki/Argument-based-command-permissions)：原文称“3 部分”，目录实际列出 4 类，保留两处原文信息。
- [单服务器安装](https://luckperms.net/wiki/Installation)与[存储类型](https://luckperms.net/wiki/Storage-types)：H2 文件名分别写为 `luckperms-h2-v2.mv.db` 与 `luckperms-h2.mv.db`，没有跨页统一为推测值。
- [高级设置](https://luckperms.net/wiki/Advanced-Setup)：正则表达式说明要求使用 `R=` 前缀，但随后的示例未包含此前缀，按原样保留。
- [常见问题](https://luckperms.net/wiki/FAQ)与[多服务器安装](https://luckperms.net/wiki/Network-Installation)：部分场景的消息服务选项建议不同，未自行裁定并改写。
- [元数据命令](https://luckperms.net/wiki/Meta-Commands)、[权限组命令](https://luckperms.net/wiki/Group-Commands)、[常规命令](https://luckperms.net/wiki/General-Commands)：部分目录、命令标题和参数说明写法不一致；搜索比较符表中另有未闭合引号。全部原有技术标记保留。
- [网页编辑器技术细节](https://luckperms.net/wiki/Web-Editor-Technical-Details)：原文写为“使用公钥签名”，JSON 示例保留尾随逗号。未以翻译名义修改机制描述。
- [独立应用与 REST API](https://luckperms.net/wiki/Standalone-and-REST-API)：继承说明的行内代码包含 `import`，保持原样。
- [切换存储类型](https://luckperms.net/wiki/Switching-storage-types)：网页导出流程未列出重新启动服务器步骤，没有自行增加步骤。

## 原文链接问题与译文调整

- Weight 的部分链接错误地将页面名放入片段（如 `#Group-Commands#...`）；译文改为指向已存在的对应本地译文及其原有锚点。
- Verbose 的 `#Permissions`、网页编辑器技术细节的 `#Web-Editor` 明确指向其他页面，译文改为相应本地页面链接。
- Configuration 的目录含 `#group-weight`，但当前原文正文未提供对应节；Hytale 的目录含 `#known-caveatsissues`，但当前正文没有对应标题。两处缺项如实保留并记录，没有补造缺失章节。
- 其余翻译后标题保留官方原始 ID，站内链接映射到对应译文；API 排除页继续链接官方来源。

## 核对方式

逐页对照全文，检查原文 hash、完整围栏代码块、行内技术标记、表格行数、原文显式锚点、原生资源 hash 及未翻译正文。错误日志、命令、代码与技术示例保留原样。

以上为文档与静态资料核对，没有在游戏服务器中验证命令、权限或功能行为。

## 过时命令锚点的导航修复

官方命令清单与权限表中，部分链接仍使用增加参数前的旧标题锚点。译文仅将其指向同一原有命令的实际标题 ID，没有改动命令、参数或示例。完整逐项记录见来源归档中的 `link-repairs.json`。旧的上下文定义入口改为现有上下文译文页。
