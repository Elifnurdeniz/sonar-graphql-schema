```graphql
"""
The input object that defines the fields for the setActiveStoredView mutation.
"""
input SetActiveStoredViewMutationInput {
  """The ID of a `StoredView` entity."""
  stored_view_id: Int64Bit
  """The location in the UI that this view is available."""
  location: String!
  """Setting this value to `true` will set `stored_view_id` to null."""
  unset_stored_view_id: Boolean
}
```
