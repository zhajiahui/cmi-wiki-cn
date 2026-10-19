---
title: script/example.js
source_kind: imported-configuration
translation_review: reviewed
source_file: script/example.js
source_version: 3.3.3.6
---

# script/example.js

文件：`script/example.js`。版本：`3.3.3.6`。

随包脚本。

```javascript title="script/example.js"
var priority = 103
var combatPower = 5.0
var attributeName = "测试脚本属性"
var attributeType = "ATTACK"
var placeholder = "testAttribute"

function onLoad(attr){
	attr.setMessages(Arrays.asList(
		"测试属性伤害 {testAttribute}",
		"受到测试属性 {testAttribute}"
	))
	return attr
}

/* 属性脚本教程: https://ersha.gitbook.io/attributeplus-pro/shu-xing-jiao-ben */
function runAttack(attr, attacker, entity, handle) {
	var damage = 0.0
	/* 判断实体类型 */
	/* https://bukkit.windit.net/javadoc/org/bukkit/entity/EntityType.html */
	if (Utils.isType(attacker, Arrays.asList(EntityType.PLAYER))){
		var damage = attr.getRandomValue(attacker, handle)
		attr.addDamage(attacker, damage, handle)
		if (Utils.hasCooling("测试冷却组", attacker, 3.0)) {
			//触发
		} else {
			//冷却中
		}
	}
	return damage > 0.0
}
```
