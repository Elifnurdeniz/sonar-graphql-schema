```graphql
"""
The input object that defines the fields for the scheduleManyJobsAndScheduleBlockerOverrides mutation.
"""
input ScheduleJobMutationInput {
  """The ID of a `Job`."""
  job_id: Int64Bit!
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit
  """The date and time this `Job` is scheduled for."""
  scheduled_datetime: Datetime
  """The length in minutes for this `Job`."""
  length_in_minutes: Int
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """Setting this value to `true` will set `scheduled_datetime` to null."""
  unset_scheduled_datetime: Boolean
  """Setting this value to `true` will set `ticket_id` to null."""
  unset_ticket_id: Boolean
}

"""
The input object that defines the fields for the scheduleManyJobsAndScheduleBlockerOverrides mutation.
"""
input ScheduleManyJobsAndScheduleBlockerOverridesMutationInput {
  """Jobs."""
  jobs: [ScheduleJobMutationInput]
  """Schedule blocker overrides."""
  schedule_blocker_overrides: [RescheduleScheduleBlockerMutationInput]
}
```
