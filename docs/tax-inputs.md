```graphql
"""Credentials for a tax provider."""
input TaxProviderCredentialMutationInput {
  """An individual credential to authenticate to a tax provider."""
  credential: TaxProviderCredentialType!
  """The credential value (e.g. username, password, etc.)"""
  value: String!
}
```
