```graphql
"""Filters for this stored view group."""
input StoredFilterMutationInput {
  """The order in which the filter is applied."""
  order: Int
  """The field that is being filtered."""
  field: String!
  """The operator being applied."""
  operator: StoredFilterOperator!
  """The value being filtered against."""
  value: String
}

"""Filter groups for this stored view."""
input StoredGroupMutationInput {
  """The list of filters for this `StoredGroup`."""
  stored_filters: [StoredFilterMutationInput]!
}
```
