```graphql
"""Details around resending an email invoice batch."""
input EmailInvoiceBatchMutationInput {
  """Send invoices with a `date` property matching this."""
  date: Date!
}

"""
The input object that defines the fields for the emailInvoiceToContact mutation.
"""
input EmailInvoiceToContactMutationInput {
  """The ID of an `Invoice`."""
  invoice_id: Int64Bit!
  """The ID of the contact that owns this."""
  contact_id: Int64Bit!
  """The type of bill this account receives."""
  bill_mode: BillMode
}
```
