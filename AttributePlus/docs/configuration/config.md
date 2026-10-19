---
title: config.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: config.yml
source_version: 3.3.3.6
---

# config.yml

文件：`config.yml`。版本：`3.3.3.6`。

主配置。

连接信息或服务器标识已替换为示例值，使用时填写自己的信息。

## `player-attribute-init-delay` { #player-attribute-init-delay }

```yaml title="config.yml · player-attribute-init-delay"
#玩家登录时属性初始化延迟(20=1秒)
#初始化时会同步生命&刷新玩家属性,并触发 AttrPlayerInitializeEvent 玩家初始化事件(3.3.1.2)
player-attribute-init-delay: 50
```

## `player-original-health-clear` { #player-original-health-clear }

```yaml title="config.yml · player-original-health-clear"
#部分服务器可能会出现玩家生命力异常多出20点
#具体可以使用 ap health player-name 来查看一个玩家身上的生命数据来源
#开启后每次更新玩家生命力时会检测是否存在非 AttributePlus 所增加的生命力并清除
player-original-health-clear: false
```

## `attribute-custom-formula` { #attribute-custom-formula }

```yaml title="config.yml · attribute-custom-formula"
#属性自定义计算公式(关闭后 attribute.yml 中 formula 将失效)
attribute-custom-formula: true
```

## `async-handle-task` { #async-handle-task }

```yaml title="config.yml · async-handle-task"
#异步处理API任务
#高版本因为某些缘故无法使用异步操作一些内容，所以需要关闭
async-handle-task: true
```

## `check-packets` { #check-packets }

```yaml title="config.yml · check-packets"
#异常数据包检测
check-packets:
  #快速关闭
  fast-close: true
  #快速切换
  fast-toggle: true
  #快速交互
  fast-interact: true
```

## `database-store-module` { #database-store-module }

```yaml title="config.yml · database-store-module"
#储存模块(关闭后持久化属性、自定义读取格式 cache-placeholder 变量数据储存将失效)
database-store-module: true
```

## `sql` { #sql }

```yaml title="config.yml · sql"
#数据储存设置
#用于储存玩家离线时的生命力并在登录服务器时恢复
#修复部分服务器玩家满血退出重登不满血问题
sql:
  #关闭则将数据储存至本地
  enable: false
  host: "HOST"
  port: 3306
  user: "USERNAME"
  password: "PASSWORD"
  database: "DATABASE"
```
