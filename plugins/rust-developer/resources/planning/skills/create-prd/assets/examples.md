# create-prd — examples

## Short discovery (one-pager)

- **Name:** Search Autocomplete
- **Summary:** Improve search UX with real-time autocomplete.
- **Problem:** Users struggle to find items quickly; no suggestions.
- **Goal:** Increase successful search completions by 15%.
- **User story:** As a user, I want inline suggestions while typing.
- **Acceptance criteria:**
  - Given the user types >= 2 chars, show up to 5 suggestions within 150ms.
  - On network errors, show graceful fallback.
- **Rollout:** Feature flag, 10% → 50% → 100%.
- **Checklist:**
  - [ ] Tasks generated
  - [ ] Specs added
  - [ ] Component tests
  - [ ] Backend tests
  - [ ] Monitoring dashboards
