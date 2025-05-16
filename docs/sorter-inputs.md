```graphql
"""Used to sort results."""
input Sorter {
  """The model attribute you wish to reference."""
  attribute: String!
  """The direction to sort in."""
  direction: SortDirection!
}
```
