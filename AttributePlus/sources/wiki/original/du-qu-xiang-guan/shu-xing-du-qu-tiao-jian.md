> For the complete documentation index, see [llms.txt](https://ersha.gitbook.io/attributeplus-pro/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://ersha.gitbook.io/attributeplus-pro/du-qu-xiang-guan/shu-xing-du-qu-tiao-jian.md).

# 属性内嵌条件格式

新版特色 / 3.1.9 版本起

## 内嵌**读取条件**

自带的属性读取格式有一个额外的 **读取条件** 当 **满足该条件时属性才会被读取**\
你也可以为你服务器开发更多不同的**内嵌条件 (**[**开发文档**](https://ersha.gitbook.io/attributeplus-pro/kai-fa-wen-dang/descriptionlinecondition)**)**\
\
**格式为** "<属性内容> **/** **<条件>**"\
条件必须写在 / 右边,否则不生效<br>

| 类型       | 说明             |
| -------- | -------------- |
| Lv.<值>   | 使用者等级必须满足才会读取  |
| Gm.<权限名> | 使用者必须拥有该权限才会读取 |

具体用法，你只需要在物品属性Lore上加 **对应类型的读取条件** 即可，例如 **"物理伤害: 1000 / Lv.1000"** 那么装备使用者等级必须大于等于 1000 该属性条目才会生效

![](https://1999935025-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MSI3dcJ6z5A8zyVhqo9%2F-MSM5SjdLS5p1AhKw_4N%2F-MSMAc25WHG4OHnSCUQN%2FPN~MY%7DQJOSJ%5D%40MB%7D4%5D_~N%7DN.png?alt=media\&token=cb7b1818-441a-4545-975a-23250ac0c36f)

![](https://1999935025-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MSI3dcJ6z5A8zyVhqo9%2F-MSM5SjdLS5p1AhKw_4N%2F-MSMAgEs8qXfF-PmjPRe%2FV%5D5RM0PBI06KUWVU~Q%7B_8%60V.png?alt=media\&token=2dfe7aee-8ee2-4682-8d21-42bf5e064ab4)

![](https://1999935025-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MSI3dcJ6z5A8zyVhqo9%2F-MSM5SjdLS5p1AhKw_4N%2F-MSMAjGVk8TzDLMHR6Y4%2FXH%40E1BZ%25%60%7BTS%25XQ24HP%5B%5BD0.png?alt=media\&token=0a40a1d5-3c74-4331-89eb-d12941f11454)
