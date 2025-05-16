```graphql
"""
The input object that defines the fields for the updateGpsTrackingProvider mutation.
"""
input UpdateGpsTrackingProviderMutationInput {
  """Whether or not this is enabled."""
  enabled: Boolean
  """`GpsTrackingProvider` Credentials."""
  gps_tracking_provider_credentials: [GpsTrackingProviderCredentialInput]
}
```
