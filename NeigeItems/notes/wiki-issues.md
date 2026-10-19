# NeigeItems 官方公开资料与付费 Wiki 缺口

核对日期：2026-10-19。当前 main 与 1.22.0 标签均对应提交 8791487eeec1866b30f45c34a60fbc0e738c9ecf。完整官方 Wiki 状态：**unavailable**；本次取得的是公开仓库材料。

## 当前公开入口核验

[当前官方 README](https://github.com/ankhorg/NeigeItems-Kotlin/blob/1.22.0/README.md) 明确写明：“Wiki付费, 99元永久, 如欲购买请添加作者QQ: 2468629609”。当前默认分支仍保留这段声明。README 提供 Javadoc 链接，没有公开用户 Wiki 目录链接。

公开 GitHub Wiki 入口转回仓库主页，未提供独立页面列表；完整仓库树中只有 README.md 和构建用第三方许可说明两个 Markdown 文件，没有用户 docs/wiki 目录或 sitemap。仓库树与提交证据在 sources/wiki/discovery/repository-snapshot.txt。

没有取得完整付费 Wiki 的目录或正文，因此其内部候选页数未知。coverage 对完整 Wiki 标为 unavailable、enumeration_complete: false，未用公开说明和示例页数冒充完整 Wiki 页数。

## 已完整收录的公开内容

- 公开 README 的非 API 段落：插件说明、Javadoc 原链接、原有付费声明和 bStats 原图。
- 当前 1.22.0 官方仓库的 15 个完整随包文件：config.yml（含全部中文帮助）、plugin.yml 模板、物品、物品动作、物品包、动作组、全局节点、用户脚本、扩展示例和 JavaScript 工具库。每页包含完整原文件，注释、配置键、概率、参数及占位符不变。
- README Development/API 与官方 Javadoc 标为 excluded_api。用户扩展示例及 JavaScriptLib/lib.js 工具库均保留全文，没有因为调用或提供方法而排除正常脚本材料。

共 16 页公开材料、1 个原生 SVG。每页 frontmatter 另有 source_material 和 scope_note，明确其属于公开仓库材料。source_kind 按本次收录契约统一为 official-wiki，并不声称仓库文件来自付费 Wiki。

## 限制与未采用资料

未访问付费墙后的目录或正文，未读取或引用工作区外的私有/付费归档、技能资料或会话材料，也未上传此类内容。未将历史站点或社区教程认作当前官方 Wiki。

plugin.yml 中的 `${name}`、`${group}`、`${version}` 为官方源文件构建占位符，保持原样；未据此替换为运行时 JAR 元数据。

本次只核对公开来源、文件完整性、哈希、链接和资源。未修改已有首页与 configuration，也未修改 mkdocs 或 Site；未提交发布，未声称游戏内验证。

## 本次校验结果

2026-10-19 本地核对通过，报告为 sources/wiki/validation/report.json。核对 16 页，15 个代码块、0 个受保护行内代码项、1 个原生资源文件；来源 SHA-256、frontmatter、manifest/nav/coverage 一致性、本地链接与锚点检查均无错误。unavailable 是来源获取状态，不会因静态校验通过而改为已取得。
