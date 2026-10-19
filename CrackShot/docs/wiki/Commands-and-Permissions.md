---
title: "命令与权限"
source_url: "https://github.com/Shampaggon/CrackShot/wiki/Commands-and-Permissions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "Shampaggon/CrackShot Wiki @ d132397f9b52a5274dba87443ad0ebcde369a0a0；2026-10-19 快照；与 0.98.13-x6 的对应关系未确认"
---

<a id="aliases"></a>

## **░ 命令别名**
    /shot, /cra, /cs

<a id="commands"></a>

## **░ 命令**
    /shot                                   - 显示插件信息。
    /shot list all                          - 列出所有武器，不包含隐藏武器。
    /shot list <page>                       - 按页码列出武器，不包含隐藏武器。
    /shot config reload                     - 重载配置。
    /shot give <user> <weapon> <amount>     - 给予其他玩家一把武器，可以指定数量。
    /shot get <weapon> <amount>             - 获取一把武器，可以指定数量。
    /shot reload                            - 装填手中的武器。

<a id="permissions"></a>

## **░ 权限**
默认情况下，用户可以合成、购买和使用所有武器。

    crackshot.reloadplugin      - 重载插件的权限。
    crackshot.list              - 列出武器的权限。
    crackshot.give.all          - 给予玩家任意武器的权限。
    crackshot.get.all           - 获取任意武器的权限。
    crackshot.use.all           - 使用任意武器的权限。（默认授予）
    crackshot.craft.all         - 合成任意武器的权限。（默认授予）
    crackshot.buy.all           - 购买任意武器的权限。（默认授予）
    crackshot.shops.all         - 创建和拆除任意武器商店的权限。
    crackshot.bypass.all        - 绕过任意武器区域检查的权限。

    crackshot.give.<weapon>     - 给予玩家指定武器的权限。
    crackshot.get.<weapon>      - 获取指定武器的权限。
    crackshot.use.<weapon>      - 使用指定武器的权限。
    crackshot.craft.<weapon>    - 合成指定武器的权限。
    crackshot.buy.<weapon>      - 合成指定武器的权限。
    crackshot.shops.<weapon>    - 创建和拆除指定武器商店的权限。
    crackshot.bypass.<weapon>   - 绕过指定武器区域检查的权限。
