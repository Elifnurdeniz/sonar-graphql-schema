```graphql
"""Provides credentials for an inline device."""
input InlineDeviceAuthenticationCredentialMutationInput {
  """An individual credential to authenticate to an inline device."""
  credential: InlineDeviceAuthenticationCredential!
  """The credential value (e.g. username, password, etc.)"""
  value: String!
}
```
