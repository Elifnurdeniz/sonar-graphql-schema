```graphql
"""
The input object that defines the fields for the createDepartment mutation.
"""
input CreateDepartmentMutationInput {
  """A descriptive name."""
  name: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
