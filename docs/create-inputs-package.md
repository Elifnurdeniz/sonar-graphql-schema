```graphql
"""
The input object that defines the fields for the createPackage mutation.
"""
input CreatePackageMutationInput {
  """A descriptive name."""
  name: String!
  """Whether or not this is enabled."""
  enabled: Boolean!
  """The ID of the company that this entity operates under."""
  company_id: Int64Bit
  """The services in this package."""
  services: [PackageServiceMutationInput]!
  """
  Setting to indicate if services in this package should be rolled up into a package total when this package is displayed.
  """
  rollup_services: Boolean
  """A note about this entity."""
  note: NoteMutationInput
}
```
