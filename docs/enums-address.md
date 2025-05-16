```graphql
"""
Whether this schedule address is a starting point, ending point, or both.
"""
enum ScheduleAddressType {
  """The starting point for the day."""
  START
  """The ending point for the day."""
  END
  """Both the start and end point."""
  BOTH
}
```
