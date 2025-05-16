```graphql
"""
The input object that defines the fields for the createDepositSlip mutation.
"""
input CreateDepositSlipMutationInput {
  """A date"""
  date: Date!
  """The bank account name/number"""
  bank_account_line: String!
  """The memo."""
  memo: Text
  """The payment IDs."""
  payment_ids: [Int64Bit]!
  """A note about this entity."""
  note: NoteMutationInput
  """
  A single file to associate with this object. Any existing file will be overwritten.
  """
  file: AssociateFileMutationInput
}
```
