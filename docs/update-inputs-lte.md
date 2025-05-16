```graphql
"""
The input object that defines the fields for the updateLteProvider mutation.
"""
input UpdateLteProviderMutationInput {
  """A descriptive name."""
  name: String
  """Whether or not this is enabled."""
  enabled: Boolean
  """Automatically detach UE when account is changed to delinquency status."""
  deactivate_on_delinquency: Boolean
  """Write PDN address allocation into BreezeVIEW."""
  write_pdn_address_allocation: Boolean
  """Whether or not a floating license model is used with BreezeVIEW."""
  floating_license: Boolean
  """Credentials for the LTE provider."""
  lte_provider_credentials: [LteProviderAuthenticationCredentialMutationInput]
  """A note about this entity."""
  note: NoteMutationInput
}
```
