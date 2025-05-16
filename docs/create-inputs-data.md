```graphql
"""
The input object that defines the fields for the createDataService mutation.
"""
input CreateDataServiceMutationInput {
  """The ID of the entity."""
  id: Int64Bit
  """Whether or not this is enabled."""
  enabled: Boolean!
  """A descriptive name."""
  name: String!
  """How this is applied."""
  application: ServiceApplication!
  """The amount, in the smallest currency value (e.g. cents, pence, pesos.)"""
  amount: Int!
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """How often this service bills, in months."""
  billing_frequency: Int!
  """The taxes applied when this service creates a transaction."""
  taxes: [ServiceTaxMutationInput]
  """The download speed of the service in kilobits per second."""
  download_speed_kilobits_per_second: Int!
  """The upload speed of the service in kilobits per second."""
  upload_speed_kilobits_per_second: Int!
  """
  The FCC technology code for the service. Only relevant to US ISPs filing FCC Form 477.
  """
  technology_code: TechnologyCode!
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
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createDataUsages mutation.
"""
input CreateDataUsageMutationInput {
  """The time."""
  time: Datetime!
  """The amount of inbound bytes (must be a counter value)."""
  inbytes: Int64Bit!
  """The amount of outbound bytes (must be a counter value)."""
  outbytes: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """The data source identifier."""
  data_source_identifier: String!
  """The data source parent."""
  data_source_parent: String!
}

"""
The input object that defines the fields for the createDataUsageTopOff mutation.
"""
input CreateDataUsageTopOffMutationInput {
  """The ID of an Account."""
  account_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int!
  """A note about this entity."""
  note: NoteMutationInput
}
```
