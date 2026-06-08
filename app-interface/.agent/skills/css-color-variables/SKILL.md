---
name: CSS Color Variables Consistency
description: Guidelines for using design system color variables instead of hardcoded colors in SCSS/CSS files
---

# CSS Color Variables Consistency

## Overview

This skill provides guidelines for writing consistent CSS/SCSS code that uses design system color variables instead of hardcoded hex colors. Following these guidelines ensures:

- **Consistency** across the application
- **Theme support** (light/dark mode compatibility)
- **Maintainability** through centralized color management
- **Accessibility** with proper contrast ratios

## Available Design System Variables

### Background Colors

```scss
--color-bg-1    // Primary background (usually lighter/gray)
--color-bg-2    // Secondary background (usually white/main)
```

### Border Colors

```scss
--border-color-1  // Primary border color (light gray)
--border-color-2  // Secondary border color (medium gray)
```

### Interactive States

```scss
--color-hover     // Hover state background (with fallback)
--color-active    // Active/pressed state background (with fallback)
--border-hover    // Hover state border color
```

### Ionic Color Variables

```scss
// Semantic colors
--ion-color-primary       // Primary brand color
--ion-color-secondary     // Secondary brand color
--ion-color-tertiary      // Tertiary brand color
--ion-color-success       // Success state (green)
--ion-color-warning       // Warning state (orange/yellow)
--ion-color-danger        // Danger/error state (red)
--ion-color-medium        // Medium gray for icons/text
--ion-color-light         // Light gray
--ion-color-dark          // Dark gray/black

// Text colors
--ion-text-color          // Primary text color
--ion-color-text-1        // Secondary text color
--ion-color-text-2        // Tertiary text color

// Background
--ion-background-color    // Main background color
--ion-toolbar-background  // Toolbar background
```

### Other Useful Variables

```scss
--border-radius   // Standard border radius
--color-skeleton  // Skeleton loading color
--ion-border-color        // Standard border color
```

## Rules & Best Practices

### ❌ DON'T: Use Hardcoded Colors

```scss
// BAD - Hardcoded colors
.my-component {
  background: #ffffff;
  border: 1px solid #e5e5ea;
  color: #3a3a3c;
  
  &:hover {
    background: #f9f9f9;
    border-color: #d1d1d6;
  }
}

.cancel-button {
  --border-color: #ff9500;
  --color: #ff9500;
}
```

### ✅ DO: Use Design System Variables

```scss
// GOOD - Using design system variables
.my-component {
  background: var(--gd-comp-color-bg-2);
  border: 1px solid var(--gd-comp-border-color-1);
  color: var(--ion-color-medium);
  
  &:hover {
    background: var(--gd-comp-color-hover, #f9f9f9);
    border-color: var(--gd-comp-border-color-1);
  }
}

.cancel-button {
  --border-color: var(--ion-color-warning);
  --color: var(--ion-color-warning);
}
```

## Common Patterns

### 1. Card/Container Backgrounds

```scss
.card {
  background: var(--gd-comp-color-bg-2);  // White/main background
  border: 1px solid var(--gd-comp-border-color-1);
  border-radius: var(--gd-comp-border-radius);
}

.container {
  background: var(--gd-comp-color-bg-1);  // Gray/secondary background
}
```

### 2. Interactive Elements (Buttons, Items)

```scss
.interactive-item {
  background: var(--gd-comp-color-bg-2);
  border: 1px solid var(--gd-comp-border-color-1);
  
  &:hover {
    background: var(--gd-comp-color-hover, #f9f9f9);
    border-color: var(--gd-comp-border-hover);
  }
  
  &:active {
    background: var(--gd-comp-color-active, #f0f0f0);
  }
}
```

### 3. Text Colors

```scss
.title {
  color: var(--ion-text-color);  // Primary text
}

.subtitle {
  color: var(--ion-color-text-1);  // Secondary text
}

.description {
  color: var(--ion-color-medium);  // Muted text
}
```

### 4. Icons

```scss
.icon {
  color: var(--ion-color-medium);  // Default icon color
}

.icon-danger {
  color: var(--ion-color-danger);
}

.icon-success {
  color: var(--ion-color-success);
}
```

### 5. Borders & Dividers

```scss
.divider {
  border-top: 1px solid var(--gd-comp-border-color-1);
}

.outlined-box {
  border: 1px solid var(--gd-comp-border-color-1);
  border-radius: var(--gd-comp-border-radius);
}
```

### 6. Semantic Colors (Actions)

```scss
.primary-button {
  --background: var(--ion-color-primary);
  --color: #ffffff;
}

.warning-button {
  --border-color: var(--ion-color-warning);
  --color: var(--ion-color-warning);
}

.danger-button {
  --background: var(--ion-color-danger);
  --color: #ffffff;
}
```

## Fallback Values

When using variables that might not be defined everywhere, provide fallback values:

```scss
// With fallback for backward compatibility
.element {
  background: var(--gd-comp-color-hover, #f9f9f9);
  color: var(--ion-color-medium, #92949c);
}
```

## Verification Checklist

Before committing CSS/SCSS changes:

- [ ] Search for hardcoded hex colors: `grep -r "#[0-9a-fA-F]" yourfile.scss`
- [ ] Verify all colors use CSS variables
- [ ] Check that variable names exist in the design system
- [ ] Test visual appearance in the browser
- [ ] Ensure consistency with other v2 components

## Migration Example

### Before (Hardcoded)

```scss
.action-item {
  background: #ffffff;
  border: 1px solid #e5e5ea;
  color: #3a3a3c;
  
  &:hover {
    background: #f9f9f9;
    border-color: #d1d1d6;
  }
}

.cancel-button {
  --border-color: #ff9500;
  --color: #ff9500;
}
```

### After (Design System)

```scss
.action-item {
  background: var(--gd-comp-color-bg-2);
  border: 1px solid var(--gd-comp-border-color-1);
  color: var(--ion-color-medium);
  
  &:hover {
    background: var(--gd-comp-color-hover, #f9f9f9);
    border-color: var(--gd-comp-border-color-1);
  }
}

.cancel-button {
  --border-color: var(--ion-color-warning);
  --color: var(--ion-color-warning);
}
```

## Benefits Summary

✅ **Consistency**: Same colors across all components  
✅ **Maintainability**: Change colors in one place  
✅ **Theme Support**: Easy to add dark mode  
✅ **Accessibility**: Design system ensures proper contrast  
✅ **Developer Experience**: Clear, semantic variable names  

## Reference

For more information about available color variables, check:
- `/src/global.scss` - Global color definitions
- `/src/theme/variables.scss` - Theme variables
- Other v2 components for usage examples
