```graphql
"""A service in a package."""
input PackageServiceMutationInput {
  """The ID of a Service."""
  service_id: Int64Bit!
  """The quantity for this service."""
  quantity: Int = 1
}
```
