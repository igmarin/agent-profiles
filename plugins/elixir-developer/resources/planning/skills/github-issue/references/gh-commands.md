# GitHub CLI Commands Reference

Quick reference for all `gh` commands used by the github-issue skill.

## Repository & Authentication

```bash
# Check authentication status
gh auth status

# Login to GitHub
gh auth login

# View repository info
gh repo view --json nameWithOwner,defaultBranchRef

# Check viewer permissions
gh repo view --json viewerPermission
```

## Issue Operations

### Create Issues

```bash
# Create a new issue
gh issue create \
  --title "Issue title" \
  --body "Issue body in markdown" \
  --label "bug,todo" \
  --assignee "username" \
  --project "Project Name"

# Create with body from file
gh issue create --title "Title" --body-file ./issue-body.md
```

### View & List Issues

```bash
# View a specific issue
gh issue view 42
gh issue view 42 --json title,body,labels,state,milestone

# List issues with filters
gh issue list --state open
gh issue list --label "bug"
gh issue list --assignee "username"
gh issue list --search "retry logic API"

# List with JSON output
gh issue list --json number,title,labels,state
```

### Edit Issues

```bash
# Update issue title
gh issue edit 42 --title "New title"

# Update issue body
gh issue edit 42 --body "New body"

# Add labels
gh issue edit 42 --add-label "in-progress,priority:high"

# Remove labels
gh issue edit 42 --remove-label "todo"

# Add and remove in one command
gh issue edit 42 --add-label "in-progress" --remove-label "todo"

# Set milestone
gh issue edit 42 --milestone "v1.2.0"

# Add assignee
gh issue edit 42 --add-assignee "username"

# Remove assignee
gh issue edit 42 --remove-assignee "username"
```

### Close & Reopen Issues

```bash
# Close an issue
gh issue close 42
gh issue close 42 --reason completed
gh issue close 42 --reason "not planned"

# Reopen a closed issue
gh issue reopen 42

# Close with comment
gh issue close 42 --comment "Fixed in PR #123"
```

### Issue Comments

```bash
# Add a comment
gh issue comment 42 --body "Working on this now"

# Add comment from file
gh issue comment 42 --body-file ./comment.md
```

## Projects V2

### List Projects

```bash
# List all projects for authenticated user
gh project list --limit 10
gh project list --json number,title,url,id

# List projects for an organization
gh project list --owner "organization-name"
```

### View Project Details

```bash
# View a specific project
gh project view 1
gh project view 1 --owner "organization-name"

# View with JSON output
gh project view 1 --json title,fields,items
```

### Manage Project Items

```bash
# Add an issue to a project
gh project item-add 1 --owner "owner-name" --url https://github.com/owner/repo/issues/42

# Remove an item from a project
gh project item-delete 1 --owner "owner-name" --id "ITEM_ID"

# List items in a project
gh project item-list 1 --owner "owner-name"
gh project item-list 1 --json id,title,content,number,status
```

### Edit Project Items

```bash
# Get field IDs and option IDs
gh project view 1 --owner "owner-name" --json fields

# Edit a field value (single select)
gh project item-edit \
  --id "ITEM_ID" \
  --field-id "FIELD_ID" \
  --single-select-option-id "OPTION_ID"

# Edit text field
gh project item-edit \
  --id "ITEM_ID" \
  --field-id "FIELD_ID" \
  --text "New value"

# Edit number field
gh project item-edit \
  --id "ITEM_ID" \
  --field-id "FIELD_ID" \
  --number 42

# Edit date field
gh project item-edit \
  --id "ITEM_ID" \
  --field-id "FIELD_ID" \
  --date "2024-01-15"

# Edit iteration field
gh project item-edit \
  --id "ITEM_ID" \
  --field-id "FIELD_ID" \
  --iteration-id "ITERATION_ID"
```

## Classic Projects

### List Classic Projects

```bash
# Via GraphQL API
gh api graphql -f query='
  query {
    repository(owner: "OWNER", name: "REPO") {
      projects(first: 10) {
        nodes {
          id
          name
          url
          columns(first: 10) {
            nodes {
              id
              name
            }
          }
        }
      }
    }
  }'
```

### Add Card to Classic Project

```bash
# Add issue as card to a column
gh api graphql -f query='
  mutation {
    addProjectCard(input: {
      projectColumnId: "COLUMN_ID",
      contentId: "ISSUE_NODE_ID"
    }) {
      cardEdge {
        node {
          id
          url
        }
      }
    }
  }'
```

