```graphql
"""
The input object that defines the fields for the createNonInventoryItem mutation.
"""
input CreateNonInventoryItemMutationInput {
  """A descriptive name."""
  name: String!
  """The ID of a GeneralLedgerCode."""
  general_ledger_code_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
