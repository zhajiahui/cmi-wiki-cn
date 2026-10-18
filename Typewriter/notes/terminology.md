# 术语

| 原文 | 本项目译法 | 说明 |
| --- | --- | --- |
| Typewriter | Typewriter | 插件名称不翻译 |
| Entry | 条目 | 对话、事件、动作、事实等的统称 |
| Sequence | 序列 | 依次触发的交互内容 |
| Manifest | 呈现 | 与按顺序执行的 Sequence 区分；保留英文类型名供面板对照 |
| Audience | 受众 | 符合条目条件的一组玩家 |
| Fact | 事实 | 原文说明其本质为数值变量，保持全项目统一译法 |
| Criteria | 条件 | 决定条目是否执行 |
| Modifier | 修改器 | 触发时修改事实的值 |
| Trigger | 触发、后续触发 | 按语境区分动作与字段名称 |
| Cinematic | 过场动画 | 包括镜头、实体及对话片段 |
| Segment | 片段 | 过场动画中的时间区间 |
| Spoken Dialogue | 逐字对话 | 动画显示的对话文本，不译为语音 |
| Interaction Bound | 交互边界 | 条件被违反时中断交互，或阻止违反条件的操作 |
| Inspector | 属性面板 | 用于编辑条目字段 |
| Artifact | 文件产物 | 扩展生成的资源，保留 ArtifactEntry、artifactId 等标识符 |
| Asset | 资源 | 外部文件等资源 |
| tick | tick | 保留游戏时间单位；按原文给定换算值表达 |
| Annotation | 注解 | Kotlin API 语境；代码注释另行区分 |
| Interface | 接口 | 开发 API 中的接口；用户界面仍译为界面 |
| Messenger | Messenger | 与 DialogueMessenger 等接口名称对应 |

页面和字段的具体译名还记录在 `titles.json` 和 `terminology.tsv` 中。代码、路径、权限、占位符与实际配置键不随说明文字翻译。