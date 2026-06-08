---
name: Flex Layout System
description: A set of attribute-selector utility classes for flexbox layouts with responsive breakpoint support.
---

# Flex Layout System

The `flex.scss` file generates flexbox utility classes using HTML attribute selectors. All flex classes automatically set `display: flex`.

## Syntax

### Core Layout: `fx-{direction}-{justify}-{align}`

Combines direction, justify-content, and align-items into one attribute.

```html
<div fx-row-start-center>...</div>
<div fx-column-between-stretch>...</div>
```

| Segment | Options |
| :--- | :--- |
| **Direction** | `row`, `column`, `row-reverse`, `column-reverse` |
| **Justify** | `start`, `end`, `center`, `between`, `around` |
| **Align** | `start`, `end`, `center`, `stretch` |

### Responsive: `fx-{direction}-{breakpoint}-{justify}-{align}`

Same as above but applies only at a minimum breakpoint width.

```html
<!-- Column on mobile, row on tablet+ -->
<div fx-column-start-center fx-row-sm-between-center>...</div>
```

| Breakpoint | Min Width |
| :--- | :--- |
| `sm` | 768px |
| `md` | 1280px |
| `lg` | 1920px |

### Gap: `fx-gap-{size}`

```html
<div fx-row-start-center fx-gap-8>...</div>
```

Sizes: `0`, `2`, `4`, `6`, `8`, `10`, `12`, `14`, `16`, `20`, `24`, `32` (px)

### Grid Sizing: `fx-{columns}` / `fx-{breakpoint}-{columns}`

12-column grid system.

```html
<div fx-row-start-stretch fx-gap-16>
  <div fx-6>Half width</div>
  <div fx-3>Quarter width</div>
  <div fx-3>Quarter width</div>
</div>

<!-- Responsive: full on mobile, half on tablet -->
<div fx-12 fx-sm-6>...</div>
```

### Order: `fx-order-{n}`

```html
<div fx-order-2>Appears second</div>
```

Values: `1` through `12`.

### Utility Attributes

| Attribute | Effect |
| :--- | :--- |
| `fx-flex` | `flex: 1 1 0%` (grow to fill) |
| `fx-flex-none` | `flex: 0 0 auto` (no grow/shrink) |
| `fx-wrap` | `flex-wrap: wrap` |
| `fx-no-wrap` | `flex-wrap: nowrap` |

## Full Example

```html
<div fx-row-between-center fx-gap-16 fx-wrap>
  <div fx-12 fx-sm-6 fx-md-4 fx-order-1>Card 1</div>
  <div fx-12 fx-sm-6 fx-md-4 fx-order-2>Card 2</div>
  <div fx-12 fx-sm-12 fx-md-4 fx-order-3>Card 3</div>
</div>
```
