```graphql
"""Credentials for the bank account processor."""
input BankAccountProcessorCredentialInput {
  """The credential for the bank account provider."""
  credential: BankAccountProviderCredential!
  """The credential value."""
  value: String!
}
```
