```graphql
"""Credentials for the external marketing processor."""
input ExternalMarketingProviderCredentialInput {
  """
  The credentials to use to authenticate against the external marketing provider.
  """
  key: ExternalMarketingProviderAuthCredential!
  """
  The value of the credential key used to authenticate against the external marking provider.
  """
  value: String!
}
```
