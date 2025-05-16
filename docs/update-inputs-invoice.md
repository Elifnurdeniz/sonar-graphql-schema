```graphql
"""
The input object that defines the fields for the updateInvoiceAttachment mutation.
"""
input UpdateInvoiceAttachmentMutationInput {
  """A descriptive name."""
  name: String
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
  """Setting this value to `true` will set `start` to null."""
  unset_start: Boolean
  """Setting this value to `true` will set `end` to null."""
  unset_end: Boolean
}

"""
The input object that defines the fields for the updateInvoiceMessage mutation.
"""
input UpdateInvoiceMessageMutationInput {
  """A descriptive name."""
  name: String
  """The message."""
  message: String
  """IDs of `AccountType`s."""
  account_type_ids: [Int64Bit]
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the updateInvoice mutation.
"""
input UpdateInvoiceMutationInput {
  """
  If an invoice is frozen, payments will not be automatically applied to it, and it cannot be modified.
  """
  frozen: Boolean
  """A custom message to print on the invoice."""
  message: String
  """Setting this value to `true` will set `message` to null."""
  unset_message: Boolean
}

"""
The input object that defines the fields for the updateInvoiceTemplate mutation.
"""
input UpdateInvoiceTemplateMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
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
