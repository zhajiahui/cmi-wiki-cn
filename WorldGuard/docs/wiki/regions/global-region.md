---
title: 全局区域
source_url: https://worldguard.enginehub.org/en/latest/regions/global-region/
source_kind: official-wiki
translation_review: reviewed
source_version: WorldGuard Documentation 7.0 (en/latest), snapshot 5bb7595138cb
---

# 全局区域 { #global-region }

全局区域是一个特殊区域，它具有以下特点：

- 覆盖整个世界

- 优先级最低

- 有一些特殊行为

每个世界都有自己的全局区域。不过，只有通过名称 `__global__` 尝试修改它时，全局区域才会真正创建。

例如，为全局区域设置旗标，会自动创建该区域：

```text
/rg flag __global__ pvp deny
```

## 属性 { #properties }

可以把全局区域看作一个始终存在的区域。除少数例外外，其旗标的工作方式与普通区域相同。

不过，与普通区域不同，全局区域会隐式将 `passthrough` [区域旗标](flags.md)设为 *allow*。如前所述，passthrough 设为 allow 会使区域不再承担保护，因此只要没有其他区域阻止，玩家就能建造。

### 修改 `passthrough` { #changing-passthrough }

将 `passthrough` [旗标](flags.md)改为 deny 后，全局区域会像普通区域一样工作：玩家必须是其所有者或成员才能建造。由于全局区域覆盖整个世界，这意味着默认禁止在世界中建造。

全局区域的优先级最低，因此其他普通区域会覆盖它；玩家是普通区域的成员时，就能在该区域内建造。

!!! note "注意"

    passthrough 与移动无关，含义是“放行建造权限”，详见[区域旗标](flags.md)。

示例：禁止在“野外”建造

将 `passthrough` 设为 `deny`：

```text
/rg flag __global__ passthrough deny
```

### 添加成员 { #adding-members }

出于兼容旧行为的原因，向全局区域添加所有者或成员，会隐式将 `passthrough` 设为 deny。因此无需另外修改该旗标，不过仍建议显式设置。

### 非玩家关联对象 { #non-player-associables }

活塞等非玩家关联对象，通常视为其所在的所有区域的成员，或仅视为最高优先级区域的成员，取决于[配置](../config.md)中的 `use-max-priority-association`。但只要它们位于至少一个其他区域中，就不再属于全局区域。这意味着活塞无法将方块从区域内部推入受保护的全局区域。因此，全局区域始终表现得像 `use-max-priority-association` 设为 `true`。

还可以通过区域的 `nonplayer-protection-domains` 调整非玩家关联对象的成员关系。但此旗标在全局区域中的行为不同：如果某个普通区域与全局区域至少共有一个保护域，那么属于普通区域的非玩家关联对象也属于全局区域，**反过来则不成立**。

### build 旗标 { #build-flag }

将 `build` 设为 `allow` **没有作用**，也没有这样设置的必要。设为 `deny` 的效果与普通区域一样，但要注意，在任何区域中将 `build` 设为 deny，基本上都意味着*任何对象*都无法破坏或放置方块，因此活塞等机制会失效。全局区域覆盖整个世界，所以会让所有不在其他区域内的活塞失效。

!!! warning "警告"

    强烈不建议在全局区域设置 `build`。如果想默认保护整个世界，请设置 `passthrough`。

## 覆盖默认值 { #overriding-defaults }

WorldGuard 的旗标有各自的*默认值*。例如，如果没有任何区域设置 `exp-drop`，它默认允许掉落经验，即使玩家并非区域成员或所有者也一样。

如果希望将 `exp-drops` 设为 `deny`，并只影响非成员，在全局区域设置是无效的。例如，你可能会尝试 `/rg flag __global__ exp-drop -g nonmembers deny`，但这**不会**达到预期。这里的非成员指的是*全局区域*的非成员。因此，如果创建一个地块区域，其成员也会被禁止掉落经验，因为他们并非全局区域的成员。记住，全局区域优先级虽低，但普通区域并不继承它，所以旗标不会按继承关系向下传递。

这种情况下，建议按[优先级与继承](priorities.md)中的说明创建“模板区域”。
