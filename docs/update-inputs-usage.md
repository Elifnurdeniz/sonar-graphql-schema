```graphql
"""
The input object that defines the fields for the updateUsageBasedBillingPolicyFreePeriod mutation.
"""
input UpdateUsageBasedBillingPolicyFreePeriodMutationInput {
  """A day."""
  day: Day
  """The start."""
  start: Time
  """The end."""
  end: Time
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateUsageBasedBillingPolicy mutation.
"""
input UpdateUsageBasedBillingPolicyMutationInput {
  """A descriptive name."""
  name: String
  """The available data usage in this policy, measured in gigabytes."""
  cap_in_gigabytes: Int
  """Whether or not rollover is enabled."""
  rollover_enabled: Boolean
  """Whether or not rollover expiration is enabled."""
  rollover_expiration_enabled: Boolean
  """
  Rollover expires after this many months, if rollover expiration is enabled.
  """
  rollover_expiration_months: Int
  """
  Whether or not to assess charges for usage over the bandwidth limit at the end of the billing period.
  """
  assess_charges_at_end_of_billing_period: Boolean
  """
  Whether or not a customer can purchase additional data usage capacity during a billing period.
  """
  allow_purchase_of_additional_capacity_during_billing_period: Boolean
  """
  The overage service that this policy uses to charge for service overages.
  """
  service_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `service_id` to null."""
  unset_service_id: Boolean
}
```
