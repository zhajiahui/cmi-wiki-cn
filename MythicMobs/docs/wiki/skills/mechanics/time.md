---
title: Time
source_url: https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/time
source_kind: official-wiki
translation_review: reviewed
source_version: 2026-10-19官方在线Wiki
---

# Time {#time}

## 说明 {#description}

设定世界时间。根据所使用的属性，时间的变化可以是绝对的，也可以是相对于目标玩家的。

time 机制必须同步执行才能生效，即设置 sync=  true  ;。

## 属性 {#attributes}

| 参数 | 别名 | 说明 | 默认值 |
| --- | --- | --- | --- |
| mode | m | 时间机制使用的模式，可设为 ADD/SET/RESET | ADD |
| amount | ticks, t, amt, time | 要改变的时间刻数 | 20 |
| personal |  | 设置修改全局时间还是玩家客户端时间 | false |
| relative |  | 设置是否让玩家的时间按偏移量与所在世界的时间保持同步 | true |

#### Mode 属性 {#mode-attribute}

mode 属性可以取的不同值都有不同的效果

- **`ADD`** - 设置带有偏移量的世界当前时间
- **`SET`** - 设置世界的当前时间
- **`RESET`** - 重新同步目标的世界时间与服务器世界时间（如果尚未同步）

## 示例 {#examples}

```yaml
# Mob File
ExampleMob:
  Type: ZOMBIE
  Skills:
  - sudoskill{s=MidnightAura} @PIR{r=30} ~onTimer:20
```

```yaml
# Skills File
MidnightAura:
  Skills:
  - aura{auraName=midnight;i=1;ms=1;rd=true;
    onTick=[
      - time{mode=SET;amount=18000;personal=true;relative=false;sync=true} @self
    ];
    onEnd=[
      - time{mode=RESET;sync=true} @self
    ]} @self
```

## 别名 {#aliases}

- setTime
