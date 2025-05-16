```graphql
"""
The input object that defines the fields for the createContract mutation.
"""
input CreateContractMutationInput {
  """The ID of a `ContractTemplate`."""
  contract_template_id: Int64Bit!
  """The ID of an Account."""
  account_id: Int64Bit!
  """The ID of the contact that owns this."""
  contact_id: Int64Bit!
  """The custom message."""
  custom_message: Text
  """A note about this entity."""
  note: NoteMutationInput
}

"""
The input object that defines the fields for the createContractTemplate mutation.
"""
input CreateContractTemplateMutationInput {
  """A descriptive name."""
  name: String!
  """The body."""
  body: Text!
  """The term in months."""
  term_in_months: Int
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The ID of a `TicketGroup`."""
  ticket_group_id: Int64Bit
  """A note about this entity."""
  note: NoteMutationInput
}
```
