```graphql
"""
The input object that defines the fields for the createSearchFilter mutation.
"""
input CreateSearchFilterMutationInput {
  """The type of entity this filter belongs to."""
  entity_type: String!
  """Whether the filter is available to every user (admins only)."""
  all_users: Boolean
  """The filter's name."""
  name: String!
  """The actual filter, as JSON."""
  filter: String!
}
```
