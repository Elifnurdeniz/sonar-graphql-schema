```graphql
"""An action that can be logged in a `GenericInventoryItemActionLog`."""
enum GenericInventoryItemActionLogAction {
  """Items were created."""
  CREATED
  """Items were consumed."""
  CONSUMED
  """Items were deleted."""
  DELETED
  """Items were assigned."""
  ASSIGNED
}
```
