---
title: 前缀与后缀叠加
source_url: https://luckperms.net/wiki/Prefix-&-Suffix-Stacking
source_kind: official-wiki
translation_review: reviewed
source_version: fc2919c3d5e6bfba82af31f9930273b00f08ddbf
---

<a id="what-does-it-do"></a>
### 有什么作用？
“元数据叠加”功能可以在聊天中的玩家用户名前后，显示多个前缀或后缀。

仍然需要安装聊天格式插件。

<a id="how-does-it-work"></a>
### 如何工作？
聊天格式插件请求玩家的前缀或后缀时，LuckPerms 不必只返回权重最高的那个，而是可以按一组规则，将多个前缀或后缀组合起来。

默认设置如下：
```yml
meta-formatting:
  prefix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
  suffix:
    format:
      - "highest"
    duplicates: first-only
    start-spacer: ""
    middle-spacer: " "
    end-spacer: ""
```

这些设置的含义很简单：请求前缀或后缀时，返回权重最高的那个。

<a id="how-do-i-add-other-elements"></a>
### 如何添加其他元素？
可以使用以下元素。

| 元素 | 说明 |
|---------|-------------|
| `highest` | 从玩家自身拥有及继承到的所有值中，选择权重最高的值。 |
| `lowest` | 与上项相同，但选择权重最低的值。 |
| `highest_own` | 选择权重最高的值，但不接受任何继承到的值。 |
| `lowest_own` | 与上项相同，但选择权重最低的值。 |
| `highest_inherited` | 选择权重最高的值，但只接受继承到的值。 |
| `lowest_inherited` | 与上项相同，但选择权重最低的值。 |
| `highest_on_track_<track>` | 选择权重最高的值，但该值必须继承自指定晋升路线中的权限组。 |
| `lowest_on_track_<track>` | 与上项相同，但选择权重最低的值。 |
| `highest_not_on_track_<track>` | 选择权重最高的值，但该值必须继承自不在指定晋升路线中的权限组。 |
| `lowest_not_on_track_<track>` | 与上项相同，但选择权重最低的值。 |
| `highest_from_group_<group>` | 选择权重最高的值，但该值必须继承自指定权限组。 |
| `lowest_from_group_<group>` | 与上项相同，但选择权重最低的值。 |
| `highest_not_from_group_<group>` | 选择权重最高的值，但该值不得继承自指定权限组。 |
| `lowest_not_from_group_<group>` | 与上项相同，但选择权重最低的值。 |

<a id="duplicate-settings"></a>
### 重复值设置
| 元素 | 说明 |
|---------|-------------|
| `first-only` | 只保留重复值中的第一个 |
| `last-only` | 只保留重复值中的最后一个 |
| `retain-all` | 保留所有重复值 |
| `none` | 不允许任何重复值 |

<a id="an-example"></a>
### 示例
例如，在监狱服中，可能有 3 类权限组：游戏进度等级、用户的赞助权限组，以及管理人员权限组。

如果用户同时属于这 3 类权限组，我希望三个前缀全部显示。例如：   
`[Mine C] [Donor] [Admin] Luck: hi!`.

但如果用户没有管理人员权限组，我希望显示：   
`[Mine C] [Donor] Luck: hi`.

叠加系统可以实现这些效果。需要将叠加中的每个“元素”都添加到 format 部分。

```yml
prefix:
  format:
    - "highest_on_track_prison"
    - "highest_on_track_donor"
    - "highest_on_track_staff"
  duplicates: first-only
  start-spacer: ""
  middle-spacer: " "
  end-spacer: ""
```

如果玩家没有任何符合某个元素条件的值，该元素就不会加入叠加结果。

起始、中间和末尾间隔符可以控制各元素之间的分隔方式。例如：

  ```yml
  prefix:
    format:
      - "highest_on_track_prison"
      - "highest_on_track_donor"
      - "highest_on_track_staff"
    duplicates: first-only
    start-spacer: "★ "
    middle-spacer: " | "
    end-spacer: " "
  ```

……会得到以下结果：   
`★ [Mine C] | [Donor] | [Admin] Luck: hi`.

可以根据所用聊天格式插件调整这些值，因为聊天格式插件也可能提供类似选项。
