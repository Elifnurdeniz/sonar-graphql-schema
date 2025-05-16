```graphql
"""Provides credentials for a cable modem provisioner."""
input CableModemAuthenticationCredentialMutationInput {
  """An individual credential to authenticate to a cable modem provisioner."""
  credential: CableModemProvisionerAuthenticationCredential!
  """The credential value (e.g. username, password, etc.)"""
  value: String!
}
```
