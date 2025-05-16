```graphql
"""
The input object that defines the fields for the createExternalMarketingProvider mutation.
"""
input CreateExternalMarketingProviderMutationInput {
  """
  The `ExternalMarketingProviderType` for 3rd party external marketing integration.
  """
  provider: ExternalMarketingProviderType!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """
  The credentials to use to authenticate against the external marketing provider.
  """
  external_marketing_provider_credentials: [ExternalMarketingProviderCredentialInput]!
}
```
