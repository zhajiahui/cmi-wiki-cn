---
title: "事件与动作"
source_url: "https://wiki.itemsadder.com/adding-content/entities/events-and-actions"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "official-wiki snapshot 2026-10-19; master@4c214199685f4380ac0f7be0ab9f77415a033921"
---


# 事件与动作

在特定事件发生时执行动作，让实体具有更多交互。其方式与自定义物品的事件和动作类似。

后续会加入新的事件和动作。这是新功能，目前仍在开发中。

## 事件

### `attack`

自定义实体攻击其他实体时执行的动作。

### `attacked`

自定义实体被其他实体攻击时执行的动作。

### `damaged`

自定义实体受到伤害时执行的动作。

### `death`

自定义实体死亡时执行的动作。

### `interact`

玩家与自定义实体交互时执行的动作。

## 动作

### `execute_command`

执行命令。

* `command`：要执行的命令
* `as_console`：是否以控制台身份执行命令（默认为 true）
* `silent`：执行命令时是否发送消息
* `flow_success_if_message_contains`：插件无法自动识别其他插件命令的成功或失败状态，因此需要指定能帮助识别命令状态的文本。

### `summon_entity`

召唤自定义实体。

* `entity`：实体 ID
* `max_per_chunk`：当前区块中允许生成的此类实体数量上限

### `script`

执行[脚本](https://itemsadder.devs.beer/plugin-usage/scripting)。

* `name`：要执行的脚本名称。例如 `example:my_script`

### 通用动作属性

#### `delay`

执行此动作前的延迟。

#### `flow`

用于改变此事件配置节中动作执行流程的高级选项。\
详情见 [VSCode 扩展](../../plugin-usage/beginners/files-editor.md)。

#### `permission`

执行此动作所需的权限。

