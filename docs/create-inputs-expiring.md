```graphql
"""
The input object that defines the fields for the createExpiringService mutation.
"""
input CreateExpiringServiceMutationInput {
  """The ID of the entity."""
  id: Int64Bit
  """Whether or not this entity is active."""
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
  """The number of times this expiring service should run."""
  times_to_run: Int!
  """How often this service bills, in months."""
  billing_frequency: Int!
  """The ID of a tax definition on a transaction."""
  tax_definition_id: Int64Bit
  """The ID of a tax definition on a reversed transaction."""
  reverse_tax_definition_id: Int64Bit
  """The taxes applied when this service creates a transaction."""
  taxes: [ServiceTaxMutationInput]
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
