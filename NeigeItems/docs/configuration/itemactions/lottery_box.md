---
title: ItemActions/lottery_box.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: ItemActions/lottery_box.yml
source_version: 1.22.0
---

# ItemActions/lottery_box.yml

文件：`ItemActions/lottery_box.yml`。版本：`1.22.0`。

随包配置。

## `TARGET` { #target }

```yaml title="ItemActions/lottery_box.yml · TARGET"
TARGET:
  beclicked:
    # 其他点击也会触发 beclicked，设为 0 避免冷却妨碍左键移动。
    cooldown: 0
    consume:
      pre: |-
        js: (function () {
          global.openAmount = "0";
          var clickedInventory = event.getClickedInventory();
          if (clickedInventory == null || !clickedInventory.equals(player.getInventory()) || !event.isRightClick()) {
            // beclicked 会默认取消点击；其他操作恢复正常，以便左键移动箱子。
            event.setCancelled(false);
            return;
          }
          global.openAmount = event.isShiftClick() ? "16" : "1";
        })()
      condition: 'Number(global.openAmount) > 0'
      amount: '<openAmount>'
      deny:
        - condition: 'Number(global.openAmount) > 0'
          actions:
            - 'tell: &c同一格内至少需要 <openAmount> 个抽奖箱，本次未开启。'
    # 同步执行扣除后的抽奖及发奖。
    sync:
      - |-
        js: (function () {
          var amount = Number(global.openAmount);
          var materials = [Material.DIAMOND, Material.GOLD_INGOT, Material.IRON_INGOT];
          var names = ["钻石", "金锭", "铁锭"];
          var counts = [0, 0, 0];
          var random = ThreadLocalRandom.current();
          // 每个箱子独立抽取一次；16 连开可以重复抽中同一种奖励。
          for (var i = 0; i < amount; i++) {
            counts[random.nextInt(materials.length)]++;
          }
          var inventory = player.getInventory();
          var summary = [];
          var overflow = false;
          for (var j = 0; j < materials.length; j++) {
            if (counts[j] <= 0) continue;
            // 直接构造原版物品，不附加 NI 物品 ID。
            var leftovers = inventory.addItem(new ItemStack(materials[j], counts[j]));
            var iterator = leftovers.values().iterator();
            while (iterator.hasNext()) {
              player.getWorld().dropItemNaturally(player.getLocation(), iterator.next());
              overflow = true;
            }
            summary.push(names[j] + " ×" + counts[j]);
          }
          player.sendMessage("§a已开启 §e" + amount + " §a个抽奖箱：§f" + summary.join("§7，§f"));
          if (overflow) {
            player.sendMessage("§e背包已满，放不下的奖励已掉落在脚边。");
          }
        })()
```
