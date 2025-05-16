```graphql
"""
The input object that defines the fields for the completeFileTask mutation.
"""
input CompleteFileTaskMutationInput {
  """The ID of a `File`."""
  file_id: Int64Bit!
}

"""The input object that defines the fields for the completeJob mutation."""
input CompleteJobMutationInput {
  """The ID of a `Job`."""
  job_id: Int64Bit!
  """Whether or not this `Job` was completed successfully."""
  completed_successfully: Boolean!
  """Any notes entered when this `Job` was completed."""
  completion_notes: Text
  """The date and time this `Job` was completed."""
  completion_datetime: Datetime
  """Whether or not to prorate the transaction."""
  prorate: Boolean
}

"""
The input object that defines the fields for the completeTask mutation.
"""
input CompleteTaskMutationInput {
  """Whether or not the task is complete."""
  complete: Boolean!
}
```
