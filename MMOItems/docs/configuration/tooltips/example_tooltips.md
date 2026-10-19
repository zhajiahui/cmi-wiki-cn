---
title: tooltips/example_tooltips.yml
source_kind: imported-configuration
translation_review: reviewed
source_file: tooltips/example_tooltips.yml
source_version: 6.10.1-SNAPSHOT
---

# tooltips/example_tooltips.yml

文件：`tooltips/example_tooltips.yml`。版本：`6.10.1-SNAPSHOT`。

随包配置。

## `copper` { #copper }

```yaml title="tooltips/example_tooltips.yml · copper"
copper:
  top:    "{-41sp}\u4076{-166sp}"
  middle: "{-41sp}\u4077{-166sp}"
  bottom: "{-41sp}\u4078"
  center_top:
    display_name: true
    span: 161
    default_char_size: 5
    char_size: [f4, i1, k4, l2, t3, I3, "'1", ' 3', ',1', '(3', ')3']
    regex: "[a-zA-Z0-9 ',()+]"
```

## `silver` { #silver }

```yaml title="tooltips/example_tooltips.yml · silver"
silver:
  top:    "{-41sp}\u4073{-166sp}"
  middle: "{-41sp}\u4074{-166sp}"
  bottom: "{-41sp}\u4075"
  center_top:
    display_name: true
    span: 161
    default_char_size: 5
    char_size: [f4, i1, k4, l2, t3, I3, "'1", ' 3', ',1', '(3', ')3']
    regex: "[a-zA-Z0-9 ',()+]"
```

## `gold` { #gold }

```yaml title="tooltips/example_tooltips.yml · gold"
gold:
  top:    "{-41sp}\u4070{-166sp}"
  middle: "{-41sp}\u4071{-166sp}"
  bottom: "{-41sp}\u4072"
  lore_header:
    - '&6{tier} {type}'
  center_top:
    display_name: true
    span: 161
    default_char_size: 5
    lore_lines: 1
    char_size: [f4, i1, k4, l2, t3, I3, "'1", ' 3', ',1', '(3', ')3']
    regex: "[a-zA-Z0-9 ',()+]"
```
