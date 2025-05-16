```graphql
"""
The input object that defines the fields for the createVehicle mutation.
"""
input CreateVehicleMutationInput {
  """A descriptive name."""
  name: String!
  """The manufacturer."""
  manufacturer: String
  """The model."""
  model: String
  """A year."""
  year: Int
  """The vehicle identification number."""
  vin: String
  """A `GpsTrackingProvider` ID."""
  gps_tracking_provider_id: Int64Bit
  """A GPS Tracking Provider vehicle unique identifier."""
  gps_tracking_uid: String
  """Whether or not GPS Tracking enabled for vehicle."""
  gps_tracking_enabled: Boolean
  """Whether or not to always track the vehicle."""
  gps_tracking_always: Boolean
  """If not always, then track on Monday."""
  gps_tracking_day_monday: Boolean
  """If not always, then track on Tuesday."""
  gps_tracking_day_tuesday: Boolean
  """If not always, then track on Wednesday."""
  gps_tracking_day_wednesday: Boolean
  """If not always, then track on Thursday."""
  gps_tracking_day_thursday: Boolean
  """If not always, then track on Friday."""
  gps_tracking_day_friday: Boolean
  """If not always, then track on Saturday."""
  gps_tracking_day_saturday: Boolean
  """If not always, then track on Sunday."""
  gps_tracking_day_sunday: Boolean
  """If not always, start time for tracking."""
  gps_tracking_start_time: Time
  """If not always, end time for tracking."""
  gps_tracking_end_time: Time
  """The timezone you want times in the system displayed in."""
  gps_tracking_timezone: Timezone
  """A note about this entity."""
  note: NoteMutationInput
}
```
