# AttributePlus Wiki 收录记录

快照：2026-10-19。随包版本：3.3.3.6。来源为 [AttributePlus Pro 官方 GitBook](https://ersha.gitbook.io/attributeplus-pro)。官方文档持续更新，没有固定到随包版本的标签；各页保留原有版本条件。

## 范围与清单

- 交叉核对官方 llms.txt 与 sitemap-pages.xml：47 个页面候选，40 页完整收录，7 页纯接口参考排除，页面 unavailable 为 0。
- 原文已经是中文，正文未重译。sources/wiki/original 保存 47 页完整 UTF-8、LF 原文及哈希；docs/wiki 保存可阅读页面。
- 配置、命令、语言文件、读取规则、机制、脚本教学、RUNTIME/UPDATE/CUSTOM/KILLER 教程、延迟触发示例、计数器示例、旧属性开发示例、触发器示例、内嵌条件示例、读取方式教学与更新记录均完整保留。
- Counter 等混合页面即使包含方法声明，也因包含实际使用示例而整页保留。开发文档目录下的教学页没有按目录整体排除。
- 7 个排除页的逐 URL 理由见 sources/wiki-coverage.json；对应原文仍在归档中。

## 格式与资源

平台为 Markdown 接口添加的英文 llms.txt 引导行只保存在原文归档，不混入 Wiki 正文。GitBook hint 标记转换为 MkDocs 提示框，类型和内容保留；图片、图注、表格、警告和代码原样保留。

15 个原生媒体文件完整下载，其中 2 个为原始 GIF，未缩放或转成静态图片。来源、字节数、SHA-256 见 sources/wiki/assets-manifest.json。原生 GIF 合计约 32.65 MB。

站内链接优先转为对应本地页面。原文中 8 处旧路径可通过官方现有同名页面唯一定位，映射记录在 sources/wiki/discovery/link-adjustments.json。KILLER 与更新日志引用的计数器示例保留原始锚点。排除的接口页仍链接官方站点。

## 原文已有问题

- 官方旧属性 Example 页明确写明示例已过时，此警告完整保留。
- 官方首页的 /plugin 路径以及原文版本支持范围按原样保留，未静默修订。
- 文档链接和历史记录中同时含旧版与新版条件，不将其中任何版本的机制自动套用于随包 3.3.3.6。

## 验证边界

本次核对文档完整性、来源哈希、受保护内容、本地链接和资源。不代表服务器或客户端运行验证。未修改项目首页、configuration、mkdocs 或 Site；未提交或发布。

## 本次校验结果

2026-10-19 本地核对通过，报告为 sources/wiki/validation/report.json。核对 40 页，51 个代码块、109 个受保护行内代码项、15 个原生资源文件；来源 SHA-256、frontmatter、manifest/nav/coverage 一致性、本地链接与锚点检查均无错误。unavailable 是来源获取状态，不会因静态校验通过而改为已取得。
