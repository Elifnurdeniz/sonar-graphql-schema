```graphql
"""
The input object that defines the fields for the updateDrivers mutation.
"""
input UpdateDriversMutationInput {
  """IDs of `User`s."""
  user_ids: [Int64Bit]!
  """A note about this entity."""
  note: NoteMutationInput
}
```
