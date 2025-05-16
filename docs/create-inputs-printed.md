```graphql
"""
The input object that defines the fields for the createPrintedInvoiceBatch mutation.
"""
input CreatePrintedInvoiceBatchMutationInput {
  """The date to generate the printed invoice batch for."""
  date: Date!
  """Include detailed transactions on a printed invoice batch."""
  with_detailed_transactions: Boolean = true
  """Exclude zero balance invoices from the printed invoice batch."""
  exclude_paid: Boolean = false
  """A note about this entity."""
  note: NoteMutationInput
  """
  A list of file IDs to be associated with this object. These must first have
  been uploaded to the /files endpoint and must be currently unassociated.
  """
  files: [AssociateFileMutationInput]
}
```
