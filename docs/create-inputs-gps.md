```graphql
"""
The input object that defines the fields for the createGpsTrackingProvider mutation.
"""
input CreateGpsTrackingProviderMutationInput {
  """A descriptive name."""
  provider: GpsTrackingProviderType!
  """Whether or not this is enabled."""
  enabled: Boolean! = true
  """`GpsTrackingProvider` Credentials."""
  gps_tracking_provider_credentials: [GpsTrackingProviderCredentialInput]!
}
```
