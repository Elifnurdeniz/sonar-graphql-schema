```graphql
"""
The input object that defines the fields for the updateVoiceProvider mutation.
"""
input UpdateVoiceProviderMutationInput {
  """A descriptive name."""
  name: String
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateVoiceProviderRateChargePercent mutation.
"""
input UpdateVoiceProviderRateChargePercentMutationInput {
  """The ID of a `VoiceProvider`."""
  voice_provider_id: Int64Bit!
  """The percentage over the base rate to charge the customer."""
  charge_percent: Float!
}

"""
The input object that defines the fields for the updateVoiceProviderRate mutation.
"""
input UpdateVoiceProviderRateMutationInput {
  """The description for the rate."""
  description: String
  """The rate that is imported from a rate deck."""
  base_rate: Float
  """The percentage over the base rate to charge the customer."""
  charge_percent: Float
}

"""
The input object that defines the fields for the updateVoiceServiceGenericParameter mutation.
"""
input UpdateVoiceServiceGenericParameterMutationInput {
  """A human readable description."""
  description: String
  """The price per unit of this item."""
  price: Int
  """
  The taxes applied when this voice service generic parameter creates a transaction.
  """
  taxes: [VoiceServiceGenericParameterTaxMutationInput]
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
}

"""
The input object that defines the fields for the updateVoiceService mutation.
"""
input UpdateVoiceServiceMutationInput {
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
  """Whether this service provides unlimited local minutes."""
  unlimited_local_minutes: Boolean
  """
  The quantity of free local minutes provided, if `unlimited_local_minutes` is false.
  """
  local_minutes: Int
  """
  The cost per minute for local calls, in thousandths of the smallest currency value (e.g. cents, pence, pesos.).
  """
  cost_per_minute_local_in_thousandths: Int
  """Whether this service provides unlimited long distance minutes."""
  unlimited_long_distance_minutes: Boolean
  """
  The quantity of free long distance minutes provided, if `unlimited_long_distance_minutes` is false.
  """
  long_distance_minutes: Int
  """
  The cost per minute for long distance calls, in thousandths of the smallest currency value (e.g. cents, pence, pesos.).
  """
  cost_per_minute_long_distance_in_thousandths: Int
  """
  If a customer has a toll free number, this is the rate charged to them for
  inbound calls, in thousandths of the smallest currency value (e.g. cents,
  pence, pesos.).
  """
  inbound_toll_free_rate_per_minute_in_thousandths: Int
  """
  This is the minimum amount of time the customer will be charged for a call.
  """
  first_interval_in_seconds: Int
  """
  After the `first_interval_in_seconds` time is exceeded, this is the minimum
  amount of subsequent time. For example, if `first_interval_in_seconds` is 30,
  and `sub_interval_in_seconds` is 6, then a 31 second call would be charged at
  36 seconds, and a 37 second call would be charged at 42 seconds.
  """
  sub_interval_in_seconds: Int
  """A two character country code."""
  country: Country
  """The ID of a tax definition on a transaction."""
  tax_definition_id: Int64Bit
  """The ID of a tax definition on a reversed transaction."""
  reverse_tax_definition_id: Int64Bit
  """Unset the ID of a tax definition on a transaction."""
  unset_tax_definition_id: Boolean
  """Unset the ID of a tax definition on a reversed transaction."""
  unset_reverse_tax_definition_id: Boolean
  """Which prefixes should be treated as local for this voice service."""
  local_prefixes: [Numeric]
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """
  If the amount for this service is zero, it will still display on invoices.
  """
  display_if_zero: Boolean
  """
  Indicates if Call Detail Records (CDRs) for this service should be displayed on an invoice.
  """
  show_call_detail_records_on_invoice: Boolean
  """
  Hide parameters of this service on customer invoices/statements and in the customer portal.
  """
  rollup_generic_parameters: Boolean
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `general_ledger_code_id` to null.
  """
  unset_general_ledger_code_id: Boolean
  """Setting this value to `true` will set `company_id` to null."""
  unset_company_id: Boolean
}
```
