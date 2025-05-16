```graphql
"""types.drive_time_result"""
type DriveTimeResult {
  """The starting latitude."""
  start_latitude: Latitude!
  """The starting longitude."""
  start_longitude: Longitude!
  """The ending latitude."""
  end_latitude: Latitude!
  """The ending longitude."""
  end_longitude: Longitude!
  """
  The amount of time it takes to drive from the start to the end, in minutes.
  """
  drive_time_in_minutes: Int
  """Whether the drive time lookup succeeded."""
  success: Boolean!
  """If the drive time lookup failed, the error that was provided."""
  error: Text
}

"""types.drive_time_result_wrapper"""
type DriveTimeResultWrapper {
  """The results of the drive time lookup."""
  results: [DriveTimeResult]!
  """The number of lookups that were loaded from the cache."""
  cached_lookups: Int!
}
```
