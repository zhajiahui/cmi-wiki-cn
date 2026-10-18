# 合并站点验证记录

## 内容与目录

- CMI：45 页译文、162 个本地资源；Residence：10 页译文、9 个本地资源。
- 全站顶部恰有 CMI、Residence 两个分类。CMI 保留原公开路径，Residence 使用 `residence/`。
- 项目分别位于根目录 `CMI/`、`Residence/`；共同导航、主题和建站脚本位于 `Site/`。Git 历史与原仓库地址沿用。
- CMI 的原文、译稿、网站正文及图片仅调整本地目录位置，未在本轮改写。已将迁移前的 353 个正文、来源和资源文件与新位置逐项比对，内容一致。

## 本地构建与浏览器

- 两个项目的内容校验均通过。
- `mkdocs build --strict -f Site/mkdocs.yml` 通过，构建警告为 0；主题自身的版本迁移横幅为控制台提示。
- 构建产物共 56 个 HTML 文件：55 个文档页与 404 页。
- 检查 8,426 处站内文件、资源引用和锚点，无缺失；所有页面的“编辑此页”均指向所属项目的源文件。
- 全文搜索索引有 939 个页面、章节和列表行记录，覆盖 CMI 45 页和 Residence 10 页；结果标有插件名称。59 个权限节点和 113 个领地标志另有逐项搜索记录，可直接跳转到表格对应行。
- 浏览器实测顶部分类切换成功；“领地”检索命中 Residence 文档，结果显示所属插件。
- 390px 手机宽度下，两个分类均可在菜单中展开；Residence 文档可正常跳转，正文宽度未超过视口。
- 根目录 `启动.bat --no-browser --port 8001` 实际启动成功。

## 构建目录

Windows 不区分 `Site` 与 `site`。本轮首次尝试使用 `site/` 输出，清理时移除了刚创建的公共文件；两个项目资料未受影响。公共文件已恢复，输出改为 `.cache/site/`，构建脚本也检查输出是否与项目源目录重叠。

## 运行验证范围

以上是文档内容、静态构建与网站浏览器验证；未在 Minecraft 服务端测试插件功能。

## 线上发布

- 2026-10-18，两个分类已发布到 https://zhajiahui.github.io/cmi-wiki-cn/ ，Residence 入口为 `residence/`。
- [合并站点工作流](https://github.com/zhajiahui/cmi-wiki-cn/actions/runs/39089441407) 的构建与部署均成功。
- 首页与 Residence 10 个页面均实际返回 HTTP 200；9 个线上图片文件的 SHA-256 与归档记录一致。
- 线上已核对两个分类入口、项目目录、编辑链接、搜索结果的插件标记。

## 权限和标志的逐项检索

- 权限与领地标志表格共增加 172 个稳定行锚点，搜索记录直接指向对应行，表格正文内容不变。
- 关闭英文词干处理，保留技术名称内的英文点号；避免 `residence.randomtp`、`cmi.command.heal.others` 被当作多个普通英文词处理。
- 调整插件标签的搜索权重，避免分类名盖过具体命令和权限的匹配。
- 使用构建产物内实际的 Material 搜索 Worker，在 Node VM 中执行查询。`residence.randomtp`、`cmi.command.heal.others`、`随机传送`、`anvilbreak` 均优先命中相应页面或列表行。


## Typewriter 分类（2026-10-18）

- 新增独立 `Typewriter/` 项目，翻译官方默认 0.8.0 文档 316 页：使用文档 43 页、扩展及条目 245 页、开发文档 28 页。CMI、Residence 原文与正文文件未改动。
- 顶部为 CMI、Residence、Typewriter 三个分类；Typewriter 使用 `typewriter/`，旧项目路径继续沿用。
- Typewriter 校验覆盖 93 个完整代码块、819 处原有行内代码、命令表的权限节点及占位符；108 个资源按 SHA-256 核对，其中包含 41 段视频。
- 全站严格构建通过。372 个 HTML 文件、155,640 处站内引用、2,790 条搜索记录均已核对；Residence 的 172 个逐行搜索入口继续保留。
- 修正原始 HTML 视频的路径，使其相对于生成后的页面 URL 解析。
- 内容与站点检查分开执行；站点验证逐页提取锚点和链接，避免同时保留全部页面 DOM。
- 使用构建产物内实际的 Material 搜索 Worker 执行查询。新增 `typewriter.connect`、`Give Item Action`、`交互边界`、`过场动画`，并回归 `residence.randomtp`、`cmi.command.heal.others`、`随机传送`。
- 发现 Material 9.7.7 的中文查询分词循环未包含字符串末尾，导致“随机传送”仅以“随机”检索。构建钩子修正两个边界条件，7 个查询的首组结果均与主题相符；CI 增加实际 Worker 查询检查。
- 原文疑点和交互组件的展示差异另记于 `Typewriter/notes/source-issues.md`。未在 Minecraft 服务端测试插件或示例。
