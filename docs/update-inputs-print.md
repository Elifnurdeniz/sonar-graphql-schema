```graphql
"""
The input object that defines the fields for the updatePrintToMailOrderError mutation.
"""
input UpdatePrintToMailOrderErrorMutationInput {
  """Whether or not the error has been marked as resolved."""
  resolved: Boolean
}

"""
The input object that defines the fields for the updatePrintToMailSettings mutation.
"""
input UpdatePrintToMailSettingsMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """The print method for the print to mail batch."""
  print_method: PrintToMailPrintMethod
  """The print type for the print to mail batch."""
  print_type: PrintToMailPrintType
  """A notification is sent if Print to Mail funds fall below this value."""
  low_funds_threshold: Int
}
```
