# WorldGuard Wiki 翻译备注

## 固定快照与范围

- 官方文档版本：7.0，来源 https://worldguard.enginehub.org/en/latest/。
- 快照时间：2026-10-19T15:14:29.129632+00:00。
- 快照标识：`5bb7595138cb07a21a98f5925b9cce145651f90af6af38a1da4da2324a33df5c`。
- 文档版本不等同于单个插件 JAR 的补丁版本；本次按已保存的官方文档快照完整翻译。
- 全部候选 39 页：已译 26 页，逐页排除 API 12 页，不可用 1 页。
- API 排除项的标题、URL、原文源码及具体理由均保留于覆盖清单；非 API 开发内容和进阶章节保留。

## 不可用页面

- https://worldguard.enginehub.org/en/latest/search/：HTTPSConnectionPool(host='worldguard.enginehub.org', port=443): Max retries exceeded with url: /en/latest/search/ (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1010)')))

## 原文中保留的差异

- 常见场景页面写 `exit-overide=true`，旗标列表使用 `exit-override`。译文保留各处原标识，没有改动命令。
- 全局区域页面的一处说明写 `exp-drops`，相邻命令及旗标列表写 `exp-drop`；两处均按原文保留。
- 区域命令页 Add Owner 示例的说明写 members，实际示例使用 addowner；译文保留“成员”，未修改命令。
- 区域命令页 Parent 小节的 “unset a parent priority” 根据该段操作对象译为“取消父区域设置”；原文和命令完整保存供核对。
- 存储驱动页将 YAML 文件名写作 `region.yml`，译文保留该写法。
- 配置页对白名单模式的简述写“仅允许黑名单中被禁止的操作”，黑名单专页明确要求 `allow` 动作；两处原文含义均保留，未擅自统一。
- 原文颜色代码包含反引号，使用 HTML code 与字符实体保留原字符，防止被误解析成 Markdown 分隔符。

## 交付校验

- 英文 Markdown 原文按 UTF-8、LF 保存，并逐页记录 SHA-256。
- 译文完整保留代码块、inline code、命令权限占位符、表格行数、表格内段落和列表及显式标题锚点。
- 图片保存原始字节，来源、文件路径和 SHA-256 见 `sources/wiki/assets-manifest.json`。
- API 与站外链接保留官方地址，已有本地译文的链接改为相对路径。
- 未修改共享 Site、现有介绍页、configuration 或 mkdocs，未提交、未发布。
- 本次校验属于文档静态校验，没有进行 Minecraft 服务端运行验证。
