# 原文疑点与展示差异

本项目按官网默认 0.8.0 文档翻译。以下问题单独记录，未擅自改动原文的示例逻辑。

## YAML `|2`

- 原文：[Snippets](https://docs.typewritermc.com/docs/helpful-features/snippets)。原文将 `|2` 解释为多行字符串末尾带 2 个换行，并建议不需要时删除 `2`。
- 已对照 [YAML 1.2.2：Block Indentation Indicator](https://yaml.org/spec/1.2.2/#8111-block-indentation-indicator)。`2` 是显式缩进指示符；末尾换行由 chomping indicator 等规则处理，并非换行数量。
- 正文按原文译出，示例保持原样。建议确认修订范围后，另行更正该段说明。

## 原文路径与示例名称

- Snippets 原文写作 `plugin/Typewriter/snippets.yml`，与安装页使用的 `plugins/Typewriter/` 写法不一致。当前保留原文路径。
- 击杀僵尸教程同时出现 `Killed Zombies Fact` 和 `Kill Zombie Fact`。保留各处原名及附带 JSON，未静默统一示例名称。
- 原文的 Questing 目录仍标注“正在重写”，部分目标和教程标为 Soon、Being Written。译为“待补充”或“正在编写”，不补写原文没有的教程。
- 部分 NPC 适配器被标注为不再支持或弃用；这些提示仍然保留。
- 开发接口介绍中的 `statful` 按同页上下文的 stateful 概念译为“有状态”，代码与接口名称保持原样。

## 网页组件

- 字段标签与公共说明来自原站生成的网页，同时保留组件源码，避免只抽取 MDX 而漏掉内容。
- 原站播放器的视频已从固定提交的资源中恢复，提供本地播放。
- EntryDisplay 的示例页提供原始 JSON 文件，便于阅读或导入，不修改示例数据。
- StateFlow 展开为状态、事实、说明、全部转换的表格；保留原有事实表达式和返回分支。
- StatusEditor 按原组件的状态判断制作中文显示：值小于等于 0 时未激活，等于 5 时完成，其余为进行中。
- Rive 交互图保留对应原文章节入口与 `.riv` 原始文件，不将截图代替交互图。

以上是原文核对与文档展示处理，不代表已在 Minecraft 服务端验证插件功能。