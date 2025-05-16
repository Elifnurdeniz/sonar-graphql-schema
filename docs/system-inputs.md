```graphql
"""Credentials for the system backup destination provider."""
input SystemBackupDestinationCredentialInput {
  """
  The name of a credential used to authenticate against a system backup destination provider.
  """
  credential: SystemBackupDestinationProviderCredential!
  """
  The value of a credential used to authenticate against a system backup destination provider.
  """
  value: String!
}
```
