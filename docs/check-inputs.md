```graphql
"""
The input object that defines the fields for the checkInToJob mutation.
"""
input CheckInToJobMutationInput {
  """The ID of a `Job`."""
  job_id: Int64Bit!
  """The ID of the `User` that created a `JobCheckIn`."""
  user_id: Int64Bit
  """The date and time that this `Job` was checked into."""
  check_in_datetime: Datetime
}

"""
The input object that defines the fields for the checkOutOfJob mutation.
"""
input CheckOutOfJobMutationInput {
  """The ID of a `Job`."""
  job_id: Int64Bit!
  """The ID of the `User` that created a `JobCheckIn`."""
  user_id: Int64Bit
  """The date and time that this `Job` was checked out of."""
  check_out_datetime: Datetime
}
```
