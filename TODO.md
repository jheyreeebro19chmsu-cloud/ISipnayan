# Router Fix Plan Progress

## Steps:
- [x] Step 1: Fix src/main.tsx - correct import path to './app/router', remove duplicate RouterProvider, render App instead
- [ ] Step 2: Update src/app/App.tsx - keep only SettingsProvider > RouterProvider
- [ ] Step 3: Create src/app/components/Layout.tsx - Navbar + Outlet for shared layout
- [ ] Step 4: Restructure router.tsx to use layout route, add loaders for auth protection
- [ ] Step 5: Test with npm run dev, check console, navigation
- [ ] Step 6: Update pages to use Outlet if needed (remove individual Navbar)

Current: Starting Step 1

