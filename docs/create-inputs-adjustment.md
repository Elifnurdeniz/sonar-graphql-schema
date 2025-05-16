```graphql
"""
The input object that defines the fields for the createAdjustmentService mutation.
"""
input CreateAdjustmentServiceMutationInput {
  """The ID of the entity."""
  id: Int64Bit
  """Whether or not this is enabled."""
  enabled: Boolean!
  """A descriptive name."""
  name: String!
  """How this is applied."""
  application: ServiceApplication!
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """The taxes applied when this service creates a transaction."""
  taxes: [ServiceTaxMutationInput]
  """
  The amount that can be adjusted using this service within the period defined in `adjustment_service_days`.
  """
  amount: Int
  """
  The period of time in which transactions are tracked to calculate against the
  total defined in `adjustment_service_amount`.
  """
  days: Int
  """The ID of a tax definition on a transaction."""
  tax_definition_id: Int64Bit
  """The ID of a tax definition on a reversed transaction."""
  reverse_tax_definition_id: Int64Bit
  """The IDs of `Role`s that are allowed to use this adjustment service."""
  role_ids: [Int64Bit]!
  """A list of account group IDs that this account is part of."""
  account_group_ids: [Int64Bit]
  """
  If the amount for this service is zero, it will still display on invoices.
  """
  display_if_zero: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}
```
