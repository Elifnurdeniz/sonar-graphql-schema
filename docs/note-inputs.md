```graphql
"""Allows the addition of a note to the parent entity."""
input NoteMutationInput {
  """The message."""
  message: Text!
  """The priority of the note."""
  priority: NotePriority!
}
```
