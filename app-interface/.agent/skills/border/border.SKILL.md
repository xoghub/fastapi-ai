# border.scss — Global Border Styles

`border.scss` menyediakan utility classes dan attribute selectors untuk kontrol border yang konsisten di seluruh aplikasi GreatDay.

**Path:** `libs/greatday-components/src/style/border.scss`

---

## Utility Classes (Borders)

### 1. Default & Tertiary Borders
Utility standar menggunakan variabel Ionic atau GreatDay.

| Class | Deskripsi |
|---|---|
| `.border-color` | Border `1px solid` menggunakan `--ion-border-color`. |
| `.border-color-tertiary` | Border `1px solid` menggunakan `--ion-color-tertiary`. |

### 2. GreatDay Specific Border Colors
Menggunakan design tokens GreatDay (`--gd-comp-border-color-X`).

| Color Level | All Sides | Top | Right | Bottom | Left |
|---|---|---|---|---|---|
| **Color 1** | `.border-color-1` | `.border-color-1-top` | `.border-color-1-right` | `.border-color-1-bottom` | `.border-color-1-left` |
| **Color 2** | `.border-color-2` | `.border-color-2-top` | `.border-color-2-right` | `.border-color-2-bottom` | `.border-color-2-left` |
| **Color 3** | `.border-color-3` | `.border-color-3-top` | `.border-color-3-right` | `.border-color-3-bottom` | `.border-color-3-left` |

---

## Attribute Selectors (Thickness & Softness)

Gunakan attribute selector untuk kontrol yang lebih granular pada ketebalan (1px atau 2px).

### 1. Standard Thickness (Color 1)
Menggunakan warna `--gd-comp-border-color-1` secara default.

| Type | All Sides | Top | Right | Bottom | Left |
|---|---|---|---|---|---|
| **1px** | `[ba-1]` | `[bt-1]` | `[br-1]` | `[bb-1]` | `[bl-1]` |
| **2px** | `[ba-2]` | `[bt-2]` | `[br-2]` | `[bb-2]` | `[bl-2]` |

### 2. Soft Borders
Menggunakan warna `--ion-border-color` untuk tampilan yang lebih halus.

| Type | All Sides | Top | Right | Bottom | Left |
|---|---|---|---|---|---|
| **1px Soft** | `[ba-1-soft]` | `[bt-1-soft]` | `[br-1-soft]` | `[bb-1-soft]` | `[bl-1-soft]` |
| **2px Soft** | `[ba-2-soft]` | `[bt-2-soft]` | `[br-2-soft]` | `[bb-2-soft]` | `[bl-2-soft]` |

---

## Utility Radius

| Attribute | Deskripsi |
|---|---|
| `[rounded-sm]` | Menerapkan border-radius dari `--gd-comp-border-radius`. |

---

## Contoh Penggunaan

```html
<!-- Box dengan border 1px solid di semua sisi (Color 1) -->
<div ba-1 rounded-sm>
  Konten dengan border dan rounded corners.
</div>

<!-- Border bawah saja (soft) -->
<div bb-1-soft>
  Header section.
</div>

<!-- Menggunakan class -->
<div class="border-color-1-bottom">
  Item list.
</div>
```

---

## Design Tokens (CSS Variables)

| Token | Deskripsi |
|---|---|
| `--border-color-1` | Warna border level 1 (utama). |
| `--border-color-2` | Warna border level 2. |
| `--border-color-3` | Warna border level 3. |
| `--border-radius` | Radius standar untuk komponen. |
| `--ion-border-color` | Warna border default dari Ionic (digunakan untuk varian *soft*). |
