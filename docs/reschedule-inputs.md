```graphql
"""
The input object that defines the fields for the rescheduleScheduleBlocker mutation.
"""
input RescheduleScheduleBlockerMutationInput {
  """The ID of a `ScheduleBlocker`."""
  schedule_blocker_id: Int64Bit!
  """The date and time that this starts."""
  start_datetime: Datetime!
  """The ID of a User."""
  user_id: Int64Bit!
}
```
