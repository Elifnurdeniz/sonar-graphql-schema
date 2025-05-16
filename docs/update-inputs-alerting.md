```graphql
"""
The input object that defines the fields for the updateAlertingRotationDay mutation.
"""
input UpdateAlertingRotationDayMutationInput {
  """The alerting rotation ID."""
  alerting_rotation_id: Int64Bit
  """A day."""
  day: Day
  """The start time for the day."""
  start_time: Time
  """The end time for the day."""
  end_time: Time
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateAlertingRotation mutation.
"""
input UpdateAlertingRotationMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """The start."""
  start: Date
  """The number of times this repeats."""
  repetitions: Int
  """The number of weeks between repetitions."""
  weeks_between_repetitions: Int
  """Whether this repeats forever or not."""
  infinite_repetitions: Boolean
  """
  The number of minutes a device can be in a warning state before generating alert.
  """
  warning_time_in_minutes_before_alerting: Int
  """
  The number of minutes a device can remain in a warning state before sending a repeat alert.
  """
  warning_time_in_minutes_before_repeat: Int
  """
  The number of minutes a device can be in a down state before generating alert.
  """
  down_time_in_minutes_before_alerting: Int
  """
  The number of minutes a device can remain in a down state before sending a repeat alert.
  """
  down_time_in_minutes_before_repeat: Int
  """Whether to include all account equipment in this rotation."""
  all_accounts: Boolean
  """Whether to include all network site equipment in this rotation."""
  all_network_sites: Boolean
  """Whether to include all inventory models in this rotation."""
  all_inventory_models: Boolean
  """IDs of `User`s."""
  user_ids: [Int64Bit]
  """IDs of `NetworkSite`s."""
  network_site_ids: [Int64Bit]
  """IDs of `InventoryModel`s."""
  inventory_model_ids: [Int64Bit]
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `repetitions` to null."""
  unset_repetitions: Boolean
}
```
