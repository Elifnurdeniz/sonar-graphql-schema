```graphql
"""An object that provides information about the current page of results."""
type PageInfo {
  """The current page of results."""
  page: Int!
  """The total number of pages available."""
  total_pages: Int!
  """The total number of records available."""
  total_count: Int!
  """The number of records displayed per page."""
  records_per_page: Int!
}
```
