---
title: "RUNTIME 类型"
source_url: "https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben/shou-ba-shou-jiao-ni-xie-shu-xing-jiao-ben/runtime-lei-xing"
source_kind: "official-wiki"
translation_review: "reviewed"
source_version: "官方持续更新 Wiki；2026-10-19 快照；未固定到随包 3.3.3.6"
---

# RUNTIME 类型

属性教程

## 属性效果

每隔几秒对周围怪物造成一次伤害

```javascript
var priority = 150
var combatPower = 5.0
var attributeName = "惩戒伤害"
var attributeType = "RUNTIME"
var placeholder = "runTimeAttribute"

function onLoad(attr) {
    return attr
}

/* AttributePlus 3.1.2 版本开始才可以设置冷却 */
function run(attr, entity, handle) {
    /* 触发后冷却 10 秒 */
    if (Utils.attributeCooling(attributeName, 10, entity)) {
        var damage = Attr.getRandomValue(entity, handle)
        /* 获取实体 5 格范围内的实体 */
        var list = Utils.getNearbyEntities(entity, 5.0, 5.0, 5.0, false)
        /* 遍历 */
        for (size in list) {
            /* 造成一次伤害 */
            Utils.damageEntity(damage, list[size], entity)
        }
    }
    return false
}
```

!!! note
    怎么给属性加上冷却呢?


```javascript
/* AttributePlus 3.1.2 版本开始才可以设置冷却 */
function run(attr, entity, handle) {
    /* 触发后冷却 10 秒 */
    if (Utils.attributeCooling(attributeName, 10, entity)) {
        var damage = attr.getRandomValue(entity, handle)
        /* 获取实体 5 格范围内的实体 */
        var list = Utils.getNearbyEntities(entity, 5.0, 5.0, 5.0, false)
        /* 遍历 */
        for (size in list) {
            /* 造成一次伤害 */
            Utils.damageEntity(damage, list[size], entity)
        }
    }
    return false
}
```
