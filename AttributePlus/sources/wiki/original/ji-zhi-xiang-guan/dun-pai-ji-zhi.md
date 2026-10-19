> For the complete documentation index, see [llms.txt](https://ersha.gitbook.io/attributeplus-pro/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://ersha.gitbook.io/attributeplus-pro/ji-zhi-xiang-guan/dun-pai-ji-zhi.md).

# 盾牌机制

1.9 +

## 说明

盾牌机制有两种处理方式，一种是**有冷却**，一种是**无冷却**\
\
**有冷却模式:** 每次冷却完毕，下次盾牌格挡是必定完全格挡此次伤害，冷却期间不会完全格挡伤害，但 盾牌格挡 属性会生效，可百分比格挡伤害。\
**无冷却模式:** 该模式下只能使用 盾牌格挡 属性来增加格挡伤害，如果没有这个属性则无论如何都会受到满额伤害。

## 机制属性

| 属性名  | 说明           |
| ---- | ------------ |
| 破盾几率 | 一定几率无视对方盾牌格挡 |
| 盾牌格挡 | 百分比格挡此次伤害    |

## 机制配置

```yaml
#支持版本: 1.9+
#盾牌格挡机制
shield:
  enable: true
  #right 则为无冷却模式
  right: false
  #right 为 false 时启用盾牌格挡冷却机制
  cd: 10
```

![旧版本效果图](https://1999935025-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MSI3dcJ6z5A8zyVhqo9%2F-MSRDGw5b7fq-_4NaQiM%2F-MSRF_vMQ_1tMrdqbmsA%2F58b331cd90239909d81a73c716352cd1_assets%252F-MBoLfs8TQZgHdsr3gnG%252F-MDcu57TFqCCZPZPQ5xA%252F-MDcu8C8XD0hKJOPFtj0%252F%25E7%259B%25BE%25E7%2589%258C%25E6%25A0%25BC%25E6%258C%25A1%25E6%259C%25BA%25E5%2588%25B6_alt%3Dmedia%26token%3D8ccb47d3-5f16-4b82-9630-93affa165871.gif?alt=media\&token=7b4ba449-6419-4c6a-8e41-cbc8e5d01b4b)
