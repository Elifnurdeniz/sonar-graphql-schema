```graphql
"""
The input object that defines the fields for the resendAutoreply mutation.
"""
input ResendAutoreplyMutationInput {
  """The ID of a `Ticket`."""
  ticket_id: Int64Bit!
  """An email address."""
  to_email_address: EmailAddress!
}
```
