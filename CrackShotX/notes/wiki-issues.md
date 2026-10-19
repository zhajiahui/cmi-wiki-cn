# CrackShotX Wiki 来源缺口

核对日期：2026-10-19。随包版本：1.1.0。完整官方 Wiki 状态：**unavailable**。

## 已有版本证据

sources/overview-sources.md 和 sources/plugin-metadata.json 记录的随包描述包含 CrackShot 依赖、csx 主命令及 crackshotx.admin、crackshotx.panel 等权限，但作者和网站字段缺失。这些证据没有给出官方导航、sitemap 或仓库。

## 公开核验

GitHub 仓库名、README、版本字符串及独有权限节点的查询记录见 sources/wiki/discovery/search-log.json。未找到能确认该 1.1.0 随包版出处的仓库或文档。全词代码搜索唯一结果是无关聊天数据；Spigot 公开搜索返回 HTTP 403；Bing 返回与查询不相关的结果，未将其作为来源或“不存在”的证据。

因此既未取得对应版完整导航，也未取得可安全归属版本的旧官方 Wiki。当前内部页面总数未知，在 coverage 中以 url: null 的 unavailable 条目记录，而非编造候选页面 URL。wiki-manifest.json 为空列表，wiki-nav.yml 为 []，文档页数为 0。

## 版本边界

未使用 CrackShot 主插件或 CrackShotPlus 的文档代替 CrackShotX，也未将旧版功能、命令、权限或面板机制套用于此 1.1.0 包。此次未收录版本对应未确认的旧文档。

后续需要能确认此包归属的作者、官网、仓库或发布记录，才能继续按官方目录补齐。当前结果表示“公开来源未确认”，不表示此项目或文档一定不存在。

未修改现有概览、配置或站点文件；未提交发布。

## 本次校验结果

2026-10-19 本地核对通过，报告为 sources/wiki/validation/report.json。核对 0 页，0 个代码块、0 个受保护行内代码项、0 个原生资源文件；来源 SHA-256、frontmatter、manifest/nav/coverage 一致性、本地链接与锚点检查均无错误。unavailable 是来源获取状态，不会因静态校验通过而改为已取得。
