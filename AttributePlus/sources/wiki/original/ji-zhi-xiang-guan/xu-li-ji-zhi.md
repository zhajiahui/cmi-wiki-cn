> For the complete documentation index, see [llms.txt](https://ersha.gitbook.io/attributeplus-pro/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://ersha.gitbook.io/attributeplus-pro/ji-zhi-xiang-guan/xu-li-ji-zhi.md).

# 蓄力机制

1.9 +  (可能1.8也支持，可能就只支持弓箭)

## 蓄力说明

在 **1.9+** 剑的攻击只要攻击间隔足够够久，就会触发一次 **横扫攻击** 这就相当于 **蓄力满** 了，所以可以打出满额的伤害，如果你攻击态度过快，你的伤害也会越来越低。\
同理，弓箭也是，你拉弓需要蓄力到底才会打出满额的伤害。

## 机制属性

| 属性名  | 说明                    |
| ---- | --------------------- |
| 蓄力加成 | 增加蓄力强度，如果 100 则蓄力一直为满 |
| 蓄力干扰 | 减少对方蓄力强度              |

## 机制配置

```yaml
#支持版本: 1.9+
#蓄力伤害机制(近战&远程都会受到影响)
accumulateDamage: false
```

![旧版本效果图](https://1999935025-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MSI3dcJ6z5A8zyVhqo9%2F-MSRCm5IlFYv8IJ1ZBxK%2F-MSRD7jFhRIkpeDZt1ZD%2Fd02b789178dedf8e6f1b91cbcbf51d23_assets%252F-MBoLfs8TQZgHdsr3gnG%252F-MFZ1GjFEhssZ9ZlSEbw%252F-MFZ2Tc2Lp484oKWzsV7%252F%25E8%2593%2584%25E5%258A%259B%25E6%259C%25BA%25E5%2588%25B6_alt%3Dmedia%26token%3D20bc6f5d-da40-4002-9457-46044df5d032.gif?alt=media\&token=5732dabd-2a02-4367-85ba-3fcab27ea2df)
