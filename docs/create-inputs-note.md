```graphql
"""The input object that defines the fields for the createNote mutation."""
input CreateNoteMutationInput {
  """The message."""
  message: Text!
  """The ID of the entity that owns this note."""
  noteable_id: Int64Bit!
  """The type of entity that owns this note."""
  noteable_type: NoteableType!
  """The priority of the note."""
  priority: NotePriority!
}
```
