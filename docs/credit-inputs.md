```graphql
"""
The credentials for the credit card processor. Generally some type of API key or authentication information.
"""
input CreditCardProcessorCredentialInput {
  """The credential name."""
  credential: CreditCardProviderCredential!
  """The credential value."""
  value: String!
}
```
