```graphql
"""
The input object that defines the fields for the updateContract mutation.
"""
input UpdateContractMutationInput {
  """The custom message."""
  custom_message: Text
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `custom_message` to null."""
  unset_custom_message: Boolean
}

"""
The input object that defines the fields for the updateContractTemplate mutation.
"""
input UpdateContractTemplateMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """A descriptive name."""
  name: String
  """The body."""
  body: Text
  """The term in months."""
  term_in_months: Int
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of a `TicketGroup`."""
  ticket_group_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
  """Setting this value to `true` will set `term_in_months` to null."""
  unset_term_in_months: Boolean
  """Setting this value to `true` will set `company_id` to null."""
  unset_company_id: Boolean
  """Setting this value to `true` will set `ticket_group_id` to null."""
  unset_ticket_group_id: Boolean
}
```
