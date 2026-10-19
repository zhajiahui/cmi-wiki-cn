> For the complete documentation index, see [llms.txt](https://ersha.gitbook.io/attributeplus-pro/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/attributecomponent/attributetype.md).

# AttributeType

属性类型

| 枚举                    | 说明                         |
| --------------------- | -------------------------- |
| AttributeType.ATTACK  | 攻击时触发，需要重写 runAttack 方法    |
| AttributeType.DEFENSE | 被攻击者时触发，需要重写 runDefense 方法 |
| AttributeType.UPDATE  | 属性更新时触发，需要重写 run 方法        |
| AttributeType.RUNTIME | 每隔多少秒触发一次，需重写 run 方法       |
| AttributeType.KILLER  | 击杀目标时触发，需要重写 runKiller 方法  |
| AttributeType.CUSTOM  | 自定义属性触发器，需要重写 runCustom 方法 |
| AttributeType.OTHER   | 该类型主要为其他类型的属性提供属性值         |

**KILLER** 类型 **JavaScript** 自定义属性脚本示例：[传送门](/attributeplus-pro/kai-fa-wen-dang/api-1.md#javascript-zhong-shi-yong-ji-shu-qi-shi-li)
