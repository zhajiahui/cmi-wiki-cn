# 官方非 API Wiki 核对记录

快照日期：2026-10-19（Asia/Taipei）。

已译 5 页；候选 16 项，逐项状态见 `sources/wiki-coverage.json`。

- 完整枚举官方文档仓库的 13 个页面文件：4 篇非 API 文档、8 篇 SDK/API 参考、1 个 404 模板；另收录官方项目 README。

- 前置知识和嵌入依赖的取舍不是接口参考，均全文翻译；FAQ 的 NoClassDefFoundError 排错也完整保留。

- FAQ 说不应嵌入 API，随后又将嵌入依赖列为找不到类的解决方案，并有 TODO；原文矛盾和未完成项保留。

- Tweaking PacketEvents 是 PacketEventsSettings Java API 设置参考，不是独立 YAML 配置手册，明确按 SDK 接口排除。

- README 的旧 development-setup 地址实测跳转至 introduction/development-setup/，没有记作失效。

原文按 UTF-8、统一 LF 归档，manifest 保存原文 SHA-256。代码块、命令、权限、数值、表格及可获取图片按来源核对；本批只做文档与本地文件检查，尚未进行游戏、服务端或线上部署测试。
