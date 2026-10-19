---
title: templates/citizens/templates.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: templates/citizens/templates.yml
source_version: 2.0.43-SNAPSHOT (build 4210)
---

# templates/citizens/templates.yml

文件：`templates/citizens/templates.yml`。版本：`2.0.43-SNAPSHOT (build 4210)`。

随包配置。

## `example` { #example }

```yaml title="templates/citizens/templates.yml · example"
example:
  commands:
    on_template_apply:
      - say --range 15 Hello!
      - npc command add say Hello again!
```

## `behavior_tree_example` { #behavior_tree_example }

```yaml title="templates/citizens/templates.yml · behavior_tree_example"
behavior_tree_example:
  traits:
    -
      name: behavior
      tree:
        sequence:
          - if `npc.spawned`:
              - cooldown patrol 10s
              - loop `memory.get('patrol_count', 0) < 3`:
                - print Patrolling area `memory.get('patrol_count', 0)`
                - walkto `npc.x + 5` `npc.y` `npc.z`
                - wait 2s
                - walkto `npc.x - 5` `npc.y` `npc.z`
                - set patrol_count `memory.get('patrol_count', 0) + 1`
              - print Patrol complete!
              - forget patrol_count
```
