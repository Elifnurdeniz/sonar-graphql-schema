```graphql
"""
The input object that defines the fields for the updateDataService mutation.
"""
input UpdateDataServiceMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """A descriptive name."""
  name: String
  """How this is applied."""
  application: ServiceApplication
  """The amount, in the smallest currency value (e.g. cents, pence, pesos.)"""
  amount: Int
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """How often this service bills, in months."""
  billing_frequency: Int
  """The taxes applied when this service creates a transaction."""
  taxes: [ServiceTaxMutationInput]
  """The download speed of the service in kilobits per second."""
  download_speed_kilobits_per_second: Int
  """The upload speed of the service in kilobits per second."""
  upload_speed_kilobits_per_second: Int
  """
  The FCC technology code for the service. Only relevant to US ISPs filing FCC Form 477.
  """
  technology_code: TechnologyCode
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """
  The global service profile name for this service if using Telrad provisioning.
  """
  telrad_global_service_profile_name: String
  """The ID of a `UsageBasedBillingPolicy`."""
  usage_based_billing_policy_id: Int64Bit
  """
  If the amount for this service is zero, it will still display on invoices.
  """
  display_if_zero: Boolean
  """The ID of a tax definition on a transaction."""
  tax_definition_id: Int64Bit
  """The ID of a tax definition on a reversed transaction."""
  reverse_tax_definition_id: Int64Bit
  """Unset the ID of a tax definition on a transaction."""
  unset_tax_definition_id: Boolean
  """Unset the ID of a tax definition on a reversed transaction."""
  unset_reverse_tax_definition_id: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `general_ledger_code_id` to null.
  """
  unset_general_ledger_code_id: Boolean
  """Setting this value to `true` will set `company_id` to null."""
  unset_company_id: Boolean
  """
  Setting this value to `true` will set `usage_based_billing_policy_id` to null.
  """
  unset_usage_based_billing_policy_id: Boolean
  """
  Setting this value to `true` will set `telrad_global_service_profile_name` to null.
  """
  unset_telrad_global_service_profile_name: Boolean
}

"""
The input object that defines the fields for the updateDataUsageHistory mutation.
"""
input UpdateDataUsageHistoryMutationInput {
  """The total billable inbound data in bytes."""
  billable_in_bytes: Int64Bit
  """The total billable outbound data in bytes."""
  billable_out_bytes: Int64Bit
  """The total free inbound data in bytes."""
  free_in_bytes: Int64Bit
  """The total free outbound data in bytes."""
  free_out_bytes: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
