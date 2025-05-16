```graphql
"""
The input object that defines the fields for the updateNonInventoryItem mutation.
"""
input UpdateNonInventoryItemMutationInput {
  """A descriptive name."""
  name: String
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """
  Setting this value to `true` will set `general_ledger_code_id` to null.
  """
  unset_general_ledger_code_id: Boolean
}
```
