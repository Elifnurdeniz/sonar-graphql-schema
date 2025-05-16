```graphql
"""
The input object that defines the fields for the createAccessLog mutation.
"""
input CreateAccessLogMutationInput {
  """The entity that this access log belongs to."""
  accessloggable_type: String!
  """The ID of the entity that this access log belongs to."""
  accessloggable_id: Int64Bit!
  """A note about this entity."""
  note: NoteMutationInput
}
```
