```graphql
"""The status of an import."""
enum AsyncImportStatus {
  """The import is pending."""
  PENDING
  """The import is running."""
  IN_PROGRESS
  """The import has successfully completed."""
  SUCCESSFUL
  """The import has failed."""
  FAILED
}
```
