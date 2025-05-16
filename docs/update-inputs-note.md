```graphql
"""The input object that defines the fields for the updateNote mutation."""
input UpdateNoteMutationInput {
  """The message."""
  message: Text
  """The priority of the note."""
  priority: NotePriority
}
```
