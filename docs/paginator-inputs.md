```graphql
"""Used to paginate through results."""
input Paginator {
  """The page of results to display."""
  page: Int!
  """The number of records displayed per page."""
  records_per_page: Int!
}
```
