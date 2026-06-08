---
trigger: always_on
---

You are an expert in TypeScript configuration and type safety.

Key Principles:
- Enable 'strict': true in tsconfig.json
- Avoid 'any' type at all costs
- Use 'unknown' for uncertain types
- Handle null and undefined explicitly

Strict Mode Features:
- noImplicitAny: Forces typing of all variables
- strictNullChecks: Prevents accessing properties of null/undefined
- strictFunctionTypes: Enforces sound function parameter bivariance
- strictPropertyInitialization: Ensures class properties are initialized

Type Safety Best Practices:
- Use type guards (typeof, instanceof, custom guards) to narrow types
- Use discriminated unions for state management
- Use 'readonly' for immutable data structures
- Use 'as const' for literal types
- Prefer Interfaces for public APIs, Types for unions/intersections

Error Handling:
- Don't throw strings; throw Error objects
- Use Result types or Option types for functional error handling
- Handle all cases in switch statements (exhaustiveness checking)

You are an expert in the TypeScript ecosystem.

Key Principles:
- Use modern tooling for faster builds
- Integrate linting and formatting
- Generate type definitions automatically

Build Tools:
- tsc: The standard compiler (good for type checking)
- esbuild/swc: Extremely fast transpilation (no type checking)
- Vite: Modern dev server with native ES modules

Linting & Formatting:
- ESLint: Use typescript-eslint for linting
- Prettier: For consistent code formatting
- Husky & lint-staged: Run checks on commit

Type Generation:
- Generate types from database schema (Prisma, Supabase)
- Generate types from GraphQL schema (GraphQL Code Generator)
- Generate types from API specs (OpenAPI TypeScript)

Debugging:
- Use source maps for debugging TS code
- Use VS Code's built-in TypeScript debugger
- Use 'ts-node' for running TS scripts directly

Monorepos:
- Use Project References for faster incremental builds
- Share types across packages
- Use build tools like Turborepo or Nx