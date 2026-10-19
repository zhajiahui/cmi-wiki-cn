# CrackShot Wiki 翻译收录记录

快照：2026-10-19。官方 Wiki Git 提交：d132397f9b52a5274dba87443ad0ebcde369a0a0。随包版本：0.98.13-x6。上游 Wiki 与 -x6 分支的对应关系仍未确认，未按随包版本改写上游机制。

## 完整目录

官方 GitHub Wiki 网页目录与 Wiki Git 仓库文件清单交叉核对，共 10 页：Home、Installation、Commands and Permissions、The Complete Guide to CrackShot、Default Weapons、Frequently Asked Questions、List of Accepted Mobs、List of Accepted Sounds、List of Modules，以及 Hooking into CrackShot。

前 9 页均已全文翻译或逐项保留配置/标识列表。Hooking into CrackShot 是 CSUtility 函数、参数、返回值及 Bukkit 事件接口参考，标为 excluded_api；原文完整归档。FAQ 中介绍与其他插件配合的四种方法均保留，包括指向该接口参考的原有链接。

《完整指南》原文 1,750 行、98,533 字符，覆盖全部模块、节点、例子、限制和警告。没有以概览替代正文。sources/wiki/translation/guide-lines.json 记录逐原文行的人工全文翻译，未改动的行保留原配置结构。默认武器页全部 YAML、声音和生物值列表均完整收录。

## 原文疑点与格式修复

- Commands and Permissions 的 crackshot.buy.<weapon> 说明原文为 “Permission to craft a specific weapon.”，与节点名及 buy.all 说明冲突；正文忠实译为“合成指定武器”，未静默改成购买权限。
- 指南 Item_Lore 的例子写成 Item_Name，原样保留。
- 指南创建商店处使用 crackshot.store.<weapon>/all，而命令权限页使用 crackshot.shops.*；两处原样保留，不替作者判断哪个适用于 -x6。
- Sounds_Trigger 最后一项标签为 remote，说明却指向 item bomb，原样保留。
- 指南目录的 Weapons folder 链接原本指向 #modules，保留该原始跳转；实际武器文件夹章节的 #folder 锚点同样保留。
- 声音与生物列表的原文把首个值紧接在三个反引号后，且缺少结束围栏。渲染页补成有效 text 代码块，并将 AMBIENT_CAVE、Bat 作为列表第一项保留；原文归档不改。
- 默认武器与指南中的数字 ID、旧材料名、旧版接口名称、配置键及示例参数均原样保留，不根据其他版本替换。

## 图片、链接与核对

指南 4 张木牌商店/合成截图已下载原生 PNG，未缩放。来源和哈希见 sources/wiki/assets-manifest.json。站内链接指向对应译文，翻译标题保留原文锚点，接口参考链接仍指向官方。

本次仅进行文档、来源、受保护字符串、代码结构、导航、图片及本地链接核对；未进行游戏内测试。未修改首页、configuration、mkdocs 或 Site；未提交或发布。

## 本次校验结果

2026-10-19 本地核对通过，报告为 sources/wiki/validation/report.json。核对 9 页，63 个代码块、411 个受保护行内代码项、4 个原生资源文件；来源 SHA-256、frontmatter、manifest/nav/coverage 一致性、本地链接与锚点检查均无错误。unavailable 是来源获取状态，不会因静态校验通过而改为已取得。
