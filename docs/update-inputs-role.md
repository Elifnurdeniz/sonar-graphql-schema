```graphql
"""The input object that defines the fields for the updateRole mutation."""
input UpdateRoleMutationInput {
  """A descriptive name."""
  name: String
  """A list of permissions associated with this role."""
  applied_permissions: [Permission!]
  """A note about this entity."""
  note: NoteMutationInput
}
```