### Move Card in Classic Project

```bash
# Move card to different column
gh api graphql -f query='
  mutation {
    moveProjectCard(input: {
      cardId: "CARD_ID",
      columnId: "NEW_COLUMN_ID"
    }) {
      clientMutationId
    }
  }'
```

## Milestones

### List Milestones

```bash
# List open milestones
gh api repos/{owner}/{repo}/milestones?state=open

# List with jq formatting
gh api repos/{owner}/{repo}/milestones?state=open --jq '.[] | "\(.title): \(.description)"'

# List all milestones (open and closed)
gh api repos/{owner}/{repo}/milestones?state=all
```

### Create Milestone

```bash
gh api repos/{owner}/{repo}/milestones \
  -f title="v1.2.0" \
  -f description="Feature release" \
  -f state="open" \
  -f due_on="2024-02-01T00:00:00Z"
```

### Update Milestone

```bash
gh api repos/{owner}/{repo}/milestones/MILESTONE_NUMBER \
  -f title="v1.2.1" \
  -f description="Updated description"
```

### Close Milestone

```bash
gh api repos/{owner}/{repo}/milestones/MILESTONE_NUMBER \
  -f state="closed"
```

## Labels

### List Labels

```bash
# List all labels in repo
gh label list

# List with JSON output
gh label list --json name,description,color
```

### Create Labels

```bash
# Create a single label
gh label create "priority:high" --color "d73a4a" --description "High priority"

# Create multiple labels from file
gh label create --force < labels.json
```

### Edit Labels

```bash
# Update label name
gh label edit "old-name" --name "new-name"

# Update label color
gh label edit "bug" --color "d73a4a"

# Update label description
gh label edit "bug" --description "Something isn't working"
```

### Delete Labels

```bash
gh label delete "deprecated-label" --yes
```

## GraphQL API Patterns

### Common Query Pattern

```bash
gh api graphql -f query='
  query {
    repository(owner: "OWNER", name: "REPO") {
      # Your query here
    }
  }'
```

### Common Mutation Pattern

```bash
gh api graphql -f query='
  mutation {
    mutationName(input: {
      # Input fields
    }) {
      # Return fields
    }
  }'
```

### Variables in GraphQL

```bash
gh api graphql \
  -f query='query($owner: String!, $name: String!) { 
    repository(owner: $owner, name: $name) { 
      issues(first: 5) { 
        nodes { title } 
      } 
    } 
  }' \
  -f owner=OWNER \
  -f name=REPO
```

## Useful Patterns

### Get Issue Node ID (for GraphQL)

```bash
gh issue view 42 --json id --jq '.id'
```

### Get Project Field Options

```bash
gh project view 1 --owner OWNER --json fields \
  --jq '.fields[] | select(.name=="Status") | .options'
```

### Search Issues with Filters

```bash
# Search by text
gh issue list --search "retry logic"

# Search by label
gh issue list --search "label:bug"

# Search by assignee
gh issue list --search "assignee:username"

# Search by milestone
gh issue list --search "milestone:v1.2.0"

# Combine filters
gh issue list --search "label:bug assignee:username is:open"
```

### Batch Operations

```bash
# Close all issues with specific label
gh issue list --label "wontfix" --json number --jq '.[].number' | \
  xargs -I {} gh issue close {}

# Add label to multiple issues
for issue in 42 43 44; do
  gh issue edit $issue --add-label "deprecated"
done
```

## Error Handling

### Common Errors

**Not authenticated:**
```bash
gh auth login
```

**Permission denied:**
```bash
# Check current permissions
gh repo view --json viewerPermission

# Request higher access if needed
```

**Resource not found:**
```bash
# Verify repo exists and you have access
gh repo view

# Check if issue exists
gh issue view ISSUE_NUMBER
```

**Rate limiting:**
```bash
# Check rate limit status
gh api rate_limit

# Wait for reset if needed
```

## Tips

1. **Use `--json` for scripting** — Easier to parse than text output
2. **Use `--jq` for filtering** — Extract specific fields from JSON output
3. **Use `-f` for form data** — Safer than string interpolation in API calls
4. **Use `--yes` to skip prompts** — Useful for automation
5. **Use `--body-file` for long content** — Avoids shell escaping issues
