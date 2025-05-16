```graphql
"""
The input object that defines the fields for the updateExternalMarketingProvider mutation.
"""
input UpdateExternalMarketingProviderMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """
  The credentials to use to authenticate against the external marketing provider.
  """
  external_marketing_provider_credentials: [ExternalMarketingProviderCredentialInput]
}
```
