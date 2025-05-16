```graphql
"""
The input object that defines the fields for the createPayPalCredential mutation.
"""
input CreatePayPalCredentialMutationInput {
  """The client ID for PayPal."""
  client_id: String!
  """The client secret for PayPal."""
  client_secret: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """A note about this entity."""
  note: NoteMutationInput
}
```
