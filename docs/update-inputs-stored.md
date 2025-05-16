```graphql
"""
The input object that defines the fields for the updateStoredView mutation.
"""
input UpdateStoredViewMutationInput {
  """A name to identify this `StoredView`."""
  name: String
  """Whether or not this StoredView is available to all users."""
  is_global: Boolean
  """The type of `StoredView`."""
  type: StoredViewType
  """The column used to sort the filtered results."""
  sort_column: String
  """The direction to sort in."""
  sort_direction: SortDirection
  """The list of filter groups for this `StoredView`."""
  stored_groups: [StoredGroupMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `sort_column` to null."""
  unset_sort_column: Boolean
  """Setting this value to `true` will set `sort_direction` to null."""
  unset_sort_direction: Boolean
}
```
