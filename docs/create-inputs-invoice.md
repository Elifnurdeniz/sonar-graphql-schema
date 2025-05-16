```graphql
"""
The input object that defines the fields for the createInvoiceAttachment mutation.
"""
input CreateInvoiceAttachmentMutationInput {
  """A descriptive name."""
  name: String!
  """The date to start attaching this PDF to invoices."""
  start: Date
  """The date to stop attaching this PDF to invoices."""
  end: Date
  """A note about this entity."""
  note: NoteMutationInput
  """
  A single file to associate with this object. Any existing file will be overwritten.
  """
  file: AssociateFileMutationInput
}

"""
The input object that defines the fields for the createInvoiceMessage mutation.
"""
input CreateInvoiceMessageMutationInput {
  """A descriptive name."""
  name: String!
  """The message."""
  message: String!
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createInvoice mutation.
"""
input CreateInvoiceMutationInput {
  """
  A list of `Debit` IDs to be used to create the invoice. They must not be currently associated with an invoice.
  """
  debit_ids: [Int64Bit]!
  """The invoice date."""
  date: Date!
  """A custom message to print on the invoice."""
  message: Text
  """The date this invoice is due by."""
  due_date: Date
}

"""
The input object that defines the fields for the createInvoiceTemplate mutation.
"""
input CreateInvoiceTemplateMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """IDs of `Companies`."""
  company_ids: [Int64Bit]
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """The content of an Invoice Template which includes a remittance slip."""
  with_remittance: Clob
  """
  The content of an Invoice Template which does not include a remittance slip.
  """
  without_remittance: Clob
  """A note about this entity."""
  note: NoteMutationInput
}
```
