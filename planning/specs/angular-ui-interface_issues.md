# Angular UI Interface Component & Layout

## 1. Big View & Features
* **Goal**: Implement the Angular (v20) frontend user interface for the Product Review Aspect-Based Sentiment Analysis (ABSA) system.
* **Features**:
  * **Authentic Dashboard Layout**: A premium, responsive web interface built using our custom Flex Layout, CSS Border, and Color Variables.
  * **Review Analysis Dashboard**:
    * An interactive text input area for users to paste marketplace product reviews.
    * A real-time analysis engine triggering the FastAPI `/api/v1/analyze` endpoint.
    * Visual Cards displaying the extracted aspects (e.g., `suara`, `harga`, `packing`) and their associated sentiments (Positive, Neutral, Negative) with harmonized color badges.
  * **Error Handling & Offline Support**:
    * Displays skeleton states with a notice warning that the server is disconnected or down if the backend API is unreachable.

## 2. Technology Stack
* **Framework**: Angular v20 (Standalone Components, Signals for fine-grained reactivity, OnPush change detection)
* **Styling**: SCSS, Custom Flex Layout attribute system, CSS variables for borders and colors (no Tailwind CSS by default as per CSS variables/border skills)
* **HTTP Client**: `provideHttpClient` to communicate with the FastAPI backend.

## 3. Project Structure & Naming Conventions
Following the conventions in [CONTEXT.md](../../CONTEXT.md):
* **Styles**:
  * [NEW] `app-interface/src/styles/colors.scss` (design tokens for backgrounds, texts, active/hover states)
  * [NEW] `app-interface/src/styles/flex.scss` (responsive flex attributes generator)
  * [NEW] `app-interface/src/styles/border.scss` (thickness & soft border attributes generator)
  * [MODIFY] `app-interface/src/styles.scss` (main style import point)
* **Components**:
  * [NEW] `app-interface/src/app/product-review-analysis.component.ts` (main dashboard component)
  * [NEW] `app-interface/src/app/product-review-analysis.html` (dashboard template)
  * [NEW] `app-interface/src/app/product-review-analysis.scss` (dashboard component styles)
  * [NEW] `app-interface/src/app/product-review-analysis-api.service.ts` (API connection service)

---

## 4. Style Consistency & Color Patterns

### 4.1 Design System Variables
We will define and use the following tokens in `colors.scss` and `border.scss`:
* `--color-bg-1`: Main page background (light/gray)
* `--color-bg-2`: Container/Card background (white/card)
* `--border-color-1`: Standard border color (light gray)
* `--border-color-2`: Secondary border color (medium gray)
* `--color-hover`: Hover background state
* `--color-active`: Click/active background state
* `--color-skeleton`: Skeleton loader animation base color
* `--border-radius`: Standard `8px` corner radius

### 4.2 Flex Layout Attribute Selectors
We will implement the flex utilities generator in `flex.scss` support:
* `fx-row-start-center`, `fx-column-between-stretch`, etc.
* Breakpoints: `sm` (768px), `md` (1280px), `lg` (1920px).
* Gap sizing: `fx-gap-8`, `fx-gap-16`, `fx-gap-24`.
* Grid columns: `fx-12`, `fx-sm-6`, `fx-md-4`.

### 4.3 Border Attribute Selectors
* Sided borders: `[ba-1]`, `[bt-1]`, `[bb-1-soft]`, etc.
* Rounded corners: `[rounded-sm]`.

---

## 5. UI Component Specifications

### 5.1 Main Layout
* Header: App branding ("FAST-AI ABSA") and server connectivity badge.
* Main Area: Split into two columns for screens >= `sm` (`fx-row-sm-start-start`):
  * **Left Column (fx-12 fx-sm-5)**: Review Input card with a text area and Analyze button.
  * **Right Column (fx-12 fx-sm-7)**: Analysis Results display or Skeleton Warning.

### 5.2 Forms & Inputs
* **Review Input Form**: Text area input with character counter, validation (minimum 10 characters), and an Analyze button displaying a loading spinner during API requests.

### 5.3 Offline & Error Handling
* If the API server is unreachable:
  * Shows a skeleton container loading block in place of results.
  * Displays a red/warning notice text: *"Server is offline or disconnected. Please check your backend connection."*

### 5.4 Analysis Results Display
* Aspect and Sentiment cards formatted using the design tokens.
* Sentiment badges:
  * **Positive**: Green tint (`var(--ion-color-success)`)
  * **Neutral**: Orange/yellow tint (`var(--ion-color-warning)`)
  * **Negative**: Red tint (`var(--ion-color-danger)`)

---

## 6. API Integration

### 6.1 Review Analysis (`POST /api/v1/analyze`)
* **Headers**:
  * `Content-Type: application/json`
* **Request**:
  ```json
  {
    "review_text": "..."
  }
  ```
* **Response (Success)**:
  ```json
  {
    "review_text": "...",
    "analysis": [
      {
        "aspect": "...",
        "sentiment": "..."
      }
    ]
  }
  ```

---

## 7. Implementation Steps

1. **Setup Global Design System**:
   * Create `colors.scss`, `flex.scss`, `border.scss` under `src/styles/`.
   * Add the required SCSS logic to generate attribute selectors for flex, gaps, grid sizes, and borders.
   * Import all three files inside `src/styles.scss`.
2. **Setup HTTP and Services**:
   * Configure `provideHttpClient` in `app.config.ts`.
   * Implement `ProductReviewAnalysisApiService` using signals to manage state (loading, error, and analysis results).
3. **Build UI Components**:
   * Create `product-review-analysis.component.ts`, `product-review-analysis.html`, and `product-review-analysis.scss`.
   * Implement UI using reactive forms and flex attribute selectors.
4. **Wire up Routing**:
   * Register the new component in `app.routes.ts`.
5. **Verify**:
   * Serve the Angular application.
   * Verify responsiveness, design system variables, and live integration with the FastAPI backend.
