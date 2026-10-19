# 官方非 API Wiki 核对记录

快照日期：2026-10-19（Asia/Taipei）。

已译 18 页；候选 20 项，逐项状态见 `sources/wiki-coverage.json`。

- 官方侧边栏之外的 Java agent 警告页已按 sitemap 和仓库补入。18 个文档目录页中，16 页翻译、2 页纯 API 排除，另加官网功能页和项目 README。

- 卡顿尖峰指南中的 `/spark profiler --only-ticks-over 150` 与命令页现行 `/spark profiler start ...` 写法不同，原样保留。

- 同一指南先以 50ms 举例，随后称降低阈值却使用 70；译文保留原值，不静默纠正。

- Java agent 页分别讨论 Java 21 和 22，未扩大到后续所有 Java 版本。

原文按 UTF-8、统一 LF 归档，manifest 保存原文 SHA-256。代码块、命令、权限、数值、表格及可获取图片按来源核对；本批只做文档与本地文件检查，尚未进行游戏、服务端或线上部署测试。
