```graphql
"""
The input object that defines the fields for the updateScheduleAddress mutation.
"""
input UpdateScheduleAddressMutationInput {
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """A descriptive name."""
  name: String
  """Address line 1."""
  line1: String
  """Address line 2."""
  line2: String
  """A city."""
  city: String
  """A state, province, or other country subdivision."""
  subdivision: Subdivision
  """A ZIP or postal code."""
  zip: String
  """A two character country code."""
  country: Country
  """A decimal latitude."""
  latitude: Latitude
  """A decimal latitude."""
  longitude: Longitude
  """The type of schedule address that this is."""
  type: ScheduleAddressType
  """The timezone you want times in the system displayed in."""
  timezone: Timezone
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateScheduleAvailabilityDayTime mutation.
"""
input UpdateScheduleAvailabilityDayTimeMutationInput {
  """A day."""
  day: Day
  """Whether this day is available from start to finish."""
  all_day: Boolean
  """The start time for the day."""
  start_time: Time
  """The end time for the day."""
  end_time: Time
}

"""
The input object that defines the fields for the updateScheduleAvailability mutation.
"""
input UpdateScheduleAvailabilityMutationInput {
  """A descriptive name."""
  name: String
  """The start date for this `ScheduleAvailability`."""
  start_date: Date
  """
  Whether or not this `ScheduleAvailability` creates or removes availability.
  """
  available: Boolean
  """Whether this repeats forever or not."""
  infinite_repetitions: Boolean
  """The number of times this repeats."""
  repetitions: Int
  """The number of weeks between repetitions."""
  weeks_between_repetitions: Int
  """The ID of a `Geofence`."""
  geofence_id: Int64Bit
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """IDs of `JobType`s."""
  job_type_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `geofence_id` to null."""
  unset_geofence_id: Boolean
}

"""
The input object that defines the fields for the updateScheduleBlockerDayTime mutation.
"""
input UpdateScheduleBlockerDayTimeMutationInput {
  """A day."""
  day: Day
  """The start time for the day."""
  start_time: Time
  """The end time for the day."""
  end_time: Time
}

"""
The input object that defines the fields for the updateScheduleBlocker mutation.
"""
input UpdateScheduleBlockerMutationInput {
  """A descriptive name."""
  name: String
  """The start date for this `ScheduleAvailability`."""
  start_date: Date
  """Whether this repeats forever or not."""
  infinite_repetitions: Boolean
  """The number of times this repeats."""
  repetitions: Int
  """The number of weeks between repetitions."""
  weeks_between_repetitions: Int
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateScheduleTimeOff mutation.
"""
input UpdateScheduleTimeOffMutationInput {
  """A descriptive name."""
  name: String
  """The date and time that this starts."""
  start_datetime: Datetime
  """The date and time that this ends."""
  end_datetime: Datetime
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}
```
