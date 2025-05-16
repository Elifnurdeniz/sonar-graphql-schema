```graphql
"""The input object that defines the fields for the updateTask mutation."""
input UpdateTaskMutationInput {
  """The task to be performed."""
  task: Text
  """The ID of a User."""
  user_id: Int64Bit
  """The date on which the task is due."""
  due: Date
  """The order this item is shown in a list."""
  list_order: Int
  """Setting this value to `true` will set `user_id` to null."""
  unset_user_id: Boolean
  """Setting this value to `true` will set `due` to null."""
  unset_due: Boolean
}

"""
The input object that defines the fields for the updateTaskTemplateItem mutation.
"""
input UpdateTaskTemplateItemMutationInput {
  """The ID of a `TaskTemplate`."""
  task_template_id: Int64Bit
  """The task to be performed."""
  task: String
  """How this task gets marked as completed."""
  completion_type: TaskCompletionType = BOOLEAN
  """
  The type of entity that completes this task. Only required when completion_type is not `BOOLEAN`.
  """
  completable_type: CompletableType
  """
  The ID of the entity that completes or completed this task. Only required if completable_type is `CustomField`.
  """
  completable_id: Int64Bit
  """The order this item is shown in a list."""
  list_order: Int
}

"""
The input object that defines the fields for the updateTaskTemplate mutation.
"""
input UpdateTaskTemplateMutationInput {
  """A descriptive name."""
  name: String
}
```
