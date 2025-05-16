```graphql
"""The input object that defines the fields for the createTask mutation."""
input TaskMutationInput {
  """The task to be performed."""
  task: Text!
  """The ID of a User."""
  user_id: Int64Bit
  """The date on which the task is due."""
  due: Date
  """How this task gets marked as completed."""
  completion_type: TaskCompletionType!
  """The type of entity that completes this task."""
  completable_type: CompletableType
  """The ID of the entity that completes or completed this task."""
  completable_id: Int64Bit
}
```
