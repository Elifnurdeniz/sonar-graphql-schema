```graphql
"""
The input object that defines the fields for the updateDepartment mutation.
"""
input UpdateDepartmentMutationInput {
  """A descriptive name."""
  name: String
  """A note about this entity."""
  note: NoteMutationInput
}
```
