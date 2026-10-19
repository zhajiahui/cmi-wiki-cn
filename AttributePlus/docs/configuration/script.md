---
title: script.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: script.yml
source_version: 3.3.3.6
---

# script.yml

文件：`script.yml`。版本：`3.3.3.6`。

随包配置。

## `scriptTools` { #scripttools }

```yaml title="script.yml · scriptTools"
#自定义脚本工具类
scriptTools:
  "Utils": "org.serverct.ersha.script.AttrScriptUtils"
  "AttributeAPI": "org.serverct.ersha.api.AttributeAPI"
  "PresetTaskAPI": "org.serverct.ersha.api.PresetTaskAPI"
  "Bukkit": "org.bukkit.Bukkit"
  "EntityType": "org.bukkit.entity.EntityType"
  "Arrays": "java.util.Arrays"
  "Data": "org.serverct.ersha.manager.data.Data"
```

## `dynamic-custom-trigger` { #dynamic-custom-trigger }

```yaml title="script.yml · dynamic-custom-trigger"
  #SkillAPI 扩展API
  #"SkillAPI": "com.sucy.skill.SkillAPI"
  #"SkillExtensionAPI": "org.serverct.ersha.listener.manager.skill.SkillExtensionAPI"


#动态注册自定义属性触发器
#注册后的触发器可用于JS写自定义脚本属性
#CUSTOM类型: https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben/shou-ba-shou-jiao-ni-xie-shu-xing-jiao-ben/update-lei-xing-1
dynamic-custom-trigger:
  #触发器名称
  #"TEST SKILL CAST":
    #事件类
    #event: "com.sucy.skill.api.event.PlayerCastSkillEvent"
    #事件触发优先级: LOWEST -> LOW -> NORMAL -> HIGH -> HIGHEST -> MONITOR
    #正常情况下 NORMAL 即可，或者 HIGH
    #priority: "HIGHEST"
    #是否在事件被其他插件取消时依旧触发
    #ignore-cancelled: false
    #获取释放者的方法名，返回的对象必须为 LivingEntity 及其子类对象
    #例如类里面的方法名为 "getPlayer()" 则填写 getPlayer
    #caster: "getPlayer"
    #获取释放目标的方法名，返回的对象必须为 LivingEntity 及其子类对象，可为空
    #target: "getTarget"
```
