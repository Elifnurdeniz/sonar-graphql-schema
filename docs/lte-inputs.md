```graphql
"""Credentials for an LTE provider."""
input LteProviderAuthenticationCredentialMutationInput {
  """An individual credential to authenticate to an LTE provider."""
  credential: LteProviderAuthenticationCredential!
  """The credential value (e.g. username, password, etc.)"""
  value: String!
}
```
