```graphql
"""
The input object that defines the fields for the createGeneralLedgerCode mutation.
"""
input CreateGeneralLedgerCodeMutationInput {
  """
  A code for this general ledger code. This is typically numeric, but does not have to be.
  """
  code: String!
  """
  A human readable description for this general ledger code (e.g. Internet Services.)
  """
  description: String!
  """A note about this entity."""
  note: NoteMutationInput
}
```
