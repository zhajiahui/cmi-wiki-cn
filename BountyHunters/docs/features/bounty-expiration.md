---
title: 悬赏有效期
source: https://docs.phoenixdevt.fr/bounty-hunters/features/bounty-expiration
source_snapshot: '2026-10-19'
---

# 悬赏有效期 {#⌛-bounty-expiration}

如果悬赏在一段时间内处于非活动状态，你可以选择自动删除它们。不活动的悬赏是指在一定时间内未更新（声明或增加）的悬赏。

可以在`config.yml`文件中打开此功能：

```yml
# Automatically remove bounties if they have been inactive for a long time.
# Time is the amount of time in hours before a bounty is considered
# inactive if it is not updated (either claimed or someone increases it).
# 720 hours = 30 days, 360 hours = 15 days are good values
# 
# Bounties are checked every 1min.
# Changing this option requires a reload.
inactive-bounty-removal:
  enabled: true
  time: 720
```

---

原文：[⌛ Bounty Expiration](https://docs.phoenixdevt.fr/bounty-hunters/features/bounty-expiration) · 原文归档：2026-10-19
