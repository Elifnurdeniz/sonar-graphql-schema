```graphql
"""The input object that defines the fields for the createTask mutation."""
input CreateTaskMutationInput {
  """The task to be performed."""
  task: Text!
  """The ID of a User."""
  user_id: Int64Bit
  """The date on which the task is due."""
  due: Date
  """The entity that the task is associated with."""
  taskable_type: TaskableType!
  """The ID of the entity that the task is associated with."""
  taskable_id: Int64Bit!
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
The input object that defines the fields for the createTaskTemplateItem mutation.
"""
input CreateTaskTemplateItemMutationInput {
  """The ID of a `TaskTemplate`."""
  task_template_id: Int64Bit!
  """The task to be performed."""
  task: String!
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
The input object that defines the fields for the createTaskTemplate mutation.
"""
input CreateTaskTemplateMutationInput {
  """A descriptive name."""
  name: String!
}
```
